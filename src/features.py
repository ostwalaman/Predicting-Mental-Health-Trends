"""Feature extraction utilities for NeuroNexus models."""

from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer


def build_tfidf(max_features: int = 5000, ngram_range: tuple[int, int] = (1, 3)) -> TfidfVectorizer:
    """Create the TF-IDF vectorizer used in the notebook experiments."""
    return TfidfVectorizer(max_features=max_features, ngram_range=ngram_range)
