"""Interactive REPL to talk to the current therapist agent."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agent.therapist import respond


def main():
    print("Therapist ready. Type 'quit' to exit.\n")
    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user.lower() in {"quit", "exit"}:
            break
        if not user:
            continue
        reply = respond(user)
        print(f"\nTherapist: {reply}\n")


if __name__ == "__main__":
    main()
