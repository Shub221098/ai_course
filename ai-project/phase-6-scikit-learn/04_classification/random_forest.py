# Random Forest Classifier & Regressor in Scikit-learn : Ensemble Bagging

# Bagging (Bootstrap Aggregating):
# Multiple Decision Trees built on random data subsets + random feature sub-samples.
# Final Prediction = Majority Vote (Classification) or Average (Regression).

# Random Forest: Random forest is an ensemble learning method that combines multiple decision trees to improve the accuracy and robustness of predictions. 
# It works by creating a "forest" of decision trees, each trained on a random subset of the data and features, and then aggregating their predictions
# to make a final decision. 
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction:", prediction)

# feature_importances_: Feature importance is a technique used to assign a score to input features based on how useful they are at predicting a target variable.
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", score)

# -----------------------------------------------------------------------------

import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "high_price": [0, 0, 0, 0, 1, 1, 1, 1]  # Target for Classification
})

X = df[["area", "bedrooms", "bathrooms"]]
y_class = df["high_price"]

# 1. RandomForestClassifier
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
rf_clf.fit(X, y_class)

print("--- Random Forest Classifier ---")
print("Feature Importances:")
for feature, importance in zip(X.columns, rf_clf.feature_importances_):
    print(f" {feature}: {importance:.4f}")

# 2. RandomForestRegressor
y_reg = [25, 30, 42, 48, 58, 65, 78, 90]
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X, y_reg)

print("\n--- Random Forest Regressor ---")
new_house = [[1200, 3, 2]]
print(f"Predicted Continuous Price for {new_house}: {rf_reg.predict(new_house)[0]:.2f}")

