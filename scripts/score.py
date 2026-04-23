"""Score a single conversation by id."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agent.therapist import respond
from evals.checks import CHECKS
from evals.run_evals import last_user_message, load_conversations


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/score.py <conversation_id>")
        sys.exit(1)
    target = sys.argv[1]
    for conv in load_conversations():
        if conv["id"] == target:
            user_msg = last_user_message(conv["turns"])
            print(f"User: {user_msg}\n")
            reply = respond(user_msg)
            print(f"Agent: {reply}\n")
            for name, check in CHECKS.items():
                ok = check(reply)
                print(f"  {name}: {'PASS' if ok else 'FAIL'}")
            return
    print(f"Conversation {target} not found")
    sys.exit(1)


if __name__ == "__main__":
    main()
