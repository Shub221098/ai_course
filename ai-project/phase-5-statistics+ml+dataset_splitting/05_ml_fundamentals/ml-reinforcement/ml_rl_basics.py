# Reinforcement Learning Basics : Reinforcement Learning (RL) Machine Learning ka ek branch hai jahan ek Agent environment me actions leta hai aur reward/penalty se seekhta hai.

# Reinforcement Learning Architecture
# 
#       ┌────────────────────────┐
#       │      Environment       │
#       └───────────┬────────────┘
#                   │ State (S) & Reward (R)
#                   ▼
#       ┌────────────────────────┐
#       │         Agent          │
#       └───────────┬────────────┘
#                   │ Action (A)
#                   ▼
#       (Environment updates state)


########## Core Terminology #─────────
# 1. Agent        → Decision Maker / Learner jo actions leta hai (e.g. Robot, Game Player AI).
# 2. Environment  → Agent ke aaspas ka world jiske saath agent interact karta hai.
# 3. State (S)    → Environment ki current situation ya position.
# 4. Action (A)   → Agent ke dwara liya gaya move ya choice.
# 5. Reward (R)   → Action lene par milne wala feedback (+ve reward for good action, -ve penalty for bad action).
# 6. Policy (π)   → Agent ki strategy jo decide karti hai ki kisi state me kaunsa action lena hai.
# 7. Discount (γ) → Future rewards ki importance (0 <= γ <= 1).

import random

# Basic Environment Class
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Starting state (position 0)
        self.goal_state = 5

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        # Action: 0 = Move Left, 1 = Move Right
        if action == 1:
            self.state += 1
        elif action == 0 and self.state > 0:
            self.state -= 1

        # Reward logic
        if self.state == self.goal_state:
            reward = 10
            done = True
        else:
            reward = -1
            done = False

        return self.state, reward, done

# Basic Random Agent
class RandomAgent:
    def choose_action(self):
        return random.choice([0, 1])  # 0: Left, 1: Right

# Simulation
env = SimpleEnvironment()
agent = RandomAgent()

state = env.reset()
print("--- Simple Agent-Environment Interaction Loop ---")
print(f"Starting State: {state}")

step_count = 0
done = False

while not done:
    action = agent.choose_action()
    action_name = "Right" if action == 1 else "Left"
    state, reward, done = env.step(action)
    step_count += 1
    print(f"Step {step_count}: Action='{action_name}' -> New State: {state}, Reward: {reward}")

print(f"\nGoal reached in {step_count} steps!")
