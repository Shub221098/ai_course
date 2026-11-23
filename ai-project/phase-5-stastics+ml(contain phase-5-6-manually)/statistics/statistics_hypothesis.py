# Hypothesis Testing: Kisi claim ko data ke basis par test karna = Hypothesis Testing

# Numerical Data
#       ↓
# T-Test / Z-Test
#       ↓
# Mean compare

# while:

# Categorical Data
#       ↓
# Chi-Square
#       ↓
# Counts / Categories compare


# scipy -> scientific python library that contains advanced mathematical, statstical advanced functions.
# tstat -> 
# t_stat ek "Score" ya "Farak Indicator" hai, jo hume yeh batata hai ki hamara Sample Mean, hamare Hypothesized Mean (50) se kitna door (bhatka hua) hai.

# p_value ->

def find_p_value_and_t_stat(sample, mean):
    print(f"Caluclation of sample: {sample} and mean: {mean}")
    t_stat, p_value = stats.ttest_1samp(sample, mean)
    print("T-statistic:", t_stat)
    print("P-value:", p_value)

    alpha = 0.05

    if p_value < alpha:
        print("Reject H0")
    else:
        print("Fail to reject H0")

# H0 -> Null Hypothesis
# H1 -> Alternative Hypothesis
# alpha(α) -> Significance level

sample = [52, 51, 49, 50, 53, 52, 48, 51, 50, 52]
# H₀: μ = 50
# H₁: μ ≠ 50
find_p_value_and_t_stat(sample, 50)

# Practical Assignment

sample = [102, 98, 101, 105, 99, 103, 100, 97, 104, 101]
# H₀: μ = 100
# H₁: μ ≠ 100
find_p_value_and_t_stat(sample, 100)


# Type1 Error and Type2 Error in Hypothesis Test

# Reality	       Our Decision	           Result                          Asli Statistical Naam
# H₀ True	    Fail to reject H₀	    ✅ Correct               True Negative (Confidence Level, 1 - alpha)
# H₀ True	    Reject H₀	            🔴 Type I Error                 False Positive (alpha)
# H₀ False	    Reject H₀	            ✅ Correct                   Statistical Power (1 - beta)
# H₀ False	    Fail to reject H₀	    🔵 Type II Error                False Negative (beta)

# One tailed test or two tailed test

# Two tailed Test - Whether the exact mean changes where we only meant to check whether μ = 50 or not, we didn't check how much less or greater it is according
#  to last mean which is μ = 50.
t_stat, p_value = stats.ttest_1samp(sample, mean)


# One tailed Test - Whether the exact mean is greater then the last tracked mean, or whether the exact mean is less then the last tracked mean.
t_stat, p_value = stats.ttest_1samp(sample, popmean= mean, alternative='greater')
t_stat, p_value = stats.ttest_1samp(sample, popmean= mean, alternative='less')

