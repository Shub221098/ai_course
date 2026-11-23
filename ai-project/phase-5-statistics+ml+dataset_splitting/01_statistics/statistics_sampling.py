import numpy as np

# # Seed set kiya taaki data fix rahe
# np.random.seed(42)

# # Mano hamare paas 1 Lakh logon ki salary ka data hai (POPULATION)
# population_salary = np.random.normal(loc=40000, scale=10000, size=100000)

# # Population ka Mean calculate karte hain
# pop_mean = np.mean(population_salary)

# # --- SAMPLING KA KHEL ---
# # Hum randomly 100 logon ka sample uthate hain (SAMPLE)
# sample_salary = np.random.choice(population_salary, size=5000)

# # Sample ka Mean calculate karte hain
# sample_mean = np.mean(sample_salary)

# print(f"Population Mean (True Average) : ₹{pop_mean:.2f}")
# print(f"Sample Mean (Estimated Average): ₹{sample_mean:.2f}")


# 🔥 Practice Assignment
# import numpy as np

# population = np.arange(1, 1001)
# Task:
# Population ka mean find karo.
# Randomly 100 values ka sample select karo.
# Sample ka mean find karo.
# Population mean aur sample mean compare karo.
# Code 5 baar run karo aur observe karo sample mean kaise change hota hai.
# Bonus 🧠

# size=10, size=100, aur size=500 compare karo.

population = np.arange(1, 1001)

population_mean = np.mean(population)

sample = np.random.choice(population,
    size=10,
    replace=False
)

sample_mean_ten = np.mean(sample)

sample = np.random.choice(population,
    size=100,
    replace=False
)

sample_mean_hund = np.mean(sample)

sample = np.random.choice(population,
    size=500,
    replace=False
)

sample_mean_five_hund = np.mean(sample)

print(f"Population Mean: ${population_mean: .4f}")
print(f"Sample Mean for size 10: ${sample_mean_ten: .4f}")
print(f"Sample Mean for size 100: ${sample_mean_hund: .4f}")
print(f"Sample Mean for size 500: ${sample_mean_five_hund: .4f}")
print(f"Comparing Population and Sample Mean for 10: ${population_mean - sample_mean_ten}")
print(f"Comparing Population and Sample Mean for 100: ${population_mean - sample_mean_hund}")
print(f"Comparing Population and Sample Mean for 500: ${population_mean - sample_mean_five_hund}")

