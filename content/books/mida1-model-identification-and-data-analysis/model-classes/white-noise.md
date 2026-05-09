---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-classes
chapter_title: Model classes
created_at: '2022-03-26T16:13:09.000000Z'
id: 110
priority: 0
slug: white-noise
title: White noise
type: page
updated_at: '2022-03-26T18:01:26.000000Z'
---

# White noise

A white noise is a sequence of uncorrelated random variables with the same mean and the same variance. A **stationary** stochastic process is called white noise if:
- $\mathbb{E}[e(t,s)]=\mu$ $\forall t$
- $Var[e(t,s)]=\mathbb{E}[(e(t,s)-\mu)^2]=\lambda^2$ $\forall t$
- $\gamma_e(\tau)=\mathbb{E}[(e(t,s)-\mu)(e(t-\tau,s)-\mu)]=0$ $\forall \tau\neq0$: this means that the values are completely uncorrelated for different time instants. This gives a white noise the caracteristic of having erratic realizations and unpredictability (fast sign changes around the mean)

We can then use a compact notation for the covariance function of a white noise:
$$
\gamma_e(\tau)= \begin{cases}
   \lambda^2 &\text{if } \tau=0 \newline
   0 &\text{if } \tau\neq0
\end{cases}
$$

We will denote: $e(t,s) \sim WN(\mu,\lambda^2)$.