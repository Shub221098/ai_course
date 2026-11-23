# Q-Learning : Q-Learning ek Model-Free, Off-Policy Reinforcement Learning algorithm hai.
# Iska goal hota hai har state-action pair ke liye optimal Q-Value (Quality value) learn karna.

# Q-Table Concept:
# Q-Table ek lookup matrix hota hai jahan:
# Rows    → States
# Columns → Actions
# Values  → Expected long-term return Q(s, a)

# Bellman Equation for Q-Learning:
# Q(s, a) = Q(s, a) + α * [ R + γ * max(Q(s', a')) - Q(s, a) ]
# Where:
# α (alpha) → Learning Rate (kitna naya reward Purane Q-value ko override karega)
# γ (gamma) → Discount Factor (Future rewards kitne important hain)
# R         → Immediate Reward
# s'        → Next State
# max(Q(s', a')) → Next state 's'' me sabse accha possible Q-value

# Exploration vs Exploitation (Epsilon-Greedy Strategy):
# Exploration (Random action)  → Naye moves explore karna (Probability ε)
# Exploitation (Best Q-value)  → Purane best action select karna (Probability 1 - ε)

import random

# GridWorld Environment (4x4)
class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.start_state = (0, 0)
        self.goal_state = (size - 1, size - 1)
        self.traps = [(1, 1), (2, 2)]
        self.state = self.start_state
        self.actions = [0, 1, 2, 3]  # 0: Up, 1: Down, 2: Left, 3: Right

    def reset(self):
        self.state = self.start_state
        return self.state

    def step(self, action):
        r, c = self.state

        if action == 0:   # Up
            r = max(0, r - 1)
        elif action == 1: # Down
            r = min(self.size - 1, r + 1)
        elif action == 2: # Left
            c = max(0, c - 1)
        elif action == 3: # Right
            c = min(self.size - 1, c + 1)

        new_state = (r, c)
        self.state = new_state

        if new_state == self.goal_state:
            reward = 10
            done = True
        elif new_state in self.traps:
            reward = -10
            done = True
        else:
            reward = -1
            done = False

        return new_state, reward, done


# Q-Learning Agent
class QLearningAgent:
    def __init__(self, states, actions, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        
        # Q-Table Initialization: Q(state, action) = 0.0
        self.q_table = {state: {a: 0.0 for a in actions} for state in states}

    def choose_action(self, state):
        # Epsilon-Greedy Choice
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        else:
            q_vals = self.q_table[state]
            max_q = max(q_vals.values())
            best_actions = [a for a, q in q_vals.items() if q == max_q]
            return random.choice(best_actions)

    def learn(self, state, action, reward, next_state, done):
        current_q = self.q_table[state][action]
        max_next_q = 0.0 if done else max(self.q_table[next_state].values())
        
        # Q-Learning Bellman Update
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[state][action] = new_q


# Training Loop
env = GridWorld(size=4)
all_states = [(r, c) for r in range(4) for c in range(4)]
agent = QLearningAgent(states=all_states, actions=[0, 1, 2, 3])

episodes = 500

print("--- Training Q-Learning Agent ---")
for ep in range(1, episodes + 1):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward

    if ep % 100 == 0:
        print(f"Episode {ep}/{episodes} | Total Reward: {total_reward}")

# Testing Learned Policy
print("\n--- Testing Optimal Learned Path ---")
agent.epsilon = 0.0  # Exploitation only
state = env.reset()
path = [state]
done = False

while not done and len(path) < 15:
    action = agent.choose_action(state)
    next_state, reward, done = env.step(action)
    path.append(next_state)
    state = next_state

print("Path chosen by Q-Learning Agent:", path)
