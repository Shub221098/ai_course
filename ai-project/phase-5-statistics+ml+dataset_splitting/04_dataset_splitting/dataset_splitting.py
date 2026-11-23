"""
Phase 5 — H. Dataset Splitting
Revision Notes + Runnable Python Examples

Topics:
1. Train Set
2. Validation Set
3. Test Set
4. Train/Test Split
5. Cross Validation
6. Stratified Split
7. Data Leakage

Memory trick:
Train = Learn
Validation = Tune
Test = Final Check
CV = Repeat
Stratify = Preserve Class Ratio
Leakage = Don't Cheat
"""

# ============================================================
# 0. IMPORTS
# ============================================================

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


# ============================================================
# 1. TRAIN SET
# ============================================================
# Train Set = Model ko sikhane wala data.
# Model training data se patterns learn karta hai.

X = [
    [1000],
    [1200],
    [1500],
    [1800],
    [2000],
]

y = [20, 24, 30, 36, 40]

# Split the data into training and testing sets.
# test_size=0.2 means:
# 80% data -> Training
# 20% data -> Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print("=" * 60)
print("1. TRAIN SET")
print("=" * 60)

print("Training Data:")
print(X_train)

print("Training Target:")
print(y_train)


# ============================================================
# 2. VALIDATION SET
# ============================================================
# Validation Set = Model ko tune/compare karne ke liye.
#
# Typical example:
# 70% -> Train
# 15% -> Validation
# 15% -> Test
#
# Hum pehle 20% Test nikalenge.
# Remaining 80% mein se 25% Validation lenge.
#
# 25% of 80% = 20%
#
# Final:
# 60% -> Train
# 20% -> Validation
# 20% -> Test

X = [
    [1000],
    [1200],
    [1500],
    [1800],
    [2000],
    [2200],
    [2500],
    [2800],
    [3000],
    [3500],
]

y = [20, 25, 30, 36, 40, 45, 50, 55, 60, 70]

# First: Separate Test Set
X_temp, X_test, y_temp, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Second: Separate Train and Validation
X_train, X_val, y_train, y_val = train_test_split(
    X_temp,
    y_temp,
    test_size=0.25,
    random_state=42,
)

print("" + "=" * 60)
print("2. TRAIN / VALIDATION / TEST")
print("=" * 60)

print("Train:", len(X_train))
print("Validation:", len(X_val))
print("Test:", len(X_test))


# ============================================================
# 3. TEST SET
# ============================================================
# Test Set = Model ka final exam.
#
# Test data ko training process mein use nahi karna chahiye.
# Model ko test data final evaluation ke time diya jata hai.

print("" + "=" * 60)
print("3. TEST SET")
print("=" * 60)

print("Test Data:")
print(X_test)

print("Test Target:")
print(y_test)


# ============================================================
# 4. TRAIN / TEST SPLIT
# ============================================================
# train_test_split() Scikit-learn ka common function hai.
#
# test_size=0.2:
# 20% -> Test
# 80% -> Train
#
# random_state=42:
# Same data + same random_state -> Same split
#
# 42 koi magic number nahi hai.
# Koi bhi fixed integer use kar sakte ho.

X = [
    [1000],
    [1200],
    [1500],
    [1800],
    [2000],
]

y = [20, 24, 30, 36, 40]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print("" + "=" * 60)
print("4. TRAIN / TEST SPLIT")
print("=" * 60)

print("Train size:", len(X_train))
print("Test size:", len(X_test))


# ============================================================
# 5. CROSS VALIDATION
# ============================================================
# Cross Validation:
# Data ko multiple train/validation splits par evaluate karna.
#
# Example: 5-Fold Cross Validation
#
# Fold 1 -> Validation
# Fold 2 -> Validation
# Fold 3 -> Validation
# Fold 4 -> Validation
# Fold 5 -> Validation
#
# Har round mein baaki data training ke liye use hota hai.
# Finally scores ka average liya ja sakta hai.

X = [
    [1000],
    [1200],
    [1500],
    [1800],
    [2000],
    [2200],
    [2500],
    [2800],
    [3000],
    [3500],
]

y = [20, 25, 30, 36, 40, 45, 50, 55, 60, 70]

model = LinearRegression()

# cv=5 means 5-fold cross validation.
# scoring="r2" means R² score use karna.

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="r2",
)

print("" + "=" * 60)
print("5. CROSS VALIDATION")
print("=" * 60)

print("CV Scores:")
print(scores)

print("Average CV Score:")
print(scores.mean())


# ============================================================
# 6. STRATIFIED SPLIT
# ============================================================
# Stratified Split mostly classification mein useful hai.
#
# Purpose:
# Target classes ka proportion train/test mein preserve karna.
#
# Example:
# Original:
# 80% Class 0
# 20% Class 1
#
# Stratified split approximately:
# Train -> 80% Class 0, 20% Class 1
# Test  -> 80% Class 0, 20% Class 1
#
# Important parameter:
# stratify=y

X = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10],
]

# Classification labels
y = [
    0, 0, 0, 0, 0,
    0, 0, 0, 1, 1,
]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,       # Preserve class distribution
    random_state=42,
)

print("" + "=" * 60)
print("6. STRATIFIED SPLIT")
print("=" * 60)

print("Training labels:")
print(y_train)

print("Testing labels:")
print(y_test)


# ============================================================
# 7. DATA LEAKAGE
# ============================================================
# Data Leakage = Aisi information training process mein aa jana
# jo model ko normally available nahi honi chahiye.
#
# Common example:
#
# WRONG:
# Full Dataset
#      ↓
# Scaling
#      ↓
# Train/Test Split
#
# Problem:
# Scaler ne test data ki information bhi dekhi.
#
# CORRECT:
# Dataset
#      ↓
# Train/Test Split
#      ↓
# Train -> fit_transform()
# Test  -> transform()
#
# Rule:
# TRAIN -> fit + transform
# TEST  -> transform only

X = [
    [1000, 2],
    [1200, 2],
    [1500, 3],
    [1800, 3],
    [2000, 4],
    [2200, 4],
]

y = [20, 24, 30, 36, 40, 45]

# First split the data.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Create scaler.
scaler = StandardScaler()

# CORRECT:
# Fit the scaler ONLY on training data.
# Then transform training data.
X_train_scaled = scaler.fit_transform(X_train)

# CORRECT:
# Test data should only be transformed.
# Do NOT fit on test data.
X_test_scaled = scaler.transform(X_test)

print("" + "=" * 60)
print("7. DATA LEAKAGE - CORRECT APPROACH")
print("=" * 60)

print("Scaled Training Data:")
print(X_train_scaled)

print("Scaled Test Data:")
print(X_test_scaled)


# ============================================================
# 8. COMPLETE MEMORY FLOW
# ============================================================
#
# Full Dataset
#      ↓
# Train/Test Split
#      ↓
# ┌──────────────┬──────────────┐
# │     Train    │     Test     │
# │    Learn     │ Final Check  │
# └──────────────┴──────────────┘
#
# Validation / Cross Validation:
# Used for model tuning and comparison.
#
# Stratify:
# Preserve class ratio in classification.
#
# Data Leakage:
# Never allow test/future information to enter training.


# ============================================================
# 9. IMPORTANT SCikit-learn PATTERN
# ============================================================
# This pattern will appear again and again in Phase 6.

# 1. Split
# X_train, X_test, y_train, y_test = train_test_split(...)

# 2. Create model
# model = SomeModel()

# 3. Train
# model.fit(X_train, y_train)

# 4. Predict
# predictions = model.predict(X_test)

# 5. Evaluate
# Compare predictions with y_test


# ============================================================
# QUICK REVISION
# ============================================================
#
# Train      -> Learn
# Validation -> Tune / Compare
# Test       -> Final Evaluation
# CV         -> Multiple Validation Rounds
# Stratify   -> Preserve Class Ratio
# Leakage    -> Don't Cheat
#
# ============================================================
# END OF H. DATASET SPLITTING
# ============================================================