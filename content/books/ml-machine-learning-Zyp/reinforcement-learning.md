---
book_slug: ml-machine-learning-Zyp
book_title: ML Machine Learning
created_at: '2023-06-07T08:56:43.000000Z'
id: 197
priority: 7
slug: reinforcement-learning
title: reinforcement learning
type: page
updated_at: '2023-06-08T14:37:13.000000Z'
---

# reinforcement learning

## Questions
### Describe and compare Q-learning and SARSA. (4)
### Describe the difference between on-policy and off-policy reinforcement learning techniques. Make an example of an on-policy algorithm and an example of an off-policy algorithm. (2)
#### On-policy vs Off-policy
On-policy control methods find the optimal policy improving the one used for sampling while off-policy methods learn the optimal policy while following a different sampling policy, which is useful because it allows:
- to learn observing other agents
- re-use experience generated from old policy
- can be applied in situations where the policy is not influenceable
- can learn multiple policies while following the same one 

#### SARSA
SARSA is an on-policy temporal difference control method. It follows the general pattern of generalized policy iteration, using TD for the evaluation part. In particular, for an on-policy method we must estimate $Q_\pi ( s, a )$ for the current behavior policy $\pi$ and for all states $s$ and actions $a$.

SARSA first evaluates the current policy using temporal difference:
$$
Q(s, a) \leftarrow Q(s,a) + \alpha[R(s,a) + \gamma Q(s', a') - Q(s,a)]
$$ 
Then improves upon that policy using an $\epsilon$-greedy policy improvement:
$$
\pi(a|s) = \begin{cases}
    1-\epsilon, \text{ if } a = \argmax_{a' \in A} Q(s,a') \\\\
    \frac{\epsilon}{|A|-1}, \text{ otherwise}
\end{cases}
$$

SARSA converges to the optimal action-value function under the following conditions:
- GLIE sequence of policies $\pi_t(s,a)$
  - All state–action pairs are explored infinitely many times
  - The policy converges on a greedy policy (at a certain timestep we must have $\epsilon = 0$)
- Robbins–Monro sequence of step–sizes $\alpha_t$

#### Q-Learning
Q-learning is an off-policy temporal difference control method defined by:
$$
Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a' \in A} Q(s', a') - Q(s,a)]
$$

In this case, the learned action-value function directly approximates the optimal action-value function, independently of the policy being followed. This means that Q-learning will find the optimal policy from experience sampled from another, different, policy.


### Describe and compare Monte Carlo and Temporal Difference for model-free policy evaluation. (3)
#### Monte Carlo Prediction (policy evaluation)
In policy evaluation we want to compute the state value function of a given policy $V^\pi(s)$, where the value of a state is the expected return starting from a state. An obvious way to estimate it from experience is simply to average the returns observed after visits to that state. This idea underlines all Monte Carlo policy evaluation methods.

The first-visit Monte Carlo policy evaluation estimates $v_\pi(s)$ as the average returns following first visits to $s$, every visit averages the returns following all the visits to $s$. Both converges to $v_\pi(s)$ as the number of visits (or first visits) goes to infinity.

Monte Carlo methods use full episodes. This means that the averages are computed using a complete and terminate episode.
However, they can be implemented incrementally with the following update rule:
$$
\begin{align*}
    N(s_t) &\leftarrow N(s_t) + 1 \\\\
    V(s_t) &\leftarrow V(s_t) + \frac{1}{N(s_t)}(v_t - V(s_t))
\end{align*}
$$
Or:
$$
V(s_t) \leftarrow V(s_t) + \alpha (v_t - V(s_t))
$$
Monte Carlo first-visit is completely unbiased but suffers a high variance, while every-visit is biased (since the same state is considered more time).

#### Temporal Difference Prediction (policy evaluation)
Roughly speaking, Monte Carlo methods wait until the return following the visit is known, then use that return as a target for $V(s_t)$. TD methods need to wait only until the next time step. At time $t+1$ they immediately form a target and make a useful update using the observed reward $r_{t+1}$ and the estimate $V^\pi(s_{t+1})$. The simplest TD method makes the update:
$$
V(s_t) \leftarrow V(s_t) + \alpha [r_{t+1} + \gamma V(s_{t+1}) - V(s_t)]
$$
immediately on transition to $s_{t+1}$ and receiving $r_{t+1}$. The target of Monte Carlo update is $v_t$ while of TD is $r_{t+1} + \gamma V(s_{t+1})$. This method is called TD(0) or one-step TD.
Because TD(0) bases its update in part on an existing estimate ($V(s_{t+1})$), we say this is a bootstrapping method.

The advantage of TD methods over Monte Carlo ones is that they are naturally online and fully incremental. This means that we do not need to have full episodes to because we do not need to know the full sum of discounted rewards after visiting one state but we only need to know one timestep.

TD exploits the Markov property while MC does not as it uses full episodes.

#### Bias Variance comparison
MC has an high variance but zero bias (first-visit), it has good convergence properties, works well with function approximation and is not very sensitive to the initial values.

TD has low variance but high bias, it is usually more efficient than MC but it has problems with functional approximation and it is more sensitive to the initial values.

### Explain what are eligibility traces and describe the TD(λ) algorithm. (3)
TD($\lambda$) is a generalization and unification of temporal difference and MC methods, where $\lambda$ indicates the use of eligibility traces. When TD methods are augmented  with eligibility traces they produce a family of methods spanning a spectrum that has MC methods at one end ($\lambda=1$) and one-step TD at the other ($\lambda = 0$).

There is another way to unify TD and MC methods using the concept of n-steps returns, for which the n-step TD uses the obtained rewards for n-steps instead of a single one, before using the estimate of the state-value function:

$$
\begin{align*}
    v_t^{(n)} &= r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + ... + \gamma^{n-1}r_{t+n} + \gamma^n V(s_{t+n}) \\\\
    V(s_t) &\leftarrow V(s_t) + \alpha (v_t^{(n)} - V(s_t))
\end{align*}
$$

In this framework TD(0) is uses the 1-step return while MC uses $\infty$-step returns.

What eligibility traces offers beyond these is an elegant algorithmic mechanism with significant computational advantages.
The primary computational advantage of eligibility traces over $n$-step methods is that only a single trace vector is required rather than a store of the last $n$ feature vectors.
Learning also occurs continually and uniformly in time rather than being delayed and then catching up at the end of the episode. In addition learning can occur and affect the behavior immediately after a state is encountered rather than being delayed $n$ steps.

The $\lambda$-return $v_t^\lambda$ combines all $n$-steps returns $V_t^(n)$ using a weight:
$$
v_t^\lambda = (1-\lambda)\sum_{n=1}^\infty \lambda^{n-1} v_t^{(n)}
$$
The forward view has the update rule:
$$
V(s_t) \leftarrow V(s_t) + \alpha (v_t^\lambda - V(s_t))
$$
Forward view uses th feature to compute $v_t^\lambda$ and, therefore, can only be used with complete episodes (like MC).

However, the backward view using eligibility traces implementation updates the weight vector on every step of an episode instead only at the end. Moreover, the computations are equally distributed in time rather than all at the end of the episode. Finally, it can be applied to continuing problems rather than just to episodic problems.

Eligibility traces are short-term memory vectors which assist the learning process affecting the weight vector. They are a mechanism to quantify how much a state affected the returns.

They combine two heuristics:
- Frequency heuristic: assign credit to the most frequent states
- Recency heuristics: assign credit to the most recent states

$$
\begin{align*}
    e_0 (s) &= 0 \\\\
    e_{t}(s) &= \gamma \lambda e_{t-1}(s) + \mathbf{1}(s = s_t)
\end{align*}
$$
The formula means that the eligibility trace is incremented on each time step for the state $s_t$ and then fades away by $\gamma \lambda$. The update rule using eligibility traces is:
$$
V(s_t) \leftarrow V(s_t) + \alpha e_t(s) \delta_t(s)
$$
Where $\delta_t(s)$ is the TD-error.

When $\lambda = 0$, only the current state is updated, which is equivalent to the TD(0) update:
$$
\begin{align*}
    e_t(s) &= \mathbf{1}(s=s_t) \\\\
    V(s_t) &\leftarrow V(s_t) + \alpha \delta_t
\end{align*}
$$

When $\lambda=1$ the sum of TD errors telescopes into MC error. This means that TD(1) is roughly equivalent to every visit MC but, since the update is online, then TD(1) may have different total update to MC.

### Describe the two problems tackled by Reinforcement Learning (RL): prediction and control. Describe how the Monte Carlo RL technique can be used to solve these two problems. (1)
...