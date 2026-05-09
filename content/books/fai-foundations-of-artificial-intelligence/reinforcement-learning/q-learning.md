---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: reinforcement-learning
chapter_title: Reinforcement learning
created_at: '2022-01-23T21:18:34.000000Z'
id: 94
priority: 2
slug: q-learning
title: Q-learning
type: page
updated_at: '2023-01-02T21:53:22.000000Z'
---

# Q-learning

We apply a policy to explore the environment in order to collect information and we keep a progressively updated estimation of the optimal Q-function applying a sample-based version of the Bellman equation.

At the beginning, the table $Q$ is initialized with random values and the at time $t$:

$$Q^\*(s,a) \gets (1-\alpha)Q^\*(s,a) + \alpha(r + \gamma \times max_{a' \in A}{Q^\*(s,a')})$$

Where $\alpha$ is the **learning rate**.