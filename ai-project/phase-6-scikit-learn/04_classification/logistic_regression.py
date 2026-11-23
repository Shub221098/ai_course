# Logistic Regression: Its name is regression but it is actually a classification algorithm. It is used to predict the probability of a categorical
# dependent variable. 
# In logistic regression, the dependent variable is binary (0 or 1, True or False, Yes or No). 
# The algorithm uses the logistic function to model the relationship between the independent variables and the probability of the dependent variable.
# Sigmoid function is used to map predicted values to probabilities. The output of the logistic regression model is a value between 0 and 1,
# which can be interpreted as the probability of the positive class (1) given the input features.
# Input -> Sigmoid -> Probability -> Class Label (0 or 1)

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


# ----------------------------------------------------------------------------


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

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
probabilities = model.predict_proba(new_student)

print("--- Logistic Regression ---")
print("New Student (Hours=6) Prediction:", "Pass (1)" if prediction[0] == 1 else "Fail (0)")
print("Fail Probability:", f"{probabilities[0][0]*100:.1f}%")
print("Pass Probability:", f"{probabilities[0][1]*100:.1f}%")

