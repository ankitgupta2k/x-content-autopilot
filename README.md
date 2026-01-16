# x-content-autopilot

AI-driven daily X (Twitter) content autopilot: generates posts from a ruleset + prompts, validates quality, then schedules/posts and logs results.

## What it does
- ✅ Generates daily posts (single tweet or thread) based on your ruleset
- ✅ Enforces guardrails: length, tone, hashtag limits, banned phrases, duplicate checks
- ✅ Posts automatically (or approval mode)
- ✅ Logs every post + metadata for analytics

## How it works (pipeline)
1. Load ruleset + prompt templates
2. Pick today’s topic/format from rotation
3. Generate 2–3 candidates via LLM
4. Validate (length, similarity vs last N posts, etc.)
5. Publish (Typefully API or X API)
6. Log to CSV/Google Sheet

## Repo structure (planned)
