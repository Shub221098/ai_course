# Hyperparameter Tuning in Scikit-learn : GridSearchCV and RandomizedSearchCV

# Hyperparameter Tuning: Finding optimal parameters before training (e.g. C, alpha, max_depth)
# GridSearchCV         → Tries all possible grid parameter combinations
# RandomizedSearchCV   → Randomly samples fixed iterations from hyperparameter distributions


# Hyperparameter Tuning & GridSearchCV

# Hyperparameter Tuning: Hyperparameters wo parameters hote hain jo model training se pehle set kiye jaate hain jaise alpha

# Problem: manually bahut saare combinations try karne pad sakte hain.
# GridSearchCV automatically combinations try karta hai + Cross-Validation use karta hai.

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

model = Ridge()

param_grid = {
    "alpha": [0.01, 0.1, 1, 10, 100]
}

grid = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="r2"
)

grid.fit(X, y)

print("Best Alpha:", grid.best_params_)
print("Best CV Score:", grid.best_score_)


# Final code
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge())
])

param_grid = {
    "model__alpha": [0.01, 0.1, 1, 10, 100]
}

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="r2"
)

grid.fit(X_train, y_train)

# ------------------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.DataFrame({
    "f1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "f2": [10, 20, 15, 25, 30, 35, 40, 45, 50, 55],
    "target": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})

X = df[["f1", "f2"]]
y = df["target"]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("rf", RandomForestClassifier(random_state=42))
])

# 1. GridSearchCV Example
param_grid = {
    "rf__n_estimators": [10, 50, 100],
    "rf__max_depth": [2, 4, 6]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring="accuracy")
grid_search.fit(X, y)

print("--- GridSearchCV Results ---")
print("Best Parameters:", grid_search.best_params_)
print(f"Best CV Accuracy: {grid_search.best_score_:.4f}")

# 2. RandomizedSearchCV Example
param_distributions = {
    "rf__n_estimators": [10, 25, 50, 75, 100, 150, 200],
    "rf__max_depth": [2, 3, 4, 5, 6, 8, 10]
}

random_search = RandomizedSearchCV(
    pipeline, param_distributions, n_iter=5, cv=3, scoring="accuracy", random_state=42
)
random_search.fit(X, y)

print("\n--- RandomizedSearchCV Results ---")
print("Best Parameters:", random_search.best_params_)
print(f"Best CV Accuracy: {random_search.best_score_:.4f}")

