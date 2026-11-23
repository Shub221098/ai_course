# Matrix Operations: 
# Neural networks process data in batches. 
# Matrix operations allow an entire layer of neurons to process a batch of inputs in a single, parallelized computation.
# Real neural network mein manually har neuron calculate nahi karte.
# Z = X × W + b
# This is why matrix multiplication is extremely important in Deep Learning.


# Forward Propagation: Forward propagation turns inputs into predictions by passing the signal through consecutive layers:
# Input
#   ↓
# Weighted Sum
#   ↓
# Bias
#   ↓
# Activation
#   ↓
# Prediction

# For Example: 
# House Features
# [area, bedrooms]
#        ↓
#    Hidden Layer
#  [neuron1, neuron2]
#        ↓
#    Output Neuron
#        ↓
#  Predicted Price

import numpy as np

# Input
X = np.array([[2, 3]])

# Weights
W = np.array([
    [0.5, 0.1],
    [0.2, 0.7]
])

# Bias
b = np.array([[1, 0.5]])

# Forward propagation
Z = X @ W + b

print("Z:")
print(Z)

# ReLU
A = np.maximum(0, Z)

print("After ReLU:")
print(A)

# NOTE:
# Python/Numpy me:
# A @ B -> Matrix Multiplication
# A * B -> Element Wise Multiplication

# Loss: 

# Model ne prediction ki:
# Actual price     = 70
# Predicted price  = 65
# Obviously model perfect nahi hai.
# Humein measure karna hai:
# Model kitna galat hai?
# Isko Loss kehte hain.
# Simple example:
# error = actual - predicted
# error = 70 - 65 = 5

# Model ko kaise pata chale ki weights ko change kaise karna hai?
# Solution is 
# Backpropagation
#         +
# Gradient Descent

# Input
#   ↓
# Weighted Sum
#   ↓
# Activation
#   ↓
# Prediction
#   ↓
# Loss
#   ↓
# Backpropagation
#   ↓
# Gradient
#   ↓
# Update Weights
#   ↓
# Better Prediction



# Gradient Descent: Weight ko kis direction mein change karein taaki loss kam ho?
# Gradient       → Loss increase direction
# Gradient Descent → Loss decrease direction

# Learning Rate: Kitna bada step lena hai, ye learning rate decide karta hai.
# Formula: new_weight = old_weight - learning_rate × gradient
# old_weight = 2
# learning_rate = 0.1
# gradient = 4

# new_weight = 2 - (0.1 × 4) = 2 - 0.4 = 1.6
# Old weight → 2
# New weight → 1.6

# If Learning rate is
# Too small → Slow training
# Too large → Unstable training
# Good value → Efficient training

# Forward propagation
# Input
#  ↓
# Network
#  ↓
# Prediction
#  ↓
# Loss


# Backpropagation
# Loss
#  ↓
# Calculate gradients
#  ↓
# Weights ke gradients
#  ↓
# Weights update

# So complete training:

#        FORWARD
# Input ───────────→ Prediction
#                      ↓
#                     Loss
#                      ↓
#        BACKWARD ← Gradients
#                      ↓
#                 Update Weights


weight = 3.0

input_value = 2.0
actual = 10.0

learning_rate = 0.1

for step in range(5):

    # Forward propagation
    prediction = input_value * weight

    # Loss
    loss = (actual - prediction) ** 2

    # Gradient
    gradient = 2 * input_value * (prediction - actual)

    # Update weight
    weight = weight - learning_rate * gradient

    print(
        f"Step: {step + 1}, "
        f"Prediction: {prediction:.2f}, "
        f"Loss: {loss:.2f}, "
        f"Weight: {weight:.2f}"
    )