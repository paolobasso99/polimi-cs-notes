---
book_slug: ml-machine-learning-Zyp
book_title: ML Machine Learning
created_at: '2023-06-06T22:59:28.000000Z'
id: 196
priority: 6
slug: markov-decision-processes
title: Markov Decision Processes
type: page
updated_at: '2023-06-07T08:56:32.000000Z'
---

# Markov Decision Processes

## Questions
### Describe the properties of the Bellman operators. (1)
...

### Describe the policy iteration technique for control problems on Markov Decision Processes. (3)
### Describe the value iteration algorithm and its properties. Does the algorithm always return the optimal policy? (2)
### Describe and compare the Value Iteration algorithm and the Policy Iteration algorithm. (2)
Policy iteration and value iteration are two Dynamic Programming approaches to solve an MDP, i.e. finding the optimal policy $\pi^*$.

We use Dynamic Programming because the brute force way of solving MDPs in which we enumerate all possible policies and perform policy evaluation on all of them is computationally unfeasible as the number of policies grows exponentially: $|A|^{|S|}$.

Dynamic programming is a general method for solving in an efficient way problems with the following characteristics:
- The problem can be decomposed into sub-problems
- The sub-problems repeats many times so we can reuse the computations

It can be applied to solving MDPs because the Bellman equation gives the recursive decomposition and the sub-problems repeats many times.

#### Policy iteration
Policy iteration has two steps: policy evaluation in which we evaluate the current policy and policy improvement in which we improve greedily the current policy.

##### Policy evaluation
Performing policy evaluation means computing the state-value function $V^\pi$. From the Bellman equations:
$$
\begin{align*}
    V^\pi(s) &= \sum_{a \in A} \pi(a|s) \sum_{s' \in S}P(s,a,s')[R(s,a,s') + \gamma V^\pi(s')] \\
    &= \sum_{a \in A} \pi(a|s) [R(s,a) + \gamma\sum_{s' \in S}P(s,a,s') V^\pi(s')]
\end{align*}
$$
Which results in a system of $|S|$ linear equations with a close form solution:
$$
V^\pi = (I- \gamma P^\pi)^{-1} R^\pi
$$
However inverting the matrix is a costly operation ($O(n^3)$) therefore we use a iterative algorithm:
$$
V_{k+1}(s) \leftarrow \sum_{a \in A} \pi(a|s) [R(s,a) + \gamma\sum_{s' \in S}P(s,a,s') V_k^\pi(s')]
$$

##### Policy improvement
In a given state $s$ we can improve the policy $\pi$ by acting greedily:
$$
\pi'(s) = \argmax_{a \in A} Q^\pi(s,a)
$$
The policy improvement theorem states that if $\pi$ and $\pi'$ are two deterministic policies and $Q^\pi(s, \pi'(s)) \ge V^\pi(s), \forall s \in S$ then policy $\pi'$ must be as good as, or better, than $\pi$:
$$
V^{\pi'}(s) \ge V^\pi(s), \forall s \in S
$$
This means that, for example, if we change the policy only in one state $s$ selecting the greedy action and leaving the same policy in every other state then the new policy will have a better state value function in $s$ and the same state value function in all the other states (improving in one state guarantees not deteriorating in the other states).

If the improvement stops ($V^{\pi'} = V^\pi$) then we found the optimal policy.

#### Value iteration
Another algorithm to find the optimal policy is Value iteration. It is based on an iterative application of the Bellman optimality backup so, unlike policy iteration, there is no explicit policy and intermediate value functions may not correspond to any policy.

Value iteration works by directly evaluating the optimal policy, i.e. computing $V^\*(s)$, using a repeated application of the bellman optimality equation: 
$$
V_{k+1}(s) \leftarrow \max_{a \in A} \lbrace R(s,a) + \gamma \sum_{s' \in S} P(s,a,s') V_k(s') \rbrace
$$
Once we have found the value function $V^\*(s)$ corresponding to the optimal policy $\pi^\*$ we can easily recover the optimal policy which will be the greedy one with respect to $V^\*(s)$.

#### Comparison
In policy iteration, at each step, policy evaluation is run until convergence, then the policy is updated and the process repeats.

In contrast, Value Iteration first computes the optimal value function and then does only one final policy improvement step which extracts the optimal policy.

### Describe which methods can be used to compute the value function Vπ of a policy π in a discounted Markov Decision Process. (1)
See the policy evaluation section in the previous question.