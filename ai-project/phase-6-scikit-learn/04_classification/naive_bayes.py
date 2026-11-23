# Naive Bayes Classifier in Scikit-learn : Probabilistic classification using Bayes Theorem

# Bayes Theorem: P(Y|X) = [P(X|Y) * P(Y)] / P(X)
# "Naive" Assumption: Features are independent of each other given the class label.

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

# -----------------------------------------------------------------------

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    "glucose": [85, 90, 140, 160, 180, 95, 110, 175],
    "bmi": [22.0, 24.5, 31.0, 33.5, 36.0, 21.5, 26.0, 34.0],
    "diabetic": [0, 0, 1, 1, 1, 0, 0, 1]
})

X = df[["glucose", "bmi"]]
y = df["diabetic"]

model = GaussianNB()
model.fit(X, y)

new_patient = [[150, 30.0]]
prediction = model.predict(new_patient)
probabilities = model.predict_proba(new_patient)

print("--- Gaussian Naive Bayes Classifier ---")
print("New Patient Prediction (0=No, 1=Diabetic):", prediction[0])
print(f"Probabilities: No={probabilities[0][0]:.2f}, Diabetic={probabilities[0][1]:.2f}")

