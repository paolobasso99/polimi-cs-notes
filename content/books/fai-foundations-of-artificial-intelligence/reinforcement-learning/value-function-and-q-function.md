---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: reinforcement-learning
chapter_title: Reinforcement learning
created_at: '2022-01-23T21:18:12.000000Z'
id: 93
priority: 1
slug: value-function-and-q-function
title: Value function and Q-function
type: page
updated_at: '2023-01-02T21:53:22.000000Z'
---

# Value function and Q-function

The total reward is typically defined s the **expected discounted cumulative reward**.  We can define the **value function** $V^\pi (s)$ of policy $\pi$ in state $s$:

$$V^\pi (s) = \mathbb{E}[\sum_{t=0}^{+\infty}{\gamma^t R(s_t, a_t)} \mid s_0 = s, a_t \in \pi(., s_t)]$$

- $\mathbb{E}$ because it is expected (stochastic)
- $\sum_{t=0}^{+\infty}$ because it is a cumulative reward on a sequence of interactions
- $\gamma^t$ because it is discounted. $\gamma \in [0,1]$ so $\gamma^t$ gets smaller and smaller
- $R(s_t, a_t)$ is the reward performing $a_t$ is $s_t$

The **state action function** $Q^\pi(s,a)$ is defined as:

$$Q^\pi (s,a) = \mathbb{E}[\sum_{t=0}^{+\infty}{\gamma^t R(s_t, a_t)} \mid s_0 = s, a_0=a, a_t \in \pi(., s_t)]$$

Note that: $V^\pi (s) =\mathbb{E}[\sum_{a \in A} \pi(a,s)Q^\pi (s,a)]$

Reinforcement learning assumes that $Q^\pi (s,a)$ is represented as a table but the number of possible inputs can be huge! We cannot afford to compute an exact $Q^\pi (s,a)$ table.

### Policy optimality

A policy $\pi^*$ is optimal if and only if it maximizes the expected discounted cumulative reward:

$$\pi^\* \in argmax_\pi V^\pi(s)$$

Therefore, we denote:
- $V^\*(s):=V^{\pi^\*}(s)$ the value function of the optimal policy
- $Q^\*(s,a):=Q^{\pi^\*}(s,a)$ the value action function of the optimal policy

The optimal action to be played in a gives state s, given by $\pi^\*(s)$, can be defined in terms of the optimal q-function:
$$\pi^\*(s) \in argmax_a Q^\*(s,a)$$

In other words, we fix the state and then find the optimal action that maximizes the q-function.

### Bellman equation

It is a **recursive** way to define the optimal q-function.

$$Q^\*(s,a) = R(s,a) + \gamma \sum_{s' \in S}{P(s'|s, a)max_{a' \in A}{Q^\*(s',a')}}$$

The maximum amount of cumulative reward that you can collect starting from a state $s$ and an action $a$ is the immediate reward $R(s,a)$ plus the discount factor times "what you will collect by playing an optimal policy starting from the next state".