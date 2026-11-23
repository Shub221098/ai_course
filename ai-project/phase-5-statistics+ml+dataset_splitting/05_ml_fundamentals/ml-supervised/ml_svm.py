# SVM — Support Vector Machine: SVM is a supervised machine learning algorithm that can be used for both classification and regression tasks. It works
# by finding the hyperplane that best separates the data into different classes.
# SVM ka main idea ye hai ki ye data points ke beech mein maximum margin hyperplane find karta hai, jisse ki classes ko best separate kiya ja sake.
# SVM ke andar support vectors hote hain, jo ki wo data points hote hain jo hyperplane ke closest hote hain aur decision boundary ko define karte hain.
# SVM ke andar different kernels hote hain, jo ki data ko higher dimensional space mein map karte hain, jisse ki non-linear decision boundaries ko bhi handle
# kiya ja sake.
# SVM ka main advantage ye hai ki ye high dimensional data ke liye effective hota hai aur overfitting ka risk kam hota hai.
# SVM ka main disadvantage ye hai ki ye computationally expensive hota hai, especially jab dataset bahut bada ho, aur ye sensitive hota hai feature scaling ke liye. 

# SVM = Best boundary + Maximum margin

# Margin: Boundary se nearest points ka distance maximum ho.

# 🟢 🟢     ← margin →    |    ← margin →    🔴 🔴
#                         ↑
#                    Boundary

# Support Vectors: Boundary ke sabse close important data points ko.

# 🟢 🟢  ⭐      |      ⭐  🔴 🔴
#                ↑
#            Boundary
# ⭐ = Support Vectors


import pandas as pd
from sklearn.svm import SVC

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1]
})

X = df[["hours"]]
y = df["passed"]

model = SVC(kernel="linear")

model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction:", prediction)

# SVM distance/margin based hai, isliye feature scales matter karte hain.

# Multiple features ho:

# area       → 500–5000
# bedrooms   → 1–5
# age        → 1–50

# Toh scaling generally important hai.

# Best practice:

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

model = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC(kernel="linear"))
])

model.fit(X, y)

# SVM
#  ↓
# Decision Boundary
#  ↓
# Maximum Margin
#  ↓
# Nearest points
#  ↓
# Support Vectors

# C Parameter: Model wrong classification ko kitna strongly punish kare?

# C small
# ↓
# Errors allowed
# ↓
# Wide margin

# C large
# ↓
# Errors punished
# ↓
# Tight margin

# Best C usually Cross-Validation se choose karte hain:
# C = [0.01, 0.1, 1, 10, 100]
#           ↓
#      Cross Validation
#           ↓
#       Best C
#           ↓
#       Final SVM

from sklearn.svm import SVC

for c in [0.1, 1, 10, 100]:

    model = SVC(
        kernel="linear",
        C=c
    )

    model.fit(X, y)

    print("C =", c)
    print("Prediction:", model.predict([[5]]))

# Kernal: Data ko ek higher-dimensional space mein represent karo, jahan classes easier to separate ho sakein.
# Non-linear problem ko SVM ke liye effectively separable banana.

# Linear data
# 🟢 🟢 🟢  |  🔴 🔴 🔴
# 🟢 🟢 🟢  |  🔴 🔴 🔴
#              ↑
#         straight boundary

# Problem 😵
# Suppose data aisa hai:

#         🟢
#      🔴 🔴 🔴
#    🔴   🟢   🔴
#      🔴 🔴 🔴
#         🟢

# Kernel	            Boundary	                Typical use
# linear	        Straight	                Linear data (SVC(kernel="linear"))
# poly	            Polynomial/curved	        Polynomial patterns (SVC(kernel="poly"))
# rbf ⭐	           Flexible curved	           Complex non-linear data (SVC(kernel="rbf"))
# sigmoid	        Sigmoid-like	            Less common (SVC(kernel="sigmoid"))

# SVC(
#     kernel="rbf",
#     C=10,
#     gamma="scale"
# )

# Gamma = ek individual training point ka influence kitna door tak hai.

# Low gamma
# → wider influence
# → smoother boundary

# High gamma
# → very local influence
# → complex boundary
# → overfitting risk

# Kernel decides "boundary kaisi ho sakti hai", C decides "boundary kitni strict ho", aur gamma decides "ek point ka influence kitna local ho."