# Decision Tree Classifier in Scikit-learn : Non-parametric tree-based classification

# Splitting Criteria: Gini Impurity or Entropy
# Gini Impurity = 1 - Σ (p_i)^2

# Decision Tree: Decision tree is a supervised learning algorithm that can be used for both classification and regression tasks. It works by splitting the data
# into subsets based on the value of input features, creating a tree-like model of decisions.
# Decision Tree questions pooch-pooch kar final decision leta hai
# Decision tree ke andar nodes hote hain jahan pe data split hota hai aur leaves hote hain jahan pe final prediction hoti hai.
# Decision tree ka main advantage ye hai ki ye easily interpretable hota hai aur visualize kiya ja sakta hai.
# Decision tree ka main disadvantage ye hai ki ye overfitting kar sakta hai, especially jab tree bahut deep ho.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1]
})

X = df[["hours"]]
y = df["passed"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction:", prediction)


# max_depth (hyperparameter):  = Maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split
# samples.
# Too Simple
#     ↓
# Underfitting

# Good Depth
#     ↓
# Good Generalization

# Too Deep
#     ↓
# Overfitting

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction:", prediction)

# --------------------------------------------------------------

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

df = pd.DataFrame({
    "age": [25, 45, 35, 50, 23, 40],
    "income": [30, 80, 60, 100, 25, 75],
    "bought_loan": [0, 1, 1, 1, 0, 1]
})

X = df[["age", "income"]]
y = df["bought_loan"]

# Decision Tree with hyperparameter controls (max_depth, min_samples_split)
tree = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=2,
    random_state=42
)

tree.fit(X, y)

print("--- Decision Tree Text Representation ---")
tree_rules = export_text(tree, feature_names=list(X.columns))
print(tree_rules)

new_applicant = [[30, 70]]
print("Prediction for new applicant:", tree.predict(new_applicant)[0])

