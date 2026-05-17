"""Experimental severity scoring for aggregate NLP research.

This module is not clinically validated and must not be used for diagnosis.
"""

from __future__ import annotations

import re


INTENSIFIERS = {"severe", "extreme", "unbearable", "constant", "always", "panic", "crisis"}
QUALIFIERS = {"mild", "sometimes", "occasionally", "manageable", "better", "improving"}
MEDICATION_TERMS = {"prozac", "zoloft", "lexapro", "adderall", "ritalin", "vyvanse", "xanax"}
RISK_TERMS = {"self harm", "suicidal", "kill myself", "hurt myself"}


def keyword_severity_score(text: object) -> int:
    """Return a prototype severity score from 1 to 10 using keyword signals."""
    if not isinstance(text, str) or not text.strip():
        return 1

    normalized = re.sub(r"\s+", " ", text.lower())
    score = 3

    score += sum(1 for term in INTENSIFIERS if term in normalized)
    score += sum(1 for term in MEDICATION_TERMS if term in normalized)
    score += 3 * sum(1 for term in RISK_TERMS if term in normalized)
    score -= sum(1 for term in QUALIFIERS if term in normalized)

    return max(1, min(10, score))
