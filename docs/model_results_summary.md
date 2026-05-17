# Model Results Summary

This file records the safe, aggregate model metrics used in the public README. It does not include raw Reddit text, author-like handles, or sensitive examples.

| Component | Method | Result | Notes |
|---|---|---:|---|
| Dataset | Reddit public posts | 22,273 merged tokenized rows | Recorded by the project pipeline workflow |
| Modeling sample | Cleaned Reddit posts | 11,803 rows | Used in the classification and severity-scoring workflow |
| Disorder discussion classification | Random Forest + TF-IDF | 0.72 weighted F1 | Accuracy recorded as 73.99% |
| Severity scoring | Random Forest regressor + keyword-derived signals | 93.18% pseudo-accuracy within +/-1 | Experimental and not clinically validated |

The repository should not claim 28K+ posts or 82% F1-score unless a future notebook, report, or reproducible run clearly proves those numbers.
