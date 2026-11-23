import matplotlib.pyplot as plt

# --- 1. डेटा तैयार करना ---
# मान लो हमारे पास अलग-अलग 12 घरों की कीमतें हैं (लाख रुपये में)
house_prices = [22, 25, 28, 35, 38, 42, 44, 48, 52, 55, 78, 85]

# --- 2. कैनवास सेटअप ---
fig, ax = plt.subplots(figsize=(8, 5))

# --- 3. हिस्टोग्राम बनाना (plt.hist) ---
ax.hist(
    house_prices,           # हमारा रॉ (Raw) डेटा
    bins=[20, 40, 60, 80, 100], # हमने खुद रेंज (Bins) तय की: 20-40, 40-60, 60-80, 80-100
    color="lightgreen",     # डिब्बों का अंदर का रंग (हल्का हरा)
    edgecolor="darkgreen",  # डिब्बों की बाहरी बॉर्डर का रंग
    linewidth=1.5,          # बॉर्डर लाइन की मोटाई
    rwidth=0.85             # Relative Width: डिब्बों की चौड़ाई। 0.85 करने से इनके बीच 15% खाली जगह दिखती है, जिससे चार्ट साफ लगता है
)

# --- 4. सजावट और नामकरण ---
ax.set_title("Property Price Distribution (Histogram)", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Price Range (in Lakhs ₹)", fontsize=11, labelpad=10)
ax.set_ylabel("Number of Houses (Frequency/Count)", fontsize=11, labelpad=10)

# --- 5. ग्रिड और फिनिशिंग ---
ax.grid(axis='y', linestyle=':', alpha=0.4) # हल्की आड़ी ग्रिड लाइन्स
ax.spines['top'].set_visible(False)         # ऊपर की बॉर्डर हटाई
ax.spines['right'].set_visible(False)       # दाईं बॉर्डर हटाई

# --- 6. डिस्प्ले करना ---
plt.tight_layout()
plt.show()