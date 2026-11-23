import numpy as np

prices = np.array([100, 250, 150, 500, 80, 350])

print("Prices > 200:")
print(prices[prices > 200])
# Output:-
# Prices > 200:
# [250 500 350]

print("Prices between 100 and 400:")
print(prices[(prices >= 100) & (prices <= 400)])
# Output:-
# Prices between 100 and 400:
# [100 250 150 350]

print("Expensive/Affordable:")
print(np.where(prices > 300, "Expensive", "Affordable"))
# Output:-
# Expensive/Affordable:
# ['Affordable' 'Affordable' 'Affordable' 'Expensive' 'Affordable' 'Expensive']