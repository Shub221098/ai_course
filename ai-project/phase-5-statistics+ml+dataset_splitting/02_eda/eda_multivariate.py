############### Multivariate Analysis: Jab hum 3 ya usse zyada columns ko ek saath analyze karte hain. ##########
# Positive correlation → strong relationship
# Negative correlation → inverse relationship
# Near 0              → weak linear relationship

# Multiple Columns
#       ↓
# Correlation Matrix
#       ↓
# Heatmap
#       ↓
# Find strong relationships
#       ↓
# Check possible redundant features
#       ↓
# Feature Engineering / ML

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bhk": [1, 1, 2, 2, 3, 3, 4, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

print(df)

print(df.corr(numeric_only=True))
# Output: 
#            area       bhk       age     price
# area   1.000000  0.977525 -0.969579  0.997498
# bhk    0.977525  1.000000 -0.917936  0.979762
# age   -0.969579 -0.917936  1.000000 -0.958797
# price  0.997498  0.979762 -0.958797  1.000000


corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.show()

plt.scatter(
    df["area"],
    df["price"],
    s=df["bhk"] * 100
)

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price — Bubble Size = BHK")
plt.show()

# Check Possible Redundant Features (Multicollinearity)
# Redundant feature ka matlab hota hai do aise input variables jo aapas
# me lagbhag identical information carry karte hain.
# Heatmap me dekhein:
# area vs bhk = 0.98!   
# Ye correlation lagbhag $1.0$ ke barabar hai.   
# Iska matlab: BHK badhne par area hi badh raha hai, alag se koi nayi information model ko nahi mil rahi.
# Machine Learning me isko Multicollinearity bolte hain. 
# Dono ko ek saath rakhne par Linear Regression jaise models confuse ho jate hain (overfitting aur unstable weights).

################ Ab is analysis se aap ML model banane se pehle ye concrete decisions lenge: ##############

# Feature Drop (Redundancy Removal):

# Kyunki area aur bhk aapas me 0.98 correlated hain, aap kisi ek feature ko drop kar sakte hain (usually area ko rakhte hain kyunki continuous numeric value zyada detailed hoti hai).   
# PNG

# Key Predictors:

# Target variable (price) ke liye area (+1.0) aur age (-0.96) sabse powerful features hain.   
# PNG

# Feature Creation (Feature Engineering):

# Aap naya ratio feature bana sakte hain, jaise:

# area_per_bhk= 
# bhk
# area
# ​
 
# Isse multicollinearity khatam ho jayegi aur model ko room size ka naya pattern milega.