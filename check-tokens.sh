#!/usr/bin/env bash
# Fails if any hex colour literal appears outside tokens.css — INCLUDING in
# comments. A hex in a comment goes stale exactly like a duplicated value, and
# it is how the next person learns the wrong number. Name the token, not the hex.
#
# The palette is closed. If you are choosing a colour, you are off-spec.
#
#   ./check-tokens.sh <dir>
set -uo pipefail
ROOT="${1:-.}"

HITS=$(grep -rInE '#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?\b' "$ROOT" \
  --include='*.css' --include='*.js'  --include='*.jsx' \
  --include='*.ts'  --include='*.tsx' --include='*.astro' \
  --include='*.svelte' --include='*.vue' --include='*.html' \
  --exclude='tokens.css' \
  --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=dist \
  --exclude-dir=.astro --exclude-dir=.next --exclude-dir=build 2>/dev/null)

if [ -n "$HITS" ]; then
  echo "OFF-SPEC — hex colour literals found outside tokens.css:"
  echo
  echo "$HITS"
  echo
  echo "The palette is closed. Use a token from tokens.css."
  echo "If you genuinely need a new value, add it to tokens.css WITH a"
  echo "contrast entry in check_contrast.py — never inline."
  echo "This applies to comments too: name the token, not the hex."
  exit 1
fi

echo "ok — no hex literals outside tokens.css"
