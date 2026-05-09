---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-classes
chapter_title: Model classes
created_at: '2022-03-26T16:26:22.000000Z'
id: 111
priority: 1
slug: moving-average-processes
title: Moving average processes
type: page
updated_at: '2022-03-28T19:54:58.000000Z'
---

# Moving average processes

Given a zero mean white noise $e(t) \sim WN(0,\lambda^2)$ we define the moving average  process of order $MA(n)$ as:
$$y(t)=c_0e(t)+c_1e(t-1)+...+c_ne(t-n)$$

Which is a linear combination of the past values of $e(t)$ from $t$ to $t-n$ with **real** parameters $c_0$,$c_1$,...,$c_n$.

## MA(n) weak characterization and stationarity
Given a moving average process $y(t) \sim MA(n)$ then we can easily demostrate that the mean function is always null:

$$
m_y(t)=\mathbb{E}[y(t)]=\mathbb{E}[c_0e(t)+c_1e(t-1)+...+c_ne(t-n)]=\newline
=c_0\mathbb{E}[e(t)]+c_1\mathbb{E}[e(t-1)]+...+c_n\mathbb{E}[e(t-n)]=0 \text{ because } e(t) \sim WN(0,\lambda^2)
$$

And the covariance function is (proof in notes 02 23 2022, step by step computation remembering that the white noise at two different time instant is completely uncorrelated):
$$
\gamma_y(\tau)= \begin{cases}
   (c_0^2+c_1^2+...+c_n^2)\lambda^2 &\text{if } \tau=0 \newline
   (c_0c_1+c_1c_2+...+c_{n-1}c_n)\lambda^2 &\text{if } \tau=\pm1 \newline
   \text{...}  \newline
   c_0c_n\lambda^2 &\text{if } \tau=\pm n \newline
   0 &\text{if } |\tau|>n
\end{cases}
$$
Which is time invariant so $y(t)$ **is stationary**.

## MA(inf) process
The class of models $MA(\infty)$ is a huge class which covers almost all SSP.

Considering a zero mean white noise $e(t) \sim WN(0,\lambda^2)$ the process $y(t) \sim MA(\infty)$ is:
$$y(t)=c_0e(t)+c_1e(t-1)+...+c_ie(t-i)+...=\sum_{i=0}^{+\infty}c_ie(t-i)$$
Which is an infinite sequence of random variables and the convergence to a proper random variance is not always guaranteed, only if:
$$\sum_{i=0}^{+\infty}c_i^2 < +\infty$$

A moving average process of order $n$ is equal to a $MA(\infty)$ process with $c_i=0$ for $i>n$.

### MA(inf) weak characterization and stationarity
The mean function of a well defined $MA(\infty)$ process is:
$$m_y(t)=\mathbb{E}[y(t)]=\mathbb{E}[\sum_{i=0}^{+\infty}c_ie(t-i)]=0$$

While the covariance function:
$$
\gamma(t,\tau)=\mathbb{E}[(y(t)-m_y(t))(y(t-\tau)-m_y(t-\tau))]=\newline
=\mathbb{E}[y(t)-y(t-\tau)]=\mathbb{E}[\sum_{i=0}^{+\infty}c_ie(t-i)\sum_{j=0}^{+\infty}c_je(t-\tau-j)]=\newline
[\text{Using linearity (well defined proces)}]\newline
=\sum_{i,j=0}^{+\infty}c_ic_j\mathbb{E}[e(t-i)e(t-\tau-j)]
$$
Since $\mathbb{E}[e(t-i)e(t-\tau-j)]=\gamma_e(t-i-(t-\tau-j))=\gamma_e(\tau+j-i)$ wich is always null except $\gamma_e(\tau+j-i)=\lambda^2$ for $i=j+\tau$. So:
$$\gamma(t,\tau)=\lambda^2\sum_{j=0}^{+\infty}c_jc_{j+\tau}$$

Which is time invariant so the process **is stationary**.

Note that for $\tau=0$ we obtain the variance $\gamma_y(0)=\lambda^2\sum_{j=0}^{+\infty}c_j^2$ and the conditions of convergence makes the process well defined because if $\sum_{i=0}^{+\infty}c_i^2 < +\infty$ then $\gamma_{y}(0) < +\infty$ and since the process is stationary then the covariance is bounded by the variance, this implies that $\gamma_y(\tau)$ is well defined for every $\tau$.

## Questions from past exams
##### Give the definition of an MA(inf) process e discuss the conditions under which it would be stationary and well defined. Prove the formula for the computation of the covariance function of an MA(inf) process. Explain why these processes are interesting to study AR and ARMA.
See above.

An $MA(\infty)$ process are interesting to study AR and ARMA processes because the steady state solution of the recursive euqation of those processes is an $MA(\infty)$ process with coefficients that are functions of the parameters of the recursive equation.

This implies also that the steady state solution is well defined when the condition under which a general MA(∞) process is well defined.