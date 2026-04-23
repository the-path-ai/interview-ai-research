# Conversation schema

Each line in `seed_conversations.jsonl` is a JSON object:

```json
{
  "id": "conv_001",
  "turns": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "..."},
    ...
  ]
}
```

- Conversations alternate user/assistant turns, always starting with `user`.
- The `assistant` turns in the seed data are the **prior agent's** responses — i.e. what you are trying to improve on.
