// Cloudflare Pages Function: POST /api/chat. Same protocol as serve.py's endpoint
// (SSE lines of {"t"}, {"note"}, {"error"[, "discard"]}, {"done"}), so the one
// index.html works on both hosts.
//
// Settings (Pages project > Settings > Variables and Secrets):
//   ANTHROPIC_API_KEY  secret, required
//   MODEL / EFFORT / MAX_TOKENS  optional overrides
import Anthropic from "@anthropic-ai/sdk";
import { SYSTEM_PROMPT } from "../_prompt.js";

const MAX_BODY = 512 * 1024;
const MAX_TURNS = 60;
const MAX_CHARS = 40000;

function validate(payload) {
  const msgs = payload && payload.messages;
  if (!Array.isArray(msgs) || msgs.length < 1 || msgs.length > MAX_TURNS) {
    throw new Error("Conversation is empty or too long. Start a new chat.");
  }
  const clean = msgs.map((m, i) => {
    const role = m && m.role;
    const content = m && m.content;
    if (role !== (i % 2 === 0 ? "user" : "assistant")) {
      throw new Error("Messages must alternate, starting with the user.");
    }
    if (typeof content !== "string" || !content.trim() || content.length > MAX_CHARS) {
      throw new Error(`Each message must be 1-${MAX_CHARS} characters.`);
    }
    return { role, content };
  });
  if (clean[clean.length - 1].role !== "user") throw new Error("The last message must be from the user.");
  return clean;
}

const json = (status, obj) =>
  new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });

export async function onRequestPost(context) {
  const { request, env } = context;
  if (!env.ANTHROPIC_API_KEY) return json(500, { error: "Server API key is not configured. Tell the site owner." });

  let messages;
  try {
    const raw = await request.text();
    if (!raw || raw.length > MAX_BODY) throw new Error("Request too large.");
    let payload;
    try { payload = JSON.parse(raw); } catch { return json(400, { error: "Bad JSON." }); }
    messages = validate(payload);
  } catch (e) {
    return json(400, { error: e.message });
  }

  const client = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });
  const { readable, writable } = new TransformStream();
  const writer = writable.getWriter();
  const enc = new TextEncoder();
  const send = (obj) => writer.write(enc.encode(`data: ${JSON.stringify(obj)}\n\n`));

  const pump = (async () => {
    const started = Date.now();
    try {
      const stream = client.beta.messages.stream({
        model: env.MODEL || "claude-opus-5",
        max_tokens: Number(env.MAX_TOKENS) || 32000,
        system: SYSTEM_PROMPT,
        messages,
        cache_control: { type: "ephemeral" },
        output_config: { effort: env.EFFORT || "medium" },
        // Retry safety-classifier declines on Anthropic's recommended model.
        betas: ["server-side-fallback-2026-07-01"],
        fallbacks: "default",
      });
      for await (const ev of stream) {
        if (ev.type === "content_block_delta" && ev.delta.type === "text_delta") await send({ t: ev.delta.text });
      }
      const final = await stream.finalMessage();
      if (final.stop_reason === "refusal") {
        await send({ error: "The model declined to answer that. Try rephrasing.", discard: true });
      } else if (final.stop_reason === "max_tokens") {
        await send({ note: "Reply was cut off at the length limit." });
      }
      await send({ done: true });
      const u = final.usage;
      // Metadata only. Never log conversation content.
      console.log(`chat ok turns=${messages.length} in=${u.input_tokens} cached=${u.cache_read_input_tokens} out=${u.output_tokens} model=${final.model} ${((Date.now() - started) / 1000).toFixed(1)}s`);
    } catch (e) {
      let msg = "Couldn't reach the model. Try again.";
      if (e instanceof Anthropic.RateLimitError) msg = "The coach is busy. Try again in a minute.";
      else if (e instanceof Anthropic.AuthenticationError) msg = "Server API key is invalid. Tell the site owner.";
      else if (e instanceof Anthropic.APIError && e.status) msg = `Upstream error (${e.status}). Try again.`;
      console.log(`chat error: ${e.name} ${e.status || ""}`);
      try { await send({ error: msg }); } catch {}
    } finally {
      try { await writer.close(); } catch {}
    }
  })();
  context.waitUntil(pump);

  return new Response(readable, {
    headers: {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Accel-Buffering": "no",
    },
  });
}
