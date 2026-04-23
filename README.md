# Pathos Therapist — 60 minute build task

Our AI therapist isn't good enough. Your job: **make it meaningfully better in 60 minutes.**

## Rules

- Use any tools, libraries, and AI assistants you want.
- Run `bash setup.sh` using the decryption password provided to get API keys loaded
- Think out loud.
- Narrow in on a few promising ideas and actually implement something.

## What's in the repo

- `agent/therapist.py` — the current (naive) therapist agent
- `data/seed_conversations.jsonl` — 25 conversations from prior sessions
- `evals/run_evals.py` — a starter evaluation harness (weak on purpose)
- `scripts/chat.py` — talk to the agent interactively
- `scripts/score.py` — score a single conversation by id

## Setup

```bash
bash setup.sh                    # loads API keys (use the decryption password provided)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Sanity check

```bash
python evals/run_evals.py        # runs the starter eval over all 25 conversations
python scripts/chat.py           # talk to the agent
```

Default model is `gpt-4o-mini`. Change it however you like.

## Evaluation

At the end of the session, your system will be run against a held-out set of 10 conversations in `.heldout/` that you cannot see. The final comparison is **before vs. after on the held-out set**. Please do not inspect or modify `.heldout/`.

## You decide

Prompts, architecture, memory, retrieval, eval rigor, simulating data, credit assignment, whatever you think moves the needle most. Ship and defend your choices.

There is certainly no "correct answer" to this interview, by any means. You should use ALL tools at your disposal. There's no way to cheat.
