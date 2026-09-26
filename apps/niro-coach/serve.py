#!/usr/bin/env python3
"""Niro Method coach: static page + /api/chat streaming endpoint.

Binds 127.0.0.1 only; Tailscale serve publishes it to the tailnet. The API key
lives in config.json ONE LEVEL ABOVE public/, so the static server can't serve it.
"""
import http.server, json, os, sys, time

import anthropic

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
CFG = os.path.join(HERE, "config.json")
PROMPT = os.path.join(HERE, "prompt", "system-prompt.md")
SELF = os.path.abspath(__file__)
MTIME = os.path.getmtime(SELF)

cfg = json.load(open(CFG)) if os.path.exists(CFG) else {}
PORT = int(cfg.get("port", 8793))
MODEL = cfg.get("model", "claude-opus-5")
EFFORT = cfg.get("effort", "medium")
MAX_TOKENS = int(cfg.get("max_tokens", 32000))
# Fixed bytes on every request, so the prompt cache keeps hitting.
SYSTEM_PROMPT = open(PROMPT).read()

client = anthropic.Anthropic(api_key=cfg.get("anthropic_api_key") or None)

MAX_BODY = 512 * 1024
MAX_TURNS = 60
MAX_CHARS = 40000


def validate(payload):
    """Return a clean messages list, or raise ValueError with a user-safe reason."""
    msgs = payload.get("messages") if isinstance(payload, dict) else None
    if not isinstance(msgs, list) or not 1 <= len(msgs) <= MAX_TURNS:
        raise ValueError("Conversation is empty or too long. Start a new chat.")
    clean = []
    for i, m in enumerate(msgs):
        role = m.get("role") if isinstance(m, dict) else None
        content = m.get("content") if isinstance(m, dict) else None
        if role != ("user" if i % 2 == 0 else "assistant"):
            raise ValueError("Messages must alternate, starting with the user.")
        if not isinstance(content, str) or not content.strip() or len(content) > MAX_CHARS:
            raise ValueError("Each message must be 1-%d characters." % MAX_CHARS)
        clean.append({"role": role, "content": content})
    if clean[-1]["role"] != "user":
        raise ValueError("The last message must be from the user.")
    return clean


def log(msg):
    # Metadata only. Never log conversation content: users paste live deal details.
    sys.stderr.write("%s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=PUBLIC, **kw)

    def do_GET(self):
        try:  # hot-reload: re-exec when this file changes
            if os.path.getmtime(SELF) != MTIME:
                os.execv(sys.executable, [sys.executable] + sys.argv)
        except Exception:
            pass
        return super().do_GET()

    def do_POST(self):
        # Tailscale strips the /niro mount prefix; accept either form anyway.
        if not self.path.split("?")[0].endswith("/api/chat"):
            return self.send_error(404)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            if not 0 < n <= MAX_BODY:
                raise ValueError("Request too large.")
            messages = validate(json.loads(self.rfile.read(n)))
        except json.JSONDecodeError:
            return self._json(400, {"error": "Bad JSON."})
        except ValueError as e:
            return self._json(400, {"error": str(e)})

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()
        started = time.time()
        try:
            with client.beta.messages.stream(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=messages,
                cache_control={"type": "ephemeral"},
                output_config={"effort": EFFORT},
                # Retry safety-classifier declines on Anthropic's recommended model.
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
            ) as stream:
                for text in stream.text_stream:
                    self._event({"t": text})
                final = stream.get_final_message()
            u = final.usage
            if final.stop_reason == "refusal":
                # A mid-stream decline leaves partial text: tell the page to drop it.
                self._event({"error": "The model declined to answer that. Try rephrasing.", "discard": True})
            elif final.stop_reason == "max_tokens":
                self._event({"note": "Reply was cut off at the length limit."})
            self._event({"done": True})
            log("chat ok turns=%d in=%s cached=%s out=%s model=%s %.1fs" % (
                len(messages), u.input_tokens, u.cache_read_input_tokens,
                u.output_tokens, final.model, time.time() - started))
        except (BrokenPipeError, ConnectionResetError):
            log("chat client disconnected")
        except anthropic.RateLimitError:
            self._safe_event({"error": "The coach is busy. Try again in a minute."})
            log("chat rate limited")
        except anthropic.AuthenticationError:
            self._safe_event({"error": "Server API key is invalid. Tell the site owner."})
            log("chat auth error: check anthropic_api_key in config.json")
        except anthropic.APIStatusError as e:
            self._safe_event({"error": "Upstream error (%s). Try again." % e.status_code})
            log("chat api error %s: %s" % (e.status_code, e.message))
        except anthropic.APIConnectionError:
            self._safe_event({"error": "Couldn't reach the model. Try again."})
            log("chat connection error")

    def _event(self, obj):
        self.wfile.write(b"data: " + json.dumps(obj).encode() + b"\n\n")
        self.wfile.flush()

    def _safe_event(self, obj):
        try:
            self._event(obj)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    # Threaded: a streaming chat must not block page loads or other chats.
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    http.server.ThreadingHTTPServer.daemon_threads = True
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        log("niro-coach on http://127.0.0.1:%d model=%s effort=%s" % (PORT, MODEL, EFFORT))
        httpd.serve_forever()
