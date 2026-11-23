import matplotlib.pyplot as plt

# --- 1. डेटा तैयार करना ---
area = [800, 1200, 1500, 1800, 2200, 2500, 3000, 3500]  # X-Axis: घर का साइज (sqft)
price = [30, 45, 55, 60, 80, 85, 110, 130]             # Y-Axis: कीमत (लाख ₹)

# --- 2. कैनवास सेटअप ---
fig, ax = plt.subplots(figsize=(8, 5))

# --- 3. स्कैटर प्लॉट बनाना (plt.scatter) ---
ax.scatter(
    area,                   # X-axis का डेटा
    price,                  # Y-axis का डेटा
    s=150,                  # Size: डॉट्स का आकार (बड़ा करने के लिए 150 किया)
    c="crimson",            # Color: डॉट्स का गहरा लाल रंग
    edgecolor="black",      # डॉट्स के चारों तरफ काली बॉर्डर
    linewidth=1.2,          # बॉर्डर लाइन की मोटाई
    alpha=0.8,              # Alpha: 80% विजिबिलिटी। अगर डॉट्स एक-दूसरे के ऊपर आ जाएं, तो धुंधलेपन की वजह से आर-पार दिख जाता है
    marker="o"              # डॉट्स का शेप (o = गोल, आप '^' से ट्रायंगल या 's' से स्क्वायर भी बना सकते हैं)
)

# --- 4. सजावट और नामकरण ---
ax.set_title("House Area vs Price Discovery", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Property Area (sqft)", fontsize=11, labelpad=10)
ax.set_ylabel("Property Price (Lakhs ₹)", fontsize=11, labelpad=10)

# --- 5. ग्रिड और फिनिशिंग ---
ax.grid(True, linestyle=':', alpha=0.4)      # हल्की बैकग्राउंड ग्रिड
ax.spines['top'].set_visible(False)          # ऊपर की बॉर्डर गायब
ax.spines['right'].set_visible(False)        # दाईं बॉर्डर गायब

# --- 6. डिस्प्ले करना ---
plt.tight_layout()
plt.show()