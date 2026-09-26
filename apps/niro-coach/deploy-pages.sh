#!/bin/bash
# Deploy the Niro Method coach to Cloudflare Pages (static page + /api/chat Function).
#
# One-time setup, in this order:
#   1. bash deploy-pages.sh --create      creates the Pages project (no deploy)
#   2. Cloudflare dashboard > Zero Trust > Access > Applications > Add > Self-hosted:
#        domain niro-coach.pages.dev (add *.niro-coach.pages.dev too, for preview URLs),
#        policy: Allow, Emails = the people you're sharing with (email one-time PIN).
#   3. bash deploy-pages.sh               sets the API key secret on first run, then deploys
#
# After that, just run step 3 whenever the page, function or skill changes.
# The deploy refuses to go out unless Access is protecting the site, because an open
# /api/chat would let anyone spend on the Anthropic key.
#
# Credentials: CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID from the environment, or
# cf_pages_token + cf_account_id in ~/niro-coach-live/config.json.
set -euo pipefail

PROJECT="${PROJECT:-niro-coach}"
SITE="https://$PROJECT.pages.dev"
HERE="$(cd "$(dirname "$0")" && pwd)"
CFG="$HOME/niro-coach-live/config.json"
cd "$HERE"   # wrangler finds functions/ and node_modules/ relative to the cwd

die() { printf '\n\033[31mERROR: %s\033[0m\n' "$*" >&2; exit 1; }

cfg_get() { [ -f "$CFG" ] && python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get(sys.argv[2],""))' "$CFG" "$1" || true; }
export CLOUDFLARE_API_TOKEN="${CLOUDFLARE_API_TOKEN:-$(cfg_get cf_pages_token)}"
export CLOUDFLARE_ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-$(cfg_get cf_account_id)}"
[ -n "$CLOUDFLARE_API_TOKEN" ] && [ -n "$CLOUDFLARE_ACCOUNT_ID" ] || die "Set CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID (or cf_pages_token / cf_account_id in $CFG)."

WR="$(command -v wrangler || true)"
[ -n "$WR" ] || die "wrangler not found. Run: npm i -g wrangler"

if [ "${1:-}" = "--create" ]; then
  "$WR" pages project create "$PROJECT" --production-branch main --compatibility-date 2026-09-01
  echo "Created. Now put Cloudflare Access in front of $SITE (see the top of this script), then run: bash deploy-pages.sh"
  exit 0
fi

# 1. Access must be in front. An Access-protected host redirects anonymous
#    requests to <team>.cloudflareaccess.com.
loc=$(curl -s -o /dev/null -w '%{redirect_url}' "$SITE/" || true)
case "$loc" in
  *cloudflareaccess.com*) echo "Access: on ($SITE redirects to login)";;
  *) [ "${SKIP_ACCESS_CHECK:-}" = 1 ] || die "$SITE is not behind Cloudflare Access (no redirect to cloudflareaccess.com). Set up Access first; see the top of this script.";;
esac

# 2. Build the system prompt from the skill, and install the SDK for bundling.
python3 build_prompt.py
npm install --silent

# 3. The Anthropic key lives only in Cloudflare's secret store.
if ! "$WR" pages secret list --project-name "$PROJECT" 2>/dev/null | grep ANTHROPIC_API_KEY >/dev/null; then
  echo "Setting ANTHROPIC_API_KEY for $PROJECT (paste it when asked):"
  "$WR" pages secret put ANTHROPIC_API_KEY --project-name "$PROJECT"
fi

# 4. Stage ONLY the files meant for the CDN (top-level page + vendored libraries).
STAGE="$HERE/.deploy-stage"
rm -rf "$STAGE"
mkdir -p "$STAGE/vendor"
cp public/index.html "$STAGE/"
cp public/vendor/marked.min.js public/vendor/purify.min.js "$STAGE/vendor/"

"$WR" pages deploy "$STAGE" --project-name "$PROJECT" --branch main --commit-dirty=true
rm -rf "$STAGE"

# 5. The chat endpoint must be gated too, not just the page.
code=$(curl -s -o /dev/null -w '%{http_code}' -X POST "$SITE/api/chat" -H 'Content-Type: application/json' -d '{"messages":[{"role":"user","content":"ping"}]}' || true)
case "$code" in
  302|401|403) echo "Access: /api/chat blocked for anonymous requests ($code)";;
  *) echo "WARNING: anonymous POST to /api/chat returned $code. Check the Access application covers the whole domain.";;
esac
echo "Deployed: $SITE"
