# Feature Selection: 
# Baaki unnecessary features:

# model ko complex bana sakte hain
# training slow kar sakte hain
# noise add kar sakte hain
# overfitting ka risk badha sakte hain
# interpretation difficult bana sakte hain

# FEATURE SELECTION
# │
# ├── 1️⃣ Filter Methods - statistics se feature select
# │   ├── Correlation ✅
# │   ├── Chi-Square ✅
# │   └── ANOVA ✅
# │
# ├── 2️⃣ Wrapper Methods - model ko baar-baar train karke feature select
# │   ├── RFE ⬅️ AB YE KARENGE
# │   ├── RFECV
# │   └── Sequential Feature Selection
# │
# └── 3️⃣ Embedded Methods
#     ├── Lasso
#     ├── Decision Tree
#     └── Random Forest

###### Correlation-based Feature Selection:
import pandas as pd

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300],
    "bedrooms": [1, 1, 2, 2, 3],
    "age": [10, 8, 7, 5, 3],
    "price": [25, 32, 40, 48, 60]
})

print(df.corr())

# area and price are highly correlated (0.9957474974017998)
# bedrooms and price are also correlated (0.979762)
# age and price are negatively correlated (-0.958797)
# area aur bedrooms khud strongly correlated hain => We can consider dropping one of the 
# features that are highly correlated with price,
# such as bedrooms, to reduce redundancy and simplify the model.

# Correlation Rule: 
# Feature ↔ Target
#         ↓
# relationship check

# Feature ↔ Feature
#         ↓
# redundancy check


# RFE (Wrapper) — Recursive Feature Elimination
# A B C D E
#     ↓
# Model train
#     ↓
# least important feature remove
#     ↓
# A B C D
#     ↓
# Model train
#     ↓
# least important feature remove
#     ↓
# A B C

from sklearn.datasets import load_diabetes
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

data = load_diabetes()

X = data.data
y = data.target

model = LinearRegression()

rfe = RFE(
    estimator=model,
    n_features_to_select=5
)

rfe.fit(X, y)

print("Selected:", rfe.support_)
print("Ranking:", rfe.ranking_)


# RFECV (Wrapper) — Recursive Feature Elimination with Cross-Validation
# Kitne features rakhne par model ka cross-validation performance best hai?
# RFECV = RFE + Cross-Validation

from sklearn.feature_selection import RFECV
from sklearn.model_selection import KFold


df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "distance": [15, 12, 10, 8, 7, 6, 4, 3],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})


X = df.drop("price", axis=1)
y = df["price"]


model = LinearRegression()
# Cross-validation strategy where n_splits=5 means the data will be split into 5 folds,
# shuffle=True means the data will be shuffled before splitting, and random_state=42 ensures reproducibility of the results.
cv = KFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

# RFECV will automatically determine the optimal number of features to select based on
# cross-validation performance.
rfecv = RFECV(
    estimator=model,
    cv=cv,
    scoring="r2"
)

rfecv.fit(X, y)
print("Optimal number of features:", rfecv.n_features_)
print("Selected features:", X.columns[rfecv.support_])
print("Feature ranking:", rfecv.ranking_)
print("CV results:", rfecv.cv_results_["mean_test_score"])


# Sequential Feature Selection (Wrapper) — Forward or Backward Selection
# Forward Selection: Start with no features and add one feature at a time based on model performance
# Backward Selection: Start with all features and remove one feature at a time based on model performance

from sklearn.feature_selection import SequentialFeatureSelector

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "distance": [15, 12, 10, 8, 7, 6, 4, 3],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

X = df.drop("price", axis=1)
y = df["price"]

model = LinearRegression()

cv = KFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

sfs = SequentialFeatureSelector(
    estimator=model,
    n_features_to_select=3,
    direction="forward",
    scoring="r2",
    cv=cv
)

sfs.fit(X, y)

print("Selected features:")
print(X.columns[sfs.get_support()])

# Lasso (Embedded) — L1 Regularization
# Lasso regression can be used for feature selection by shrinking the coefficients of less
# important features to zero, effectively removing them from the model.
# Lasso = L1 Regularization → coefficients can become exactly 0 → those features can be selected out.


from sklearn.linear_model import Lasso, LassoCV
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, cross_val_score


# =========================================================
# 1. DATASET
# =========================================================

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "random_noise": [99, 12, 45, 87, 23, 65, 34, 78],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})


X = df.drop("price", axis=1)
y = df["price"]


# =========================================================
# 2. FEATURE SCALING
# =========================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# =========================================================
# 3. CROSS-VALIDATION SETUP
# =========================================================

cv = KFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)


# =========================================================
# 4. TRY DIFFERENT ALPHA VALUES
# =========================================================

alphas = [0.001, 0.01, 0.1, 0.5, 1, 1.5, 2, 5, 10]

print("--- Alpha vs CV R² ---")

for alpha in alphas:

    lasso = Lasso(alpha=alpha)

    scores = cross_val_score(
        lasso,
        X_scaled,
        y,
        cv=cv,
        scoring="r2"
    )

    print(
        f"Alpha: {alpha:<5} "
        f"Mean CV R²: {scores.mean():.4f}"
    )


# =========================================================
# 5. AUTOMATICALLY FIND BEST ALPHA
# =========================================================

lasso_cv = LassoCV(
    alphas=alphas,
    cv=cv
)

lasso_cv.fit(X_scaled, y)

print("\n--- Best Alpha ---")
print("Best alpha:", lasso_cv.alpha_)


# =========================================================
# 6. FINAL LASSO MODEL
# =========================================================

lasso = Lasso(alpha=lasso_cv.alpha_)

lasso.fit(X_scaled, y)


# =========================================================
# 7. CHECK COEFFICIENTS
# =========================================================

coef_series = pd.Series(
    lasso.coef_,
    index=X.columns
)

print("\n--- Final Coefficients ---")
print(coef_series)


# =========================================================
# 8. SELECT NON-ZERO FEATURES
# =========================================================

selector = SelectFromModel(
    lasso,
    prefit=True
)

selected_features = X.columns[
    selector.get_support()
]

print("\n--- Selected Features ---")
print(selected_features.tolist())

# Decision Tree (Embedded) — Feature Importance
# Decision trees can be used to assess feature importance based on how much each feature
# contributes to reducing the impurity in the tree. Features that contribute more to reducing
# impurity are considered more important.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# =========================================================
# 1. DATASET
# =========================================================

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "random_noise": [99, 12, 45, 87, 23, 65, 34, 78],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

# =========================================================
# 2. FEATURES AND TARGET
# =========================================================

X = df.drop("price", axis=1)
y = df["price"]

# =========================================================
# 3. CREATE AND TRAIN DECISION TREE
# =========================================================

model = DecisionTreeRegressor(
    random_state=42
)

model.fit(X, y)

# =========================================================
# 4. FEATURE IMPORTANCE
# =========================================================

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

importance = importance.sort_values(
    ascending=False
)

print("--- Feature Importance ---")
print(importance)

# =========================================================
# 5. VISUALIZE FEATURE IMPORTANCE
# =========================================================

importance.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Decision Tree Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Random Forest (Embedded) — Feature Importance
# Random forests can also be used to assess feature importance based on how much each feature
# contributes to reducing the impurity across all trees in the forest. Features that contribute
# more to reducing impurity are considered more important.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor

# =========================================================
# 1. DATASET
# =========================================================

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "random_noise": [99, 12, 45, 87, 23, 65, 34, 78],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

# =========================================================
# 2. FEATURES AND TARGET
# =========================================================

X = df.drop("price", axis=1)
y = df["price"]

# =========================================================
# 3. CREATE RANDOM FOREST
# =========================================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# =========================================================
# 4. TRAIN MODEL
# =========================================================

model.fit(X, y)

# =========================================================
# 5. FEATURE IMPORTANCE
# =========================================================

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

importance = importance.sort_values(
    ascending=False
)

print("--- Random Forest Feature Importance ---")
print(importance)

# =========================================================
# 6. VISUALIZE
# =========================================================

importance.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()