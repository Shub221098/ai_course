# End-to-End Scikit-learn ML Pipeline Project

# End-to-End Pipeline Steps:
# Raw Dataset
#     ↓
# Train/Test Split
#     ↓
# Preprocessing (ColumnTransformer: Imputer + Scaler + Encoder)
#     ↓
# Scikit-learn Pipeline
#     ↓
# Hyperparameter Tuning (GridSearchCV + Cross-Validation)
#     ↓
# Final Evaluation & Metrics

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

# 1. Raw Dataset Creation
data = pd.DataFrame({
    "age": [25, 45, 35, 50, 23, 40, 52, 28, 33, 48],
    "income": [30, 80, 60, 100, 25, 75, 110, 35, 50, 90],
    "city": ["Surat", "Mumbai", "Delhi", "Surat", "Mumbai", "Delhi", "Mumbai", "Surat", "Delhi", "Mumbai"],
    "bought_loan": [0, 1, 1, 1, 0, 1, 1, 0, 0, 1]
})

X = data[["age", "income", "city"]]
y = data["bought_loan"]

# 2. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. ColumnTransformer Preprocessing Pipelines
numeric_features = ["age", "income"]
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_features = ["city"]
categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(drop="first", handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# 4. Full Machine Learning Pipeline
full_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# 5. Hyperparameter Tuning with GridSearchCV
param_grid = {
    "classifier__n_estimators": [10, 50, 100],
    "classifier__max_depth": [2, 4, 6]
}

grid_search = GridSearchCV(full_pipeline, param_grid, cv=2, scoring="accuracy")
grid_search.fit(X_train, y_train)

# 6. Evaluation on Unseen Test Data
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("--- End-to-End Scikit-learn Pipeline Results ---")
print("Best Hyperparameters:", grid_search.best_params_)
print("\nTest Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nTest Classification Report:\n", classification_report(y_test, y_pred))

