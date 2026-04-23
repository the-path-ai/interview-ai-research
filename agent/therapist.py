"""The current therapist agent. Naive on purpose."""

from openai import OpenAI

from agent.prompts import SYSTEM_PROMPT

_client = OpenAI()

DEFAULT_MODEL = "gpt-4o-mini"


def respond(user_message: str, model: str = DEFAULT_MODEL) -> str:
    """Produce a single therapist response to a user message.

    No conversation history. No memory. No safety routing. No structure.
    """
    completion = _client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    )
    return completion.choices[0].message.content or ""
