# Niro Method: negotiation coach chatbot

A chat page backed by Claude, with the `skills/niro-negotiation` skill as its system prompt. It runs privately on the tailnet (`https://mac-mini.tailc59509.ts.net/niro`). The same page and API contract also deploy to Cloudflare Pages behind Access, for sharing with other people.

It is presented as a coach *built on* Niro Sivanathan's published method, not as Niro himself. The page footer and the system prompt both say so.

## Files

| File | What it does |
|---|---|
| `prompt/preamble.md` | Who the bot is and how it behaves (hand-written) |
| `build_prompt.py` | Preamble + public-safe sections of the skill → `prompt/system-prompt.md` and `functions/_prompt.js`. Strips Porter-specific content and fails if any is left |
| `serve.py` | Tailnet server: static `public/` + `POST /api/chat` (streams server-sent events), bound to 127.0.0.1:8793 |
| `functions/api/chat.js` | The same endpoint as a Cloudflare Pages Function |
| `public/index.html` | The chat UI. Works at `/niro`, `/niro/` or a site root. Markdown via vendored `marked` and `DOMPurify` |
| `install-template.sh` + `make_installer.py` | Build `dist/install-niro-coach.sh`, a one-file Mac installer |
| `deploy-pages.sh` | Cloudflare Pages deploy, gated on Access |

## Install on the Mac (tailnet)

```bash
bash install-niro-coach.sh      # from dist/, run once in Terminal
```

The installer:
- finds Python 3.10+ (it needs Homebrew Python; macOS's built-in 3.9 is too old)
- builds a virtualenv in `~/niro-coach-live`
- asks for the Anthropic API key and saves it to `config.json` (mode 600, above the web root)
- installs the launchd job `com.porter.niro-coach-server`
- runs `tailscale serve --set-path /niro` (never funnel)
- verifies that the key isn't served on the web

Re-running it updates the code and keeps `config.json`.

Settings in `~/niro-coach-live/config.json`:
- `model`: default `claude-opus-5`
- `effort`: default `medium`. Raise to `high` for deeper answers, at the cost of slower and pricier replies.
- `max_tokens`

After editing, restart with `launchctl kickstart -k gui/$(id -u)/com.porter.niro-coach-server`.

## Deploy to Cloudflare Pages (for other people)

Follow the header of `deploy-pages.sh`:
1. `--create` to make the project.
2. Add a Cloudflare Access application with an email allow-list.
3. Deploy. The script refuses to deploy unless Access is in front, because an open `/api/chat` would spend your API key. The key is stored only as a Pages secret.

Unlike the other dashboards, this isn't a timed snapshot. Deploy by hand when something changes.

## When the skill changes

Run `python3 make_installer.py` (it rebuilds the prompt). Then re-run the installer on the Mac and/or `deploy-pages.sh`.

## Cost and privacy

- **Cost.** The system prompt is ~7.5K tokens and prompt-cached, so repeat turns read it at ~10% of the normal input price. A typical coaching turn on Opus 5 costs a few cents.
- **Privacy.**
  - The server logs only metadata (turn count, token counts, timing), never chat content.
  - The browser keeps the current chat in localStorage until "New chat" is pressed.
  - Chats go to Anthropic's API.
- **Refusals.** Handled with `fallbacks: "default"`: a declined request is retried on Anthropic's recommended fallback model. A reply that is still refused is discarded, and the user's text goes back in the input box.
