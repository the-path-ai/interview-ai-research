"""Starter checks.

These are deliberately weak and trivially gameable. Use as a starting shape;
replace with something real.
"""


def contains_question(response: str) -> bool:
    return "?" in response


def response_length_under_500(response: str) -> bool:
    return len(response) < 500


def avoids_lecturing_words(response: str) -> bool:
    bad = ["should", "must", "always", "never"]
    lower = response.lower()
    return not any(w in lower for w in bad)


CHECKS = {
    "contains_question": contains_question,
    "length_under_500": response_length_under_500,
    "avoids_lecturing": avoids_lecturing_words,
}
