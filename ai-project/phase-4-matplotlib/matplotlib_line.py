import matplotlib.pyplot as plt

# --- 1. डेटा तैयार करना ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]  # X-Axis पर दिखाने के लिए महीने
sales = [20, 35, 30, 45, 50, 65]                     # Y-Axis पर दिखाने के लिए सेल्स
revenue = [10, 15, 14, 22, 25, 32]                   # Y-Axis पर दिखाने के लिए रेवेन्यू

# --- 2. कैनवास (फिगर) सेट करना ---
# figsize=(9, 5) का मतलब है चार्ट 9 इंच चौड़ा और 5 इंच लंबा बनेगा
fig, ax = plt.subplots(figsize=(9, 5))

# --- 3. पहली लाइन बनाना (Sales) ---
ax.plot(
    months,                 # X-axis का डेटा
    sales,                  # Y-axis का डेटा
    label="Sales",          # पहचान बॉक्स (Legend) के लिए नाम
    color="royalblue",      # लाइन का सुंदर नीला रंग
    linewidth=3,            # लाइन की मोटाई (Thickness)
    marker="o",             # डेटा पॉइंट पर गोल बिंदु (Circle)
    markersize=8,           # गोल बिंदु का साइज बड़ा किया
    markerfacecolor="white",# बिंदु के अंदर का रंग सफेद किया
    markeredgewidth=2       # बिंदु की बाहरी बॉर्डर की मोटाई
)

# --- 4. दूसरी लाइन बनाना (Revenue) ---
ax.plot(
    months,                 # X-axis का डेटा
    revenue,                # Y-axis का डेटा
    label="Revenue",        # पहचान बॉक्स (Legend) के लिए नाम
    color="darkorange",     # लाइन का संतरी रंग
    linewidth=2.5,          # लाइन की मोटाई
    linestyle="--",         # लाइन को टुकड़ों में काटा (Dashed style)
    marker="s",             # डेटा पॉइंट पर चौकोर बिंदु (s = Square)
    markersize=7            # चौकोर बिंदु का साइज
)

# --- 5. डेटा लेबल्स लगाना (plt.text) ---
# लूप चलाकर हम हर महीने के पॉइंट के ठीक ऊपर उसका असली नंबर छाप रहे हैं
for i in range(len(months)):
    # सेल्स के नंबर लाइन के थोड़े ऊपर (sales[i] + 1.5) छापेंगे
    ax.text(months[i], sales[i] + 1.5, str(sales[i]), 
            color="royalblue", fontweight="bold", ha="center", fontsize=9)
    
    # रेवेन्यू के नंबर लाइन के थोड़े ऊपर (revenue[i] + 1.5) छापेंगे
    ax.text(months[i], revenue[i] + 1.5, str(revenue[i]), 
            color="darkorange", fontweight="bold", ha="center", fontsize=9)

# --- 6. चार्ट की सजावट और नामकरण ---
ax.set_title("Monthly Sales vs Revenue Performance", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Months of the Year", fontsize=11, labelpad=10)
ax.set_ylabel("Value (in Lakhs ₹)", fontsize=11, labelpad=10)

# --- 7. ग्रिड लाइन्स (हल्की बैकग्राउंड लाइन्स) ---
# axis='y' यानी सिर्फ आड़ी (Horizontal) लाइनें दिखेंगी, जो बहुत हल्की (alpha=0.4) और डॉटेड (':') होंगी
ax.grid(axis='y', linestyle=':', alpha=0.4)

# --- 8. बाहरी बॉर्डर (Spines) को हटाना ---
# आधुनिक लुक के लिए ऊपर की छत और दाईं दीवार को हटा दिया
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# --- 9. लेजेंड (पहचान बॉक्स) दिखाना ---
# loc="upper left" से यह बॉक्स ऊपर बाईं तरफ सेट हो जाएगा
ax.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="pink")

# --- 10. लेआउट सेट करना और डिस्प्ले करना ---
# tight_layout() से कोई भी टेक्स्ट या नंबर फ्रेम से बाहर नहीं कटता
plt.tight_layout()
plt.show()