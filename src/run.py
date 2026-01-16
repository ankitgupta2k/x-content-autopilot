from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, UTC
import random

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "autopilot.yaml"
DATA_PATH = ROOT / "data" / "posts.json"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_history() -> list[dict]:
    if not DATA_PATH.exists():
        return []
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_history(history: list[dict]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with DATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def build_post(cfg: dict) -> str:
    topics = cfg["content"]["topic_rotation"]
    topic = random.choice(topics)

    # Simple placeholder content (we’ll replace this with OpenAI generation next)
    body = (
        f"Idea → Impact: A simple way to think about {topic.lower()}.\n\n"
        f"Start with the smallest workflow that creates value, then add guardrails.\n\n"
        f"What's one process you’d automate this month?"
    )

    hashtags = cfg.get("output", {}).get("hashtags", [])
    hashtags_max = cfg["content"]["constraints"]["hashtags_max"]
    if cfg.get("output", {}).get("add_hashtags", False) and hashtags:
        tag_str = " ".join(f"#{t}" for t in hashtags[:hashtags_max])
        body = f"{body}\n\n{tag_str}"

    max_chars = cfg["content"]["constraints"]["max_chars"]
    if len(body) > max_chars:
        body = body[: max_chars - 1] + "…"
    return body


def main() -> None:
    cfg = load_config()
    history = load_history()

    post = build_post(cfg)

    record = {
        "ts": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "text": post,
        "mode": "dry-run" if not cfg["schedule"].get("autopublish", False) else "autopublish",
    }
    history.append(record)
    save_history(history)

    print("\n=== DRAFT POST (DRY-RUN) ===\n")
    print(post)
    print("\nSaved to data/posts.json")


if __name__ == "__main__":
    main()
