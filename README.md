# Pathos Therapist — 60 minute build task

Our AI therapist isn't good enough. Your job: **make it meaningfully better in 60 minutes.**

## Rules

- Use any tools, libraries, and AI assistants you want.
- Bring your own API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, whatever). Export them as env vars before running.
- Ship something runnable. Don't leave it half-broken.
- Think out loud.

## What's in the repo

- `agent/therapist.py` — the current (naive) therapist agent
- `data/seed_conversations.jsonl` — 25 conversations from prior sessions
- `evals/run_evals.py` — a starter evaluation harness (weak on purpose)
- `scripts/chat.py` — talk to the agent interactively
- `scripts/score.py` — score a single conversation by id

## Sanity check

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python evals/run_evals.py        # runs the starter eval over all 25 conversations
python scripts/chat.py           # talk to the agent
```

Default model is `gpt-4o-mini`. Change it however you like.

## Evaluation

At the end of the session, your system will be run against a held-out set of 10 conversations in `.heldout/` that you cannot see. The final comparison is **before vs. after on the held-out set**. Please do not inspect or modify `.heldout/`.

## You decide

Prompts, architecture, memory, retrieval, eval rigor, training data sketches, per-turn credit assignment, whatever you think moves the needle most. Ship and defend your choices.
