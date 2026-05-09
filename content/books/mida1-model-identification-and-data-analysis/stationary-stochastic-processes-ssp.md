---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
created_at: '2022-03-26T15:33:16.000000Z'
id: 109
priority: 2
slug: stationary-stochastic-processes-ssp
title: Stationary stochastic processes (SSP)
type: page
updated_at: '2022-03-26T18:01:26.000000Z'
---

# Stationary stochastic processes (SSP)

A stochastic process $v(t,s)$ is stationary if:
1. $m_v(t)=m_v$ $\forall{t}$: the mean function is a constant
2. $\gamma_v(t,\tau ) = \gamma_v(\tau )$ $\forall{t}$: the covariance is function only of the time lag $\tau$, not of the time $t$.
In summary the partial indicators of SSP are **time invariant**.

Intuitively this definition respond to the question: what does it mean for a random process to remain the “same” over time? Obviously, the exact values will be different, since the process is random. However a SSP has the partial indicators that are time invariant and so the characterization of the process does not change with time.

## Importance of SSPs
- SSPs are typical of many practical situations
- SSPs are easier to study
- Non stationarity typically arises as an additive contribution: $v(t,s) = v_{SSP}(t,s) + v_{NSSP}(t,s)$ so the study of SSPs is useful also when modeling non stationary processes.

## Questions from past exams
##### Specify which conditions the mean function and the covariance function must satisfy to say that the process is (weak-sense) stationary. Explain intuitively what stationarity means.
See above.

##### Let $y_1(t)$ and $y_2(t)$ be two stationary stochastic processes that are uncorrelated each other (that is, $\mathbb{E}[(y_1(t) − m_{y_1}(t))(y_2(r) − m_{y_2}(t))] = 0$, $\forall t, r$). Prove that the process $𝑧(𝑡) = 𝑦_1(𝑡) + 𝑦_2(𝑡)$ is stationary too.
In order for $𝑧(𝑡) = 𝑦_1(𝑡) + 𝑦_2(𝑡)$ to be stationary then:
1. $m_z(t)=m_z$ $\forall{t}$
2. $\gamma_z(t,\tau ) = \gamma_z(\tau )$ $\forall{t}$

If we compute the mean function of $z$:
$$m_z(t)=\mathbb{E}[z(t)]=\mathbb{E}[𝑦_1(𝑡) + 𝑦_2(𝑡)]=\mathbb{E}[𝑦_1(𝑡)]+\mathbb{E}[𝑦_2(𝑡)]=m_{y_1}+m_{y_2}=m_z$$

While the covariance function:
$$\gamma_z(t,\tau)=\mathbb{E}[(z(t)-m_z)(z(t-\tau)-m_z)]= \newline
\mathbb{E}[((𝑦_1(𝑡)-m_{y_1})+(𝑦_2(𝑡)-m_{y_2}))((𝑦_1(𝑡-\tau)-m_{y_1})+(𝑦_2(𝑡-\tau)-m_{y_2}))]= \newline
\mathbb{E}[(𝑦_1(𝑡)-m_{y_1})(𝑦_1(𝑡-\tau)-m_{y_1})+(𝑦_2(𝑡-\tau)-m_{y_2})(𝑦_2(𝑡-\tau)-m_{y_2})] = \newline
\gamma_{y_1}(\tau)+\gamma_{y_2}(\tau)=\gamma_z(\tau)
$$
Which is time invariant