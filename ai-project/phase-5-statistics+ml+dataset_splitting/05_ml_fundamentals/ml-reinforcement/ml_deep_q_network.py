# Deep Q-Network (DQN) : Deep Q-Network tabular Q-Learning ko Neural Networks ke saath combine karta hai.

# Tabular Q-Learning ki Limitations:
# Jab State Space bahut bada ho (jaise Video Games me pixels 1080p, ya Robotics me continuous states), 
# tab Q-Table banana impossible ho jata hai kyunki billions of states store nahi ki ja sakti.

# DQN ka Solution:
# Q-Table ko ek Neural Network (Function Approximator) se replace kar do!
# Input  → State (S)
# Output → Every action 'a' ki Q-Value Q(S, a; θ)

# DQN ki 2 Sabse Important Techniques:

# 1. Experience Replay (Memory Buffer):
# Agent ke past experiences (state, action, reward, next_state, done) ko ek Replay Buffer me store karte hain.
# Training ke me memory se RANDOM samples pick karke network train karte hain.
# Advantage → Sequential data ka correlation break hota hai aur training stable hoti hai.

# 2. Target Network:
# 2 Neural Networks maintenance kiye jate hain:
# - Main Q-Network (θ)   → Har step me update hota hai.
# - Target Network (θ⁻)  → Periodic steps (e.g. 1000 steps) ke bad Main Network se sync hota hai.
# Advantage → Target instability/chasing moving target problem fix hoti hai.

import random

# Replay Buffer Implementation (Pure Python)
class ReplayBuffer:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.buffer = []

    def push(self, state, action, reward, next_state, done):
        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)  # Remove oldest experience
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size=32):
        return random.sample(self.buffer, min(batch_size, len(self.buffer)))

    def __len__(self):
        return len(self.buffer)


# Conceptual DQN Agent Overview
print("--- Deep Q-Network (DQN) Architecture Demo ---")

memory = ReplayBuffer(capacity=100)

# Simulate storing experiences in memory
for step in range(1, 10):
    dummy_state = (step, step % 2)
    dummy_action = step % 4
    dummy_reward = 1.0 if step == 9 else -0.1
    dummy_next_state = (step + 1, (step + 1) % 2)
    dummy_done = (step == 9)
    
    memory.push(dummy_state, dummy_action, dummy_reward, dummy_next_state, dummy_done)

print(f"Total Experiences stored in Replay Buffer: {len(memory)}")

# Sample a random mini-batch for Neural Network Training
batch = memory.sample(batch_size=3)
print("\nSampled Mini-Batch for Training:")
for exp in batch:
    print(" (S, A, R, S', Done):", exp)
