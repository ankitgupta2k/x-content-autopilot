---
title: x-content-autopilot
---

# x-content-autopilot

An **AI-driven daily content autopilot for X (Twitter)**.

It turns your **ruleset + prompt templates** into high-quality posts, applies guardrails, then **schedules/posts** and **logs** everything so the system improves over time.

---

## Why this exists
Most content automation ends up sounding generic—or worse, spammy.  
This project aims for **safe, consistent, brand-aligned output**:

- predictable cadence
- consistent voice
- low repetition
- measurable improvement

---

## What it does

### 1) Generate
- Selects a topic + format from your rotation
- Produces 2–3 candidate posts (single post or thread)

### 2) Validate (Guardrails)
- X-safe length limits
- Hashtag and CTA limits
- Banned phrases / tone checks
- Duplicate/similarity check vs recent posts

### 3) Publish
- **Dry-run mode:** generate + log only
- **Auto mode:** schedule/post automatically
- **Approval mode (optional):** send draft for one-click approval

Publishing options:
- Typefully API (simpler scheduling)
- Direct X API (full control)

### 4) Log
Stores post text + metadata (date, topic, format, score) to enable weekly review and iteration.

---

## Single Source of Truth
Configuration lives in:
- `config/autopilot.yaml`

This file controls cadence, topic rotation, guardrails, CTAs, hashtags, and publishing mode.

---

## Planned structure
- config/ # autopilot.yaml (single source of truth)
- src/ # generate/validate/publish pipeline
- data/ # post history for duplicate checks
- .github/workflows # daily scheduler (GitHub Actions)


---

## Roadmap
- [ ] Config v1 (`config/autopilot.yaml`)
- [ ] Generator + validator (dry-run)
- [ ] Duplicate checker (last 30 posts)
- [ ] Daily GitHub Actions schedule
- [ ] Posting via Typefully / X API
- [ ] Logging + weekly performance summary
- [ ] Optional approval workflow

---

## Safety / compliance
No auto-follow/unfollow. Keep cadence human-like (start with 1 post/day). Add approval mode until the voice is stable.

_Last updated: Jan 2026_

