---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: reinforcement-learning
chapter_title: Reinforcement learning
created_at: '2022-01-23T21:14:52.000000Z'
id: 92
priority: 0
slug: introduction-and-markov-decision-proceses
title: Introduction and Markov decision proceses
type: page
updated_at: '2023-01-02T21:53:22.000000Z'
---

# Introduction and Markov decision proceses

Reinforcement learning deals with sequential decision making problems where an agent:

1. Observes the state of the environment
2. Acts on the environment performing some action
3. The environment evolves in a new state and provides the agent a **reward**, a feedback that the agent will use to decide if a specific action is good in a given state

The **goal** of the agent is: learning a **policy** (a prescription of actions, what action is best in every state) which maximizes the **total reward**.

## Markow decision processes
- **S state space**: the possible states
- **A action space**: the possible actions
- **P transition model**: which is the next state when a given action in  given state. We allow a the transition model to be a stochastic function. $P(s^{'}|s,a) \to [0,1]$
- **R reward function**: $R(s, a) \to \real$
- **$\gamma$ discount factor**: how much I care about the future rewards compared to the immediate rewards. $\gamma \in [0, 1]$
- **$\mu_0$ initial state distribution**: $\mu_0(S) \to [0,1]$ is the probability that the interactions starts in state S.

In this model we are in a single agent environment and the transition model satisfies the **Markov property**: the distribution of the next state depends only on the current state and the action, it is independent from the history of states actions observed so far.

**P and R are unknown**: in order to play in the environment the agent must interact and learn.

### Agent behaviour (policies)

The agent behaviour is modelled with the policy. A policy $\pi$ is a function taking a state and an action and giving a probability, $\pi \to [0, 1]$, such that $\pi(a|s)$ is the probability to perform action $a$ in state $s$.