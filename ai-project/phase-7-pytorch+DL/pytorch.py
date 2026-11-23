# ============================================================
# Phase 7 — PyTorch Fundamentals, Tensors & Model Persistence
# Comprehensive Notes + Runnable Code Examples
# ============================================================


# ############################################################
# 1. PyTorch Kya Hai?
# ############################################################
# PyTorch ek open-source Python library hai jiska use Deep Learning
# aur Neural Networks ko build aur train karne ke liye hota hai.

# PyTorch ki main capabilities:
# 1. Neural Networks (ANN, CNN, RNN, Transformers) build aur train karna.
# 2. Images, Audio, aur Text data par AI models train karna.
# 3. Automatic Differentiation (Autograd) se gradients auto-calculate karna.
# 4. GPU (CUDA) acceleration par super-fast computations chalana.

# Virtual environment mein installation:
# pip install torch numpy


# ############################################################
# 2. Tensor Kya Hota Hai?
# ############################################################
# Tensor PyTorch ka primary data structure hai (NumPy ndarray jaisa).
# Deep Learning mein saara data (inputs, weights, biases, loss, predictions)
# Tensors ke form mein represent hota hai.

# Tensor Dimensions Breakdown:
# ├── 0D Tensor (Scalar)  → Single number (e.g. loss = 16.0, temp = 37)
# ├── 1D Tensor (Vector)  → 1D List of numbers (e.g. [2, 4, 6])
# ├── 2D Tensor (Matrix)  → 2D Grid with rows & columns (e.g. [[1,2],[3,4]])
# └── 3D/ND Tensor        → Multi-dimensional arrays (e.g. RGB Image: [Channels, Height, Width])


# ############################################################
# 3. NumPy vs PyTorch Comparison
# ############################################################
import numpy as np
import torch
import torch.nn as nn

print("=" * 60)
print("3. NUMPY VS PYTORCH COMPARISON")
print("=" * 60)

# NumPy Array
np_arr = np.array([10, 20, 30])
print("NumPy Array * 2:", np_arr * 2)  # [20 40 60]

# PyTorch Tensor
torch_tensor = torch.tensor([10, 20, 30])
print("PyTorch Tensor * 2:", torch_tensor * 2)  # tensor([20, 40, 60])

# Key Differences:
# - NumPy CPU par chal karta hai aur automatic differentiation nahi support karta.
# - PyTorch GPU par chal sakta hai aur Autograd (`requires_grad=True`) provide karta hai.


# ############################################################
# 4. Tensor Creation Methods
# ############################################################
print("\n" + "=" * 60)
print("4. TENSOR CREATION METHODS")
print("=" * 60)

# 0D Tensor (Scalar)
scalar_0d = torch.tensor(10)

# 1D Tensor (Vector)
vector_1d = torch.tensor([10, 20, 30])

# 2D Tensor (Matrix)
matrix_2d = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print("0D Tensor (Scalar):", scalar_0d)
print("1D Tensor (Vector):", vector_1d)
print("2D Tensor (Matrix):\n", matrix_2d)

# Useful Tensor Creation Functions
print("\n--- Factory Functions ---")
print("Zeros (2x3):\n", torch.zeros(2, 3))       # All 0s
print("Ones (2x3):\n", torch.ones(2, 3))         # All 1s
print("Random (2x3):\n", torch.rand(2, 3))       # Uniform random between [0, 1)
print("Arange (0 to 4):", torch.arange(5))       # Range of numbers [0, 1, 2, 3, 4]


# ############################################################
# 5. Tensor Attributes: Shape, ndim, dtype, numel()
# ############################################################
print("\n" + "=" * 60)
print("5. TENSOR ATTRIBUTES (Shape, ndim, dtype, numel)")
print("=" * 60)

x = torch.tensor([
    [10, 20, 30],
    [40, 50, 60]
])

print("Shape (Dimensions size):", x.shape)        # torch.Size([2, 3])
print("Dimensions (ndim):", x.ndim)              # 2
print("Data type (dtype):", x.dtype)             # torch.int64
print("Total elements (numel):", x.numel())      # 6

# Note: Deep Learning mein input features aur weights ke liye
# Commonly `torch.float32` (Float Tensor) use hota hai.
x_float = torch.tensor([10, 20, 30], dtype=torch.float32)
print("Explicit Float32 Dtype:", x_float.dtype)  # torch.float32


# ############################################################
# 6. Tensor Mathematical Operations
# ############################################################
print("\n" + "=" * 60)
print("6. TENSOR MATHEMATICAL OPERATIONS")
print("=" * 60)

a = torch.tensor([10.0, 20.0, 30.0])
b = torch.tensor([1.0, 2.0, 3.0])

print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Element-wise Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Power (a ** 2):", a ** 2)

# Matrix Multiplication (@ operator or torch.matmul)
mat_a = torch.tensor([[1.0, 2.0]])         # Shape: (1, 2)
mat_b = torch.tensor([[3.0], [4.0]])       # Shape: (2, 1)

mat_mult = mat_a @ mat_b                   # (1*3 + 2*4) = 11.0
print("\nMatrix Multiplication (mat_a @ mat_b):\n", mat_mult)


# ############################################################
# 7. 🔥 Most Important: Autograd & requires_grad=True
# ############################################################
print("\n" + "=" * 60)
print("7. AUTOGRAD & REQUIRES_GRAD=TRUE (Automatic Differentiation)")
print("=" * 60)

# Gradient Descent Formula:
# w_new = w_old - learning_rate * (dL / dw)
# PyTorch is dL/dw (Gradient) ko automatic calculate karta hai.

# Weight parameter define kar rahe hain jiske gradients track hone hain
w = torch.tensor(3.0, requires_grad=True)

# Forward Pass Calculation
prediction = w * 2.0

# Loss Calculation (Mean Squared Error style: (prediction - target)^2)
loss = (prediction - 10.0) ** 2.0

# Backpropagation: PyTorch executes automatic differentiation
loss.backward()

print("Weight (w):", w.item())
print("Prediction (w * 2):", prediction.item())
print("Loss ((pred - 10)^2):", loss.item())
print("Calculated Gradient (dL/dw):", w.grad.item())

# Mathematical Proof of Gradient:
# Loss function: L(w) = (2w - 10)^2
# Derivative w.r.t w: dL/dw = 2 * (2w - 10) * 2 = 4 * (2w - 10)
# Substituting w = 3.0:
# dL/dw = 4 * (2(3) - 10) = 4 * (6 - 10) = 4 * (-4) = -16.0 ✅


# ############################################################
# 8. Memory Persistence: CPU, RAM vs SSD & Model Weights Saving
# ############################################################
print("\n" + "=" * 60)
print("8. MEMORY PERSISTENCE & SAVING MODEL WEIGHTS")
print("=" * 60)

# Memory Hierarchy Concept:
# ├── CPU      → Brain (Executes calculations & instructions)
# ├── RAM      → Temporary Volatile Working Memory (Erased on power off / program exit)
# └── SSD/HDD  → Permanent Non-Volatile Storage (Files, datasets, model.pth)

# How AI Models "Remember" Forever:
# AI models apnee learned knowledge ko "Weights & Biases" (parameters) me store karte hain.
# Training ke dauran weights RAM/VRAM me hote hain. Unhe disk par save kar diya jaye
# toh program finish hone ya system restart hone ke baad bhi weights recover kiye ja sakte hain!

# Model creation example
model = nn.Linear(in_features=2, out_features=1)

# Learned weights ko SSD/HDD file ("model.pth") par save karna
torch.save(model.state_dict(), "model.pth")
print("Model state_dict successfully saved to disk as 'model.pth'!")

# Future / Next day: Naya model instance bana kar saved weights reload karna
new_model = nn.Linear(in_features=2, out_features=1)
new_model.load_state_dict(torch.load("model.pth", weights_only=True))
new_model.eval()
print("Saved parameters successfully loaded into new_model instance!")


# ############################################################
# 9. GPU Acceleration & Device Transfer (.to(device))
# ############################################################
print("\n" + "=" * 60)
print("9. GPU ACCELERATION & DEVICE TRANSFER (.to(device))")
print("=" * 60)

# CPU RAM vs GPU VRAM:
# CPU : General-purpose tasks, OS, normal Python code (Fewer powerful cores)
# GPU : Parallel matrix multiplication, Deep Learning acceleration (Thousands of small cores, VRAM)

# Device Configuration: CUDA GPU check karo, nahi toh CPU fallback
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Selected Execution Device:", device)

# Crucial PyTorch Rule:
# Model Parameters aur Input Tensors dono SAME DEVICE par hone chahiye!
model_gpu = nn.Linear(3, 1).to(device)
input_tensor = torch.tensor([[1.0, 2.0, 3.0]]).to(device)

prediction_gpu = model_gpu(input_tensor)
print("Input Tensor Device Location:", input_tensor.device)
print("Prediction Output:\n", prediction_gpu)


# ############################################################
# 10. 🧪 Practice Assignment Solutions (Tasks 1 - 4)
# ############################################################
print("\n" + "=" * 60)
print("10. 🧪 PRACTICE ASSIGNMENT SOLUTIONS (TASKS 1 - 4)")
print("=" * 60)

# --- Task 1: Create a tensor [5, 10, 15, 20] and print shape, ndim, dtype ---
t1 = torch.tensor([5, 10, 15, 20])
print("Task 1 Tensor:", t1)
print("Task 1 Shape:", t1.shape)
print("Task 1 Dimensions (ndim):", t1.ndim)
print("Task 1 Data Type (dtype):", t1.dtype)

# --- Task 2: Operations on x = [2, 4, 6] & y = [1, 3, 5] ---
task_x = torch.tensor([2, 4, 6])
task_y = torch.tensor([1, 3, 5])
print("\nTask 2 Addition (x + y):", task_x + task_y)
print("Task 2 Element-wise Multiplication (x * y):", task_x * task_y)

# --- Task 3: Matrix Multiplication [[1, 2], [3, 4]] @ [[5], [6]] ---
mat1 = torch.tensor([[1, 2], [3, 4]])      # Shape: (2, 2)
mat2 = torch.tensor([[5], [6]])            # Shape: (2, 1)
mat_result = mat1 @ mat2                    # (1*5 + 2*6 = 17, 3*5 + 4*6 = 39)
print("\nTask 3 Matrix Multiplication Result (@):\n", mat_result)

# --- Task 4: Autograd with w = 2.0, loss = (w * 3 - 12) ** 2 ---
w_task = torch.tensor(2.0, requires_grad=True)
loss_task = (w_task * 3.0 - 12.0) ** 2.0
loss_task.backward()

print("\nTask 4 Weight (w):", w_task.item())
print("Task 4 Loss:", loss_task.item())
print("Task 4 Gradient (dL/dw):", w_task.grad.item())

# Mathematical Proof for Task 4:
# L(w) = (3w - 12)^2
# dL/dw = 2 * (3w - 12) * 3 = 6 * (3w - 12)
# When w = 2.0:
# dL/dw = 6 * (3(2) - 12) = 6 * (6 - 12) = 6 * (-6) = -36.0 ✅

