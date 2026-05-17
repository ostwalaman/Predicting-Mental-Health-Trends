"""Text preprocessing helpers for NeuroNexus.

These utilities intentionally operate on local data supplied by the user.
Raw Reddit data and credentials are not included in this repository.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd


DEFAULT_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "was",
    "were",
    "with",
}


def clean_text(text: object) -> str:
    """Normalize one text field for lightweight NLP experiments."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str, stopwords: set[str] | None = None) -> list[str]:
    """Split cleaned text and remove common stopwords."""
    stopwords = stopwords or DEFAULT_STOPWORDS
    return [token for token in text.split() if token not in stopwords and len(token) > 1]


def preprocess_dataframe(df: pd.DataFrame, text_column: str) -> pd.DataFrame:
    """Add cleaned text and token columns to a dataframe."""
    output = df.copy()
    output["clean_text"] = output[text_column].map(clean_text)
    output["tokens"] = output["clean_text"].map(tokenize)
    output["processed_text"] = output["tokens"].map(" ".join)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Preprocess a Reddit post CSV.")
    parser.add_argument("--input", required=True, help="Input CSV path.")
    parser.add_argument("--output", required=True, help="Output CSV path.")
    parser.add_argument("--text-column", default="Selftext", help="Column containing post text.")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    processed = preprocess_dataframe(df, args.text_column)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    processed.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
