# DBSCAN Clustering in Scikit-learn : Density-Based Spatial Clustering of Applications with Noise

# Key Parameters:
# eps          → Maximum distance between two samples for one to be considered in the neighborhood of the other
# min_samples  → Minimum number of samples in a neighborhood for a point to be considered a core point
# Noise Points → Outlier points assigned cluster label `-1`


# DBSCAN — Density-Based Clustering: Density-Based Spatial Clustering of Applications with Noise

# DBSCAN ke 2 main parameters
# 1. eps

# eps = ek point ke around kitna distance consider karna hai.
# eps small
# → chhota neighborhood

# eps large
# → bada neighborhood

# 2. min_samples

# Minimum kitne nearby points hone chahiye taaki area ko sufficiently dense maana ja sake.

# id="q2v8za"
# DBSCAN(
#     eps=0.5,
#     min_samples=5
# )


# DBSCAN ke point types:
# Core    → dense area ka main point - 0
# Border  → cluster ke edge par  -  1
# Noise   → isolated  -  -1

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# 1. Data
df = pd.DataFrame({
    "income": [20, 22, 25, 60, 65, 70, 120, 125, 130, 300],
    "spending": [15, 18, 20, 55, 60, 58, 100, 110, 105, 10]
})

# 2. Features
X = df[["income", "spending"]]

# 3. Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. DBSCAN
model = DBSCAN(
    eps=0.8,
    min_samples=3
)

# 5. Create clusters
labels = model.fit_predict(X_scaled)

# 6. Add result to DataFrame
df["cluster"] = labels

print(df)

# K-Distance Plot: Har point ke k-th nearest neighbor ki distance nikalo, distances ko sort karo, aur graph banao.
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from kneed import KneeLocator

df = pd.DataFrame({
    "income": [20, 22, 25, 60, 65, 70, 120, 125, 130, 300],
    "spending": [15, 18, 20, 55, 60, 58, 100, 110, 105, 10]
})

X = df[["income", "spending"]]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
min_samples = 3
neighbors = NearestNeighbors(
    n_neighbors=min_samples
)

neighbors.fit(X_scaled)

distances, indices = neighbors.kneighbors(X_scaled)

k_distances = distances[:, -1]

# Find knee automatically
x = range(len(k_distances))

knee = KneeLocator(
    x,
    k_distances,
    curve="convex",
    direction="increasing"
)

eps = k_distances[knee.knee]

print("Automatically selected eps:", eps)

k_distances = sorted(k_distances)

plt.plot(k_distances)

plt.xlabel("Points sorted by distance")
plt.ylabel("3rd Nearest Neighbor Distance")
plt.title("K-Distance Plot")

plt.show()

# DBSCAN
model = DBSCAN(
    eps=eps,
    min_samples=min_samples
)

labels = model.fit_predict(X_scaled)

df["cluster"] = labels

print(df)

# --------------------------------------------------------------------------

import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

df = pd.DataFrame({
    "income": [20, 22, 25, 60, 65, 70, 120, 125, 130, 300],  # 300 is an outlier
    "spending": [15, 18, 20, 55, 60, 58, 100, 110, 105, 300]
})

X = df[["income", "spending"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=2)
df["cluster"] = dbscan.fit_predict(X_scaled)

print("--- DBSCAN Clustering Results ---")
print(df)
print("\nIdentified Clusters:", set(df["cluster"]))
print("Noise Points Count (label -1):", (df["cluster"] == -1).sum())

