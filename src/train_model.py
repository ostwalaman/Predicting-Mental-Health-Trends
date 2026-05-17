"""Train a baseline Random Forest + TF-IDF classifier.

Example:
    python src/train_model.py --input clean_posts.csv --text-column Selftext --label-column Subreddit
"""

from __future__ import annotations

import argparse

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from features import build_tfidf
from preprocess import clean_text


def train_classifier(
    df: pd.DataFrame,
    text_column: str,
    label_column: str,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple[Pipeline, str]:
    """Train and evaluate a Random Forest classifier on cleaned text."""
    data = df[[text_column, label_column]].dropna().copy()
    data["clean_text"] = data[text_column].map(clean_text)

    x_train, x_test, y_train, y_test = train_test_split(
        data["clean_text"],
        data[label_column],
        test_size=test_size,
        random_state=random_state,
        stratify=data[label_column],
    )

    model = Pipeline(
        steps=[
            ("tfidf", build_tfidf()),
            ("classifier", RandomForestClassifier(n_estimators=200, random_state=random_state)),
        ]
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    report = classification_report(y_test, predictions)
    weighted_f1 = f1_score(y_test, predictions, average="weighted")
    accuracy = accuracy_score(y_test, predictions)
    summary = f"Weighted F1: {weighted_f1:.2f}\nAccuracy: {accuracy:.2%}\n\n{report}"
    return model, summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the NeuroNexus baseline classifier.")
    parser.add_argument("--input", required=True, help="Input CSV path.")
    parser.add_argument("--text-column", default="Selftext", help="Column containing post text.")
    parser.add_argument("--label-column", default="Subreddit", help="Target label column.")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    _, summary = train_classifier(df, args.text_column, args.label_column)
    print(summary)


if __name__ == "__main__":
    main()
