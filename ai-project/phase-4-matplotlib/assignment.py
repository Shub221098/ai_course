import pandas as pd
import matplotlib.pyplot as plt

# Ek student performance dataset banao:

students = ["A", "B", "C", "D", "E"]

math = [80, 65, 90, 70, 85]
science = [75, 70, 95, 60, 88]
english = [85, 72, 80, 75, 90]

# Create a 2 × 2 subplot:

# ┌─────────────────┬─────────────────┐
# │ Math            │ Science         │
# │ Bar Chart       │ Line Chart      │
# ├─────────────────┼─────────────────┤
# │ English         │ Math vs Science │
# │ Bar Chart       │ Scatter Plot    │
# └─────────────────┴─────────────────┘


# Create a dataflame
df = pd.DataFrame({
    "students": ["A", "B", "C", "D", "E"],
    "math" : [80, 65, 90, 70, 85],
    "science" :  [75, 70, 95, 60, 88],
    "english" : [85, 72, 80, 75, 90]
})

fig, axs = plt.subplots(2, 2, figsize=(10, 7))

# Bar Chart
axs[0, 0].bar(df["students"], df["math"], color="pink", edgecolor="navy", width=0.3, linewidth=1.2)
axs[0, 0].set_title("Students Math Performance", fontsize=11, fontweight="bold")
axs[0, 0].set_ylabel("Math")
axs[0, 0].grid(axis="y", linestyle=":", alpha=0.4)


# Line Chart
axs[0, 1].plot(df["students"], df["science"], marker="o", color="darkorange", linewidth=2.5, markersize=6)
axs[0, 1].set_title("Students Science Performance", fontsize=11, fontweight="bold")
axs[0, 1].set_ylabel("Science")
axs[0, 1].grid(axis="y", linestyle="-", alpha=0.4)

# Histogram Chart
axs[1, 0].bar(df["students"], df["english"], color="lightgreen", edgecolor="darkgreen", width=0.3, linewidth=1.2)
axs[1, 0].set_title("Students English Performance", fontsize=11, fontweight="bold")
axs[1, 0].set_ylabel("English")
axs[1, 0].grid(axis="y", linestyle="-.", alpha=0.4)

# Scatter Chart
axs[1, 1].scatter(df["math"], df["science"], color="crimson", edgecolor="black", alpha=0.8)
axs[1, 1].set_title("Students English Performance", fontsize=11, fontweight="bold")
axs[1, 1].set_xlabel("Math")
axs[1, 1].set_ylabel("Science")
axs[1, 1].grid(True, linestyle="--", alpha=0.4)

for row in axs:
    for ax in row:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    

fig.suptitle("Student Performance Analytics Dashboard", fontsize=15, fontweight="bold", y=0.98)

plt.tight_layout()
plt.show()