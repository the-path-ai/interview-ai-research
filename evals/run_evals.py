"""Run the starter checks across all seed conversations.

For each conversation, we take the last user message, generate a fresh
agent response, and score it. This is intentionally simplistic.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rich.console import Console
from rich.table import Table

from agent.therapist import respond
from evals.checks import CHECKS

DATA_PATH = Path(__file__).parent.parent / "data" / "seed_conversations.jsonl"


def last_user_message(turns):
    for turn in reversed(turns):
        if turn["role"] == "user":
            return turn["content"]
    return None


def load_conversations(path: Path = DATA_PATH):
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    console = Console()
    conversations = load_conversations()
    console.print(f"[bold]Loaded {len(conversations)} conversations[/bold]")

    table = Table(title=f"Starter Eval ({len(conversations)} conversations)")
    table.add_column("id")
    for name in CHECKS:
        table.add_column(name)

    totals = {name: 0 for name in CHECKS}
    for i, conv in enumerate(conversations, 1):
        console.print(f"[dim]Running conversation {i}/{len(conversations)}: {conv['id']}[/dim]")
        user_msg = last_user_message(conv["turns"])
        reply = respond(user_msg)
        row = [conv["id"]]
        for name, check in CHECKS.items():
            passed = check(reply)
            totals[name] += int(passed)
            row.append("[green]PASS[/green]" if passed else "[red]FAIL[/red]")
        table.add_row(*row)

    console.print(table)
    n = len(conversations)
    console.print()
    for name, count in totals.items():
        console.print(f"  {name}: {count}/{n}")


if __name__ == "__main__":
    main()
