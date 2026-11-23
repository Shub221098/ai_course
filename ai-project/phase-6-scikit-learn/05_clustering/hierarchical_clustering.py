# Hierarchical Clustering: Data points ko gradually merge karke clusters ki hierarchy banate hain.
# Dendrogram: Kaunse points/clusters kis stage par merge hue.


#                           Hierarchical Clustering 
#                                     |
# ========================================================================
#      AGGLOMERATIVE (Bottom-Up)             DIVISIVE (Top-Down)
#    (Niche se Upar: Jodna / Merge)        (Upar se Niche: Todna / Split)
# ========================================================================

#           [ A B C D E ]                        [ A B C D E ]
#          (1 Big Cluster)                      (1 Big Cluster)
#              ▲     ▲                               │     │
#              │     │                               ▼     ▼
#          [ A B ]  [ C D E ]                   [ A B ]  [ C D E ]
#             ▲        ▲    ▲                      │        │    │
#             │        │    │                      ▼        ▼    ▼
#          [ A B ]   [ C ] [ D E ]              [ A B ]   [ C ] [ D E ]
#           ▲   ▲           ▲   ▲                │   │           │   │
#           │   │           │   │                ▼   ▼           ▼   ▼
#         [A]  [B]   [C]   [D]  [E]            [A]  [B]   [C]   [D]  [E]
#      (5 Individual Points/Clusters)        (5 Individual Points/Clusters)

#   Direction: NICHE SE UPAR (Merge)       Direction: UPAR SE NICHE (Split)

# Practically Agglomerative hierarchical clustering jyada use hoti h.

# Kaunse 2 clusters ko merge karein? => Linkage
# Linkage method decide karta hai ki cluster-to-cluster distance kaise calculate hogi.

# Linkage	                        Main idea
# Single	                    Minimum distance
# Complete	                    Maximum distance
# Average	                    Average distance
# Ward	                Minimum increase in within-cluster variance

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.DataFrame({
    "income": [20, 22, 25, 60, 65, 70, 120, 125, 130],
    "spending": [15, 18, 20, 55, 60, 58, 100, 110, 105]
})

X = df[["income", "spending"]]
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)
labels = model.fit_predict(X_scaled)
# ⚠️ Ward ki ek important restriction hai: sklearn mein Ward linkage Euclidean distance ke saath hi use hota hai.


# Hierarchical Clustering
#         ↓
# Kaunse clusters merge karein?
#         ↓
# Linkage
#         ↓
# Distance kaise calculate karni hai?
#         ↓
# Merge
#         ↓
# Dendrogram

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# -------------------------------------------------------------
# STEP 1: Data Setup (Hierarchical Clustering Input)
# 5 alag-alag points (Annual Income vs Spending Score)
# -------------------------------------------------------------
X = np.array([
    [15, 39],  # Point A (Low income, low spending)
    [16, 42],  # Point B (A ke bohot kareeb)
    [25, 45],  # Point C
    [85, 80],  # Point D (High income, high spending)
    [90, 82]   # Point E (D ke bohot kareeb)
])
labels = ["A", "B", "C", "D", "E"]

# -------------------------------------------------------------
# STEP 2 & 3: Distance Metric & Linkage Method
# - Metric: 'euclidean' (Points ke beech seedhi line ki doori)
# - Linkage: 'ward' (Clusters ke beech minimum variance dekhna)
# -------------------------------------------------------------
# linkage() function internally:
# 1. Distance matrix banata hai (Euclidean)
# 2. Linkage criteria laga kar decide karta hai kaun pehle merge hoga
# 3. Chote clusters ko bade clusters me merge karta jata hai
mergings = linkage(X, method="ward", metric="euclidean")
print("mergings====>", mergings)

# -------------------------------------------------------------
# STEP 4: Dendrogram (Visual Tree)
# Yahan dekh kar hum decide karenge ki 'Kainchi' kahan chalani hai
# -------------------------------------------------------------
plt.figure(figsize=(7, 4))
dendrogram(
    mergings,
    labels=labels,
    leaf_rotation=0,
    leaf_font_size=12
)
plt.title("Step 4: Dendrogram Tree")
plt.xlabel("Data Points")
plt.ylabel("Cluster Distance (Height)")

# Ek red line draw karte hain cut point dikhane ke liye (e.g., threshold = 40)
plt.axhline(y=40, color="r", linestyle="--", label="Cut Threshold (K=2)")
plt.legend()
plt.show()

# -------------------------------------------------------------
# STEP 5: Final Merge & Cluster Assignment (Sklearn)
# Dendrogram se pata chala ki 2 clusters natural hain:
# - Cluster 0: [A, B, C]
# - Cluster 1: [D, E]
# -------------------------------------------------------------
model = AgglomerativeClustering(
    n_clusters=2,           # Final kitne tukde chahiye
    metric="euclidean",     # Distance calculation formula
    linkage="ward"          # Merge rule
)

cluster_labels = model.fit_predict(X)

# Final Result Table
df = pd.DataFrame(X, columns=["Income", "Spending"], index=labels)
df["Assigned_Cluster"] = cluster_labels
print(df)


# -------------------------------------------------------------------------

# Hierarchical Clustering in Scikit-learn : Agglomerative (Bottom-Up) Clustering

# Linkage Criteria:
# ward     → Minimizes total variance within clusters (Requires Euclidean distance)
# complete → Maximum distance between any two points in clusters
# average  → Average distance between all pairs of points

import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "income": [20, 22, 25, 60, 65, 70, 120, 125, 130],
    "spending": [15, 18, 20, 55, 60, 58, 100, 110, 105]
})

X = df[["income", "spending"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Agglomerative Clustering (n_clusters=3, linkage='ward')
agg_clustering = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="ward")
df["cluster"] = agg_clustering.fit_predict(X_scaled)

print("--- Hierarchical (Agglomerative) Clustering ---")
print(df)

