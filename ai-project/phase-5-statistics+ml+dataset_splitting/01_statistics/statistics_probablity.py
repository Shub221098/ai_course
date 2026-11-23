import numpy as np

# Seed set kiya taaki data fix rahe
np.random.seed(42)

# Ek Coin ko 10,000 baar toss karte hain (0 = Tail, 1 = Head)
tosses = np.random.randint(0, 2, size=10000)
print(f"Tosses: ${tosses}")

# Pata karte hain kitni baar Head (1) aaya
total_heads = np.sum(tosses==1)
print(f"Total Heads: ${total_heads}")
total_tails = np.sum(tosses==0)
print(f"Total Tails: ${total_tails}")

prob_head = total_heads / 10000

print(f"Total Heads cooked: {total_heads}")
print(f"Calculated Probability of Head: {prob_head:.4f} (Expected: 0.5000)")

# ============================================================================

# Dice practical

tosses = np.random.randint(1, 7, size=5000)

num_six = np.sum(tosses==6)
print(f"Total sixes: {num_six}")

prob_six = num_six / 5000

print(f"Six comes on dice: ${num_six} times")
print(f"Calculated Probability of six occured on dice: {prob_six: .4f}")

# Task 1

# Coin ko 1000 times flip simulate karo.

# Find:

# Heads count
# Tails count
# Heads probability
# Tails probability

flip = np.random.randint(0, 2, 1000)

heads_count = np.sum(flip==1)
print(f"Head count: ${heads_count}")
tails_count = np.sum(flip==0)
print(f"Tails count: ${tails_count}")

prob_head = heads_count / 1000
print(f"Head probability: ${prob_head}")
prob_tail = tails_count / 1000
print(f"Tail probability: ${prob_tail}")

# Task 2

# Dice ko 10,000 times roll karo.

# Find probability of:

# Getting 6
# Getting an even number
# Getting a number greater than 4

total_roll = 10000
dice_roll = np.random.randint(1, 7, total_roll)

get_six = np.sum(dice_roll==6)
print(f"Sum of getting number six: ${get_six}")
get_even = np.sum(dice_roll % 2 == 0)
print(f"Sum of getting even numbers: ${get_even}")
get_num_greaterthan_four = np.sum(dice_roll > 4)
print(f"Sum of getting number greater than four: ${get_num_greaterthan_four}")

prob_six= get_six / total_roll
print(f"Probablity of getting number six: ${prob_six}")
prob_even= get_even / total_roll
print(f"Probablity of getting even numbers: ${prob_even}")
prob_num_greaterthan_four= get_num_greaterthan_four / total_roll
print(f"Probablity of getting number greater than four: ${prob_num_greaterthan_four}")

# Theoretical Probability:डाइस में कुल 6 साइड्स होती हैं ($1, 2, 3, 4, 5, 6$) और 6 केवल 1 बार आता है:
# P (Getting 6) = 1 / 6 = approx 0.1667 or  16.67%
# Experimental Probability (आपके Python कोड की तरह): आपने डाइस को $1000$ बार रोल किया (total_roll = 1000), और मान लीजिए $175$ बार 6 आया:
# P (Getting 6) = 175 / 1000 = approx 0.175 or 17.5%


# Conditional Probablity : Conditional probability mein denominator condition ke according change hota hai.
# P(A | B)

total_students = 1000

python_students = 600

male_python_students = 450

female_python_students = 150

prob_python = 600 / 1000  # P(Python)

prob_male_python = 450 / 600  # P(Male | Python)

prob_female_python = 150 / 600  # P(Female | Python)

# Bayes Theoram :  Bayes' Theorem hume reverse probability calculate karne mein help karta hai. 
# P(A | B) = P(B | A) × P(A) / P(B)
# P(A)     → Prior
# P(B | A) → Likelihood
# P(B)     → Evidence
# P(A | B) → Posterior

total_students = 100

python_students = 60
male_python_students = 45
total_male_students = 50

# 1. P(Python)
prob_python_students = python_students / total_students
print("P(Python):", prob_python_students)
# 2. P(Male | Python)
prob_male_python = male_python_students / python_students
print("P(Male | Python):", prob_male_python)
# 3. P(Male)
prob_male = total_male_students / total_students
print("P(Male):", prob_male)
# 4. P(Python | Male) using Bayes' Theorem
prob_python_male = prob_male_python * python_students / total_male_students
print("P(Python | Male):", prob_python_male)