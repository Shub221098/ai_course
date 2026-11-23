# Principal Component Analysis (PCA) in Scikit-learn : Dimensionality Reduction

# Key Concepts:
# Reduces feature dimension while preserving maximum dataset variance.
# n_components           → Number of principal components to keep (or ratio e.g. 0.95 for 95% variance)
# explained_variance_ratio_ → Percentage of variance explained by each principal component
# ⚠️ Scaling is mandatory before running PCA!

# PCA (Principal Component Analysis): PCA dimensionality reduce karta hai while preserving
# as much important information as possible.

# In Simple words: PCA bahut saare features ko kuch naye important features/components mein convert karta hai.

# PCA Most Important Concept:
# Principal Component = data ki ek new direction jo maximum useful variation/information capture karti hai.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = np.array([
    [90, 92],
    [80, 82],
    [70, 71],
    [60, 62],
    [50, 52]
])

print(data.shape)

plt.scatter(data[:, 0], data[:, 1])

plt.xlabel("Math")
plt.ylabel("Science")
plt.title("Math vs Science")

plt.show()

pca = PCA(n_components=1)
reduced_data = pca.fit_transform(data)

# fit()

# PCA data se learn karta hai:

# data ka variance
# important direction
# principal component
# transform()

# Data ko us new component/direction mein convert karta hai.

print("Original shape:", data.shape)
print("Reduced shape:", reduced_data.shape)
print("Reduced data:",reduced_data)

# "PC1 ne original data ki kitni information capture ki
print(pca.explained_variance_ratio_)

# PCA se pehle Scaling kyun?
# PCA variance use krta h, hum directly PCA lagayenge, toh large-scale feature PCA ko 
# disproportionately influence kar sakta hai.

# Age       Salary
# 25        50000
# 30        80000
# 35        120000
# 40        150000

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# data = np.array([
#     [25, 50000],
#     [30, 80000],
#     [35, 120000],
#     [40, 150000]
# ])


data = np.array([
    [5, 3, 2, 1],
    [6, 4, 3, 2],
    [7, 5, 4, 3],
    [8, 6, 5, 4],
    [2, 1, 1, 0],
    [3, 2, 1, 1],
    [9, 8, 7, 6],
    [10, 9, 8, 7]
])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("Original:")
print(data)

print("\nScaled:")
print(scaled_data)

pca = PCA(n_components=1)

reduced_data = pca.fit_transform(scaled_data)

print("Reduced Data:")
print(reduced_data)

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Using pipeline
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=0.95)) # here we are saying 1 component preserver karo, if
    # n_components=0.95 means 95% variance preserve karo
])
reduced_data = pipeline.fit_transform(data)

print("Original Shape:")
print(data.shape)

print("\nReduced Shape:")
print(reduced_data.shape)

print("\nReduced Data:")
print(reduced_data)

print("\nExplained Variance Ratio:")
print(pipeline.named_steps["pca"].explained_variance_ratio_)

# -----------------------------------------------------------------------------

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.DataFrame({
    "f1": [10, 20, 30, 40, 50],
    "f2": [15, 25, 35, 45, 55],
    "f3": [100, 200, 300, 400, 500],
    "f4": [1, 2, 3, 4, 5]
})

X = df[["f1", "f2", "f3", "f4"]]

# PCA Pipeline (StandardScaler + PCA)
pca_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=2))
])

X_pca = pca_pipeline.fit_transform(X)

pca_step = pca_pipeline.named_steps["pca"]

print("--- Principal Component Analysis (4D -> 2D) ---")
print("Transformed Shape:", X_pca.shape)
print("Explained Variance Ratio per component:", pca_step.explained_variance_ratio_)
print(f"Total Preserved Variance: {pca_step.explained_variance_ratio_.sum()*100:.2f}%")

