import numpy as np
import matplotlib.pyplot as plt

# CLT (Central Limit Theoram):- 

# Agar hum kisi population se bahut saare random samples lein aur har sample ka mean calculate karein,
# to un sample means ka distribution approximately normal distribution ki taraf jaata hai — especially jab sample size sufficiently large ho.

# Expected pattern:

# n = 10   → Standard Error बड़ा
# n = 30   → Standard Error कम
# n = 100  → Standard Error और कम

# Mathematically:

# SE = σ / √n

# So:

# Sample Size ↑
#      ↓
# √n ↑
#      ↓
# SE ↓

population = np.arange(1, 1001)

sample_means1 = []
sample_means2 = []
sample_means3 = []

def generate_sample_means(population, sample_size, number_of_samples):
    for i in range(number_of_samples):
        sample = np.random.choice(
            population,
            size=sample_size,
            replace=False 
        )
    sample_mean = np.mean(sample)
    return sample_mean

sample_means1.append(generate_sample_means(population, 10, 1000))
plt.hist(sample_means1, bins=10)
standard_error1 = np.std(sample_means1)
print(f"Standard Error1: ${standard_error1}")

sample_means2.append(generate_sample_means(population, 30, 1000))
plt.hist(sample_means2, bins=30)
standard_error2 = np.std(sample_means2)
print(f"Standard Error2: ${standard_error2}")

sample_means3.append(generate_sample_means(population, 100, 1000))
plt.hist(sample_means3, bins=100)
standard_error3 = np.std(sample_means3)
print(f"Standard Error3: ${standard_error3}")

plt.title("Distribution of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.show()

