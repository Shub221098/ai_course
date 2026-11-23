# Logistic Regression: Its name is regression but it is actually a classification algorithm. It is used to predict the probability of a categorical
# dependent variable. 
# In logistic regression, the dependent variable is binary (0 or 1, True or False, Yes or No). 
# The algorithm uses the logistic function to model the relationship between the independent variables and the probability of the dependent variable.
# Sigmoid function is used to map predicted values to probabilities. The output of the logistic regression model is a value between 0 and 1,
# which can be interpreted as the probability of the positive class (1) given the input features.
# Input → Sigmoid → Probability

# -∞    →    0
#  0    →   0.5
# +∞    →    1

import pandas as pd
from sklearn.linear_model import LogisticRegression

# OLD STUDENT DATA
#       ↓
# ┌───────────────────┐
# │ Hours   Passed    │
# │ 1       0         │
# │ 2       0         │
# │ 3       0         │
# │ 4       0         │
# │ 5       1         │
# │ 6       1         │
# │ 7       1         │
# │ 8       1         │
# └───────────────────┘
#       ↓
#    model.fit()
#       ↓
# MODEL LEARNS PATTERN
#       ↓
# NEW STUDENT
# Hours = 6
#       ↓
# ┌──────────────────────┐
# │ predict()             │
# │ → 1                   │
# │ → PASS                │
# │                      │
# │ predict_proba()       │
# │ → Fail = 14.7%        │
# │ → Pass = 85.3%        │
# └──────────────────────┘

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1]
})

X = df[["hours"]]
y = df["passed"]

model = LogisticRegression()

model.fit(X, y)

new_student = [[6]]

prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

print("Prediction:", prediction)
print("Probability:", probability)

# Confusion Matrix: Confusion matrix is a table that is used to evaluate the performance of a classification model.

# Confusion Matrix
#       ↓
#  ┌────┼────┐
#  ↓    ↓    ↓
# Accuracy  Precision
#           Recall
#              ↓
#             F1
#              ↓
#           ROC-AUC

# Agar 1 = Pass:

# TP → Pass ko Pass bola ✅ - True Postive
# FN → Pass ko Fail bola ❌ - False Negative

# TN → Fail ko Fail bola ✅ - True Negative
# FP → Fail ko Pass bola ❌ - False Positive

# So:

# True = prediction correct
# False = prediction wrong
# Positive/Negative = predicted class ka type

#                  PREDICTED
#                  0       1
#               ┌───────┬───────┐
# ACTUAL    0   │  TN=1 │  FP=1 │
#               ├───────┼───────┤
#           1   │  FN=1 │  TP=1 │
#  
#              └───────┴───────┘
from sklearn.metrics import confusion_matrix

actual = [1, 1, 0, 0]
predicted = [1, 0, 0, 1]

cm = confusion_matrix(actual, predicted)

print(cm)
# Output:
# [[1 1]
#  [1 1]]

# Accuracy: Total predictions mein se kitni predictions correct thi?
# Defination: A global performance metric that measures the percentage of total predictions the model got right, but can be dangerously misleading when classes are imbalanced.
# Accuracy = (TP + TN) / (TP + TN + FP + FN)

from sklearn.metrics import accuracy_score

actual = [1, 1, 0, 0]
predicted = [1, 0, 0, 1]

accuracy = accuracy_score(actual, predicted)

print("Accuracy:", accuracy)

# Precision: Model ne jitne cases ko Positive bola, unmein se actually kitne Positive the?
# Defination: Precision is a class-specific performance metric that measures the percentage of positive predictions the model got right, but can be misleading when classes are imbalanced.
# Precision = TP / (TP + FP)

from sklearn.metrics import precision_score
actual = [1, 1, 0, 0]
predicted = [1, 0, 0, 1]

precision = precision_score(actual, predicted)

print("Predicted:", precision)

# Recall: Actually jitne Positive cases the, model ne unmein se kitne correctly identify kiye?
# Defination: Recall is a class-specific performance metric that measures the percentage of actual positives the model got right, but can be misleading when classes are imbalanced.
# Recall = TP / (TP + FN)

from sklearn.metrics import recall_score

actual = [1, 1, 0, 0]
predicted = [1, 0, 0, 1]

recall = recall_score(actual, predicted)

print("Recall:", recall)

# F1 Score: Precision aur Recall ka harmonic mean hai. F1 Score tab useful hota hai jab class imbalance ho.
# Defination: F1 Score is a single balance metric that measures how well Precision and Recall perform together, strictly punishing the model if either one of them is low.
# F1 Score = 2 * (Precision * Recall) / (Precision + Recall)

from sklearn.metrics import f1_score

actual = [1, 1, 0, 0]
predicted = [1, 0, 0, 1]

f1 = f1_score(actual, predicted)

print("F1 Score:", f1)

# Accuracy → Overall correct?
# Precision → Positive bola, kitna sahi?
# Recall → Actual Positive mein se kitne pakde?
# F1 → Precision + Recall ka balance.


# Balanced Dataset (class balance) -> Accuracy
# Unbalanced Dataset (class imbalance) -> Precision, Recall, F1 Score

# ROC-AUC: Receiver Operating Characteristic - Area Under Curve. It is a performance measurement for classification problem at various threshold settings.
# ROC is a probability curve and AUC represents degree or measure of separability. It tells how much the model is capable of distinguishing between classes.
# AUC roughly batata hai ki model Positive aur Negative cases ko kitna achhe se distinguish/rank kar raha hai.

# AUC ≈ 1.0 → Excellent
# AUC ≈ 0.9 → Very good
# AUC ≈ 0.7 → Reasonable
# AUC ≈ 0.5 → Random guessing
# AUC < 0.5 → Worse than random / ranking reversed

# ROC = different thresholds check karo
# AUC = overall separation ability

from sklearn.metrics import roc_auc_score

actual = [0, 0, 1, 1, 1]

probability = [0.1, 0.2, 0.7, 0.8, 0.9]

auc = roc_auc_score(actual, probability)

print("ROC-AUC:", auc)

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


# Naive Bayes: Naive Bayes is a probabilistic machine learning algorithm based on Bayes' theorem, which assumes that the features are conditionally
# independent given the class label.
# Naive Bayes = Probability ke basis par classification.

# For example:
# "Win free money"

# Model Checks
# P(Spam | words)
# P(Not Spam | words)

# if
# P(Spam | words) = 0.92
# P(Not Spam | words) = 0.08

# output = Spam

import pandas as pd
from sklearn.naive_bayes import GaussianNB

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed":      [0, 0, 0, 0, 1, 1, 1, 1]
})

X = df[["study_hours"]]
y = df["passed"]

model = GaussianNB()

model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction:", prediction)

probability = model.predict_proba([[6]])

print(probability) # [[0.00816257 0.99183743]]

# Naive Bayes ke different variants bhi hote hain:

# Variant	Use
# GaussianNB	Numerical data
# MultinomialNB	Text/count data
# BernoulliNB	Binary features

# Variant	                            Input/Data Format	                                Quick Test Question & Examples                              Use Case
# GaussianNB	                    Floats / Continuous	                        "Kya value points/decimals me ho sakti hai?"                     Numerical data
#                                                                         👉 Examples: \(3.14\), \(72.5\), height, temperature
# MultinomialNB	                     Integers / Counts	                        "Kya ye kisi cheez ki ginti (repetition) hai?"                   Text/count data
#                                                                         👉 Examples: \(0, 1, 2, 15\), word counts in a document
# BernoulliNB	                        Binary flags	                        "Kya ye sirf Yes/No ya Present/Absent hai?"                      Binary features
#                                                                         👉 Examples: \(0 \text{ or } 1\), True/False, feature exists or not

# Naive Bayes kab use kare?

# Especially useful:

# 📧 Spam detection
# 📝 Text classification
# 📰 News classification
# 💬 Sentiment classification
# Fast baseline models

# Toh actual difference kya hai?
#                           Logistic Regression	                    Naive Bayes
# predict()	            Final class	                            Final class
# predict_proba()	    Class probability	                    Class probability
# Probability kaise?	Sigmoid / model coefficients	        Bayes theorem + feature likelihoods

# Main idea	Decision boundary	Probability