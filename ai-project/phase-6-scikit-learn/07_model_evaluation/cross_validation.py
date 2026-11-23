# Cross Validation in Scikit-learn : K-Fold and Stratified K-Fold Cross Validation

# Cross Validation Architecture
# 
#  Full Dataset
#      │
#  K-Fold Split (e.g. K=5)
#      │
#  ┌───┴───┬───────┬───────┬───────┬───────┐
#  │ Fold1 │ Fold2 │ Fold3 │ Fold4 │ Fold5 │
#  └───┬───┴───────┴───────┴───────┴───────┘
#      ▼
#  Iterative Evaluation across K folds -> Mean Score & Std

import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "passed": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})

X = df[["hours"]]
y = df["passed"]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

# 1. K-Fold Cross Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
kfold_scores = cross_val_score(pipeline, X, y, cv=kf, scoring="accuracy")

print("--- K-Fold Cross Validation ---")
print("Scores per fold:", kfold_scores)
print(f"Mean Accuracy: {kfold_scores.mean():.4f} (+/- {kfold_scores.std():.4f})")

# 2. Stratified K-Fold Cross Validation (Preserves Class Ratio in Imbalanced Datasets)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
stratified_scores = cross_val_score(pipeline, X, y, cv=skf, scoring="accuracy")

print("\n--- Stratified K-Fold Cross Validation ---")
print("Scores per fold:", stratified_scores)
print(f"Mean Accuracy: {stratified_scores.mean():.4f}")

