import matplotlib.pyplot as plt

# --- 1. डेटा तैयार करना ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20, 35, 30, 45, 50, 65]
profit = [5, 12, 8, 18, 20, 28]

# --- 2. 2x2 का ग्रिड ढांचा तैयार करना ---
# plt.subplots(2, 2) का मतलब: 2 रो (Rows) और 2 कॉलम (Columns) = टोटल 4 खाली खाने बनेंगे।
# axs एक 2D मैट्रिक्स है जिसके इंडेक्स [Row, Column] की तरह काम करते हैं।
fig, axs = plt.subplots(2, 2, figsize=(10, 7))

# --- 🟢 3. पहला खाना (Top-Left: Row 0, Column 0) -> Sales Bar Chart ---
axs[0, 0].bar(months, sales, color="pink", edgecolor="navy", width=0.6, linewidth=1.2)
axs[0, 0].set_title("Sales by Month", fontsize=11, fontweight="bold")
axs[0, 0].set_ylabel("Sales Value")
axs[0, 0].grid(axis="y", linestyle=":", alpha=0.4)

# --- 🟠 4. दूसरा खाना (Top-Right: Row 0, Column 1) -> Profit Line Chart ---
axs[0, 1].plot(months, profit, marker="o", color="darkorange", linewidth=2.5, markersize=6)
axs[0, 1].set_title("Profit Trend", fontsize=11, fontweight="bold")
axs[0, 1].set_ylabel("Profit Value")
axs[0, 1].grid(axis="y", linestyle=":", alpha=0.4)

# --- 🟢 5. तीसरा खाना (Bottom-Left: Row 1, Column 0) -> Sales Histogram ---
axs[1, 0].hist(sales, bins=3, color="lightgreen", edgecolor="darkgreen", rwidth=0.85)
axs[1, 0].set_title("Sales Frequency (Histogram)", fontsize=11, fontweight="bold")
axs[1, 0].set_xlabel("Sales Range")
axs[1, 0].set_ylabel("Count")
axs[1, 0].grid(axis="y", linestyle=":", alpha=0.4)

# --- 🔴 6. चौथा खाना (Bottom-Right: Row 1, Column 1) -> Scatter Plot ---
axs[1, 1].scatter(sales, profit, s=120, color="crimson", edgecolor="black", alpha=0.8)
axs[1, 1].set_title("Sales vs Profit Correlation", fontsize=11, fontweight="bold")
axs[1, 1].set_xlabel("Sales")
axs[1, 1].set_ylabel("Profit")
axs[1, 1].grid(True, linestyle=":", alpha=0.4)

# --- ✨ 7. एडवांस ट्रिक: एक साथ सारे चार्ट्स की बॉर्डर (Spines) साफ करना ---
# क्योंकि axs एक 2x2 मैट्रिक्स है, हम लूप चलाकर चारों खानों की top और right बॉर्डर एक साथ हटा देंगे।
for row in axs:
    for ax in row:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

# --- 👑 8. पूरे डैशबोर्ड का एक मेन बड़ा टाइटल लगाना ---
# y=0.98 का मतलब यह टाइटल पूरे फ्रेम के थोड़ा ऊपर अच्छे से सेट रहेगा।
fig.suptitle("Business Analytics Executive Dashboard", fontsize=15, fontweight="bold", y=0.98)

# --- 9. लेआउट एडजस्ट करना और शो करना ---
# tight_layout() यहाँ सबसे ज्यादा जरूरी है क्योंकि 4 चार्ट के नाम आपस में भिड़ सकते हैं।
plt.tight_layout()
plt.show()