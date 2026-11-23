# Neural Network mein bhi basic idea same hai, but model ke andar bahut saare interconnected neurons hote hain.

# Example:

# area = 1200
# bedrooms = 3
# location = Surat
#        ↓
#    ML Model
#        ↓
# price = ₹70 lakh


# Input Layer       Hidden Layer       Output Layer

#   area  ────────┐
#                 ├──── neuron ────┐
#   bedrooms ─────┤                │
#                 ├──── neuron ────┼──── price
#   location ─────┤                │ 
#                 └──── neuron ────┘


# Neuron kya hota hai?

# Neuron ko ek small mathematical function samjho.
# It takes inputs: x1, x2, x3
# Har input ke saath ek weight hota hai: x1 × w1, x2 × w2, x3 × w3
# Phir sabko add karke bias add hota hai: z = x1w1 + x2w2 + x3w3 + b
# Then activation function:
# output = activation(z)
# So complete neuron:

# Inputs
#   ↓
# Weighted Sum
#   ↓
# + Bias
#   ↓
# Activation Function
#   ↓
# Output

# Weight kya hai?
# Weight decide karta hai ki input kitna important hai.
# Model training ke time neural network weights ko automatically learn karta hai.

# Bias kya hai?
# Bias model ko flexibility deta hai
# output = input × weight + bias

# Activation kya hai?
# Ye Deep Learning ka very important concept hai.
# Agar hum sirf:
# y = x1w1 + x2w2 + b
# use karein, toh network basically linear relationship learn karega.

# Activation function network mein non-linearity introduce karta hai.
# Common activations:

# 1. ReLU:
# ReLU(x) = max(0, x)
# negative → 0
# positive → same value

# 2. Sigmoid
# 3. Tanh


# Complete Neuron Example:
# x1 = 2
# x2 = 3

# w1 = 0.5
# w2 = 0.8

# bias = 1

# z(Weighted Sum) = (2 × 0.5) + (3 × 0.8) + 1
#   = 1 + 2.4 + 1
#   = 4.4

# ReLU(4.4) = 4.4

# Neuron output = 4.4