# K-Nearest Neighbors (KNN) in Scikit-learn : Distance-based classification algorithm

# KNN Principle:
# Classify query point based on majority vote of K nearest neighbors in feature space
# ⚠️ Scaling is mandatory for distance-based algorithms!


# KNN (k nearest neighbor): KNN new data point ke nearest K data points ko dekhta hai aur unke basis par prediction karta hai

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3) # currently choosing manually neighbors, but can be optimized using cross-validation

model.fit(X, y)

prediction = model.predict([[5]])

print("Prediction:", prediction)

# KNN ka main advantage ye hai ki ye simple aur intuitive hota hai, aur non-linear decision boundaries ko bhi handle kar sakta hai.
# KNN ka main disadvantage ye hai ki ye computationally expensive hota hai, especially jab dataset bahut bada ho, aur ye sensitive hota hai irrelevant features aur feature scaling ke liye.

# n_neighbors (hyperparameter): Number of neighbors to use for prediction. A small value of K can lead to overfitting, while a large value can lead
# to underfitting.
# how to choose K: Use cross-validation to find the optimal value of K that gives the best performance on the validation set.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

for k in [1, 3, 5]:

    model = KNeighborsClassifier(n_neighbors=k)

    scores = cross_val_score(
        model,
        X,
        y,
        cv=3,
        scoring="accuracy"
    )

    print(
        "K =", k,
        "CV Accuracy =", scores.mean()
    )

# Scaling in KNN: KNN distance-based algorithm hai, isliye feature scaling important hai. Agar features different scales pe hain,
# to unka distance calculation biased ho sakta hai.
# Attendance ka number bht bada h to scaling krna pdega
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

for k in [1, 3, 5]:

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=k))
    ])

    scores = cross_val_score(
        pipeline,
        X,
        y,
        cv=3,
        scoring="accuracy"
    )

    print(
        "K =", k,
        "CV Accuracy =", scores.mean()
    )

# Raw Data
#    ↓
# Train/Test Split
#    ↓
# Pipeline
#    ├── StandardScaler
#    └── KNN
#    ↓
# Cross-Validation
#    ↓
# Different K values
#    ↓
# Best K
#    ↓
# Final Model
#    ↓
# Test Set Evaluation
#    ↓
# Prediction


# ---------------------------------------------------------------------------

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

df = pd.DataFrame({
    "income": [20, 22, 25, 60, 65, 70, 120, 125, 130],
    "spending": [15, 18, 20, 55, 60, 58, 100, 110, 105],
    "tier": [0, 0, 0, 1, 1, 1, 2, 2, 2]  # Target class
})

X = df[["income", "spending"]]
y = df["tier"]

# KNN Pipeline with Scaling
knn_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=3))
])

knn_pipeline.fit(X, y)

new_customer = [[68, 57]]
pred_tier = knn_pipeline.predict(new_customer)
print("--- K-Nearest Neighbors (K=3) ---")
print("Predicted Customer Tier:", pred_tier[0])

# Finding Optimal K using Cross-Validation
print("\n--- Cross-Validation for Optimal K ---")
for k in [1, 3, 5]:
    cv_pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=k))
    ])
    scores = cross_val_score(cv_pipeline, X, y, cv=3)
    print(f"K = {k} | Mean Accuracy: {scores.mean():.2f}")

