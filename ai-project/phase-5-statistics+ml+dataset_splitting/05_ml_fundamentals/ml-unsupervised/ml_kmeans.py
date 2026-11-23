from sklearn.cluster import KMeans
import pandas as pd

# Sirf features, koi target 'y' nahi hai!
data = pd.DataFrame({
    'income': [15, 16, 17, 80, 85, 90],
    'spending': [80, 85, 82, 15, 20, 18]
})

# K=2 groups banane hain
kmeans = KMeans(n_clusters=2, random_state=42)
data['cluster'] = kmeans.fit_predict(data)

print(data)

# 
import pandas as pd
from sklearn.cluster import KMeans

df = pd.DataFrame({
    "income": [20, 22, 25, 60, 65, 70, 120, 125, 130],
    "spending": [15, 18, 20, 55, 60, 58, 100, 110, 105]
})

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

X = df[["income", "spending"]]

model.fit(X)

df["cluster"] = model.labels_

print(df)

# Centroid - har clusten ka centre point

print(model.cluster_centers_)

# As K-Means distance-basee algorithm h, Agar features ka scale bahut different ho:

# income     → 20,000 - 2,00,000
# spending   → 1 - 100

# toh income distance ko dominate kar sakti hai.

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X_scaled)

# n_init = 1
#    ↓
# 1 baar K-Means run
#    ↓
# Result

# n_init = 10
#    ↓
# 10 different starting points
#    ↓
# 10 K-Means runs
#    ↓
# Best result choose


# K-Means ka sabse popular interview sawal yahi hota hai: "Hume kaise pata chalega ki $K$ (clusters ki ginti) kitni rakhni hai?"
# Isko nikaalne ke liye hum use karte hain Elbow Method (Kohni ka tarika)

# In K-Means, we find the optimal number of clusters using the Elbow Method.
# We plot WCSS (Inertia) against different values of K. The point where the rate of decrease sharply slows down—forming an 'elbow' bend—is selected
# as the optimal K."

# WCSS (Error)
#   |  
#   |\
#   | \
#   |  \
#   |   \ <-- Yahan tak bohot fast gira
#   |    \__________ <-- (ELBOW POINT!) Yahan se curve flat ho gaya
#   |               \______
#   +-------------------------> K (Clusters)
#        1   2   3   4   5

# Scikit-learn me model ka error kmeans.inertia_ ke andar store hota hai:
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1 se 10 clusters test karenge
wcss = []
k_range = range(1, 6)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data)  # Aapka dataset
    wcss.append(kmeans.inertia_)  # Error list me add kar li

# Graph plot karna
plt.plot(k_range, wcss, marker="o")
plt.title("The Elbow Method")
plt.xlabel("Number of clusters (K)")
plt.ylabel("WCSS (Inertia)")
plt.show()

# ⚠️ Ek important baat: Elbow koi guaranteed mathematical answer nahi hai. Kabhi elbow clear nahi hota. Aise cases mein Silhouette Score bhi use karte hain.
# Silhouette Score: Chosen K ke clusters kitne well-separated aur internally compact hain.
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

for k in range(2, 7):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    print("K =", k, "Silhouette Score =", score)

#       Elbow	                                           Silhouette
# Inertia dekhta hai	                            Cluster quality dekhta hai
# Lower inertia better	                            Higher score better
# Elbow/bend find karte hain	                    Highest score look karte hain
# K choose karne mein help	                        K choose karne mein help