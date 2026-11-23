# Dynamic Programming in RL : Value Iteration & Policy Iteration
# Jab Environment ka Complete Model (Transition Probabilities & Rewards) pata ho, tab hum Dynamic Programming algorithms use karte hain.

# Markov Decision Process (MDP):
# MDP ko 5 elements se represent kiya jata hai: (S, A, P, R, γ)
# S → Set of States
# A → Set of Actions
# P → State Transition Probability P(s' | s, a)
# R → Reward Function R(s, a, s')
# γ → Discount Factor

# Value Function V(s):
# State 's' me hone par long-term expected reward.

# Bellman Optimality Equation for Value Iteration:
# V(s) = max_a Σ P(s'|s,a) * [ R(s,a,s') + γ * V(s') ]

# Value Iteration Algorithm:
# 1. State values V(s) ko zero initialize karo.
# 2. Loop chala kar har state ke liye max expected value update karo.
# 3. Tab tak repeat karo jab tak V(s) converge na ho jaye.

import random

# Grid Environment for Value Iteration
states = [(r, c) for r in range(3) for c in range(3)]
goal_state = (2, 2)
trap_state = (1, 1)
actions = [0, 1, 2, 3]  # 0: Up, 1: Down, 2: Left, 3: Right
gamma = 0.9

def get_next_state(s, a):
    r, c = s
    if a == 0: r = max(0, r - 1)
    elif a == 1: r = min(2, r + 1)
    elif a == 2: c = max(0, c - 1)
    elif a == 3: c = min(2, c + 1)
    return (r, c)

def get_reward(s):
    if s == goal_state: return 10
    if s == trap_state: return -10
    return -1

# Initialize Value Function V(s)
V = {s: 0.0 for s in states}

print("--- Running Value Iteration ---")
iterations = 20
for it in range(1, iterations + 1):
    new_V = V.copy()
    for s in states:
        if s == goal_state or s == trap_state:
            new_V[s] = get_reward(s)
            continue
        
        # Max value over all possible actions
        action_values = []
        for a in actions:
            next_s = get_next_state(s, a)
            r = get_reward(next_s)
            val = r + gamma * V[next_s]
            action_values.append(val)
        
        new_V[s] = max(action_values)
    V = new_V

print("Converged State Values V(s):")
for r in range(3):
    row_str = [f"{V[(r, c)]:.2f}" for c in range(3)]
    print(" | ".join(row_str))
