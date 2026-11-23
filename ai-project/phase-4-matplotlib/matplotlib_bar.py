import matplotlib.pyplot as plt
import pandas as pd

# Mujhe kya dikhana hai?
#        ↓
# Comparison?     → Bar
# Trend over time? → Line
# Distribution?   → Histogram
# Relationship?    → Scatter


############## Bar Chart ##############
cities = ["Surat", "Mumbai", "Delhi"]
prices = [5500000, 9000000, 6000000]

plt.bar(cities, prices)

plt.xlabel("City")
plt.ylabel("Average Price")
plt.title("Average Property Price by City")

plt.show()


# Real life Use Cases

df = pd.DataFrame({
    "city": ["Surat", "Mumbai", "Delhi"],
    "average_price": [5500000, 9000000, 6000000]
})

df = df.sort_values(by="average_price")

# Step 1: Setting up the Canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Step 2: Customising the Bars

# color="pink": Fills the inside of all the bars with a clean, light pink
# color.edgecolor="navy": Draws a crisp, dark blue border outline around every single bar so they stand out clearly.
# linewidth=1.5: Sets the thickness of that dark blue border line to 1.5 points.
# width=0.6: Controls how thick the bars are. The default thickness is 0.8. Lowering it to 0.6 shrinks the bars slightly, adding clean, professional white space between them so they don't look crowded.
ax.bar(df["city"], df["average_price"], color="pink", edgecolor="navy", linewidth=1.5, width=0.6)

ax.xlabel("City")
ax.ylabel("Average Price")
ax.title("Average Property Price")

#  Step 3: Adding Grid Lines

# axis='y': This is crucial. It tells Matplotlib to only draw horizontal grid lines tracking across from the Y-axis.
# It keeps vertical grid lines turned off, which prevents the chart from looking like a messy prison cage.
# linestyle=':': Changes the grid lines from solid dark lines to subtle dotted lines.
# alpha=0.6: Sets the transparency to 60%. This makes the lines faint and light grey, ensuring they sit gently in the background without distracting from the actual bars
ax.grid(axis='y', linestyle=':', alpha=0.6)

# Step 4: Stripping the Border Box (Spines)

# spines are the four boundary box lines that frame a standard chart (top, bottom, left, right).By setting the top and right spines to False,
# we chop off the top ceiling line and the right wall line. This modernises the look completely, giving your chart a clean, open minimalist design
# preferred in modern corporate dashboards.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Step 5: Fixing Layout and Spacing

# plt.xticks(rotation=45, ha="right"): Tilts long titles like "Affordable 2 BHK" at a 45-degree angle and anchors their right edge directly under the bar.
# This stops them from overlapping into an unreadable blob.plt.
# tight_layout(): Automatically calculates how much space the new tilted labels take and shrinks the graph just enough so that no text gets cut off
# at the bottom boundary of the image.
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()