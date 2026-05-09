---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: frequency-domain-analysis
chapter_title: Frequency Domain Analysis
created_at: '2022-03-26T20:44:02.000000Z'
id: 120
priority: 1
slug: frequency-domain-and-spectrum
title: Frequency domain and spectrum
type: page
updated_at: '2022-03-28T20:05:22.000000Z'
---

# Frequency domain and spectrum

The **frequency domain** is another way to obtain the weak (wide sense) characterization of a **stationary** stochastic process.

Consider a stationary stochastic process $y(t)$:
- $\mathbb{E}[y(t)]=m_y \text{ } \forall t$
- $\gamma_y(\tau)=\mathbb{E}[(y(t)-m_y)(y(t-\tau)-m_y)]=m_y$

Then we define the **spectrum** as the *discrete Fourier transform* of the covariance function $\gamma_y(\tau)$ of the stationary stochastic process $y(t)$:
$$\Gamma(\omega):=\sum_{\tau=-\infty}^{+\infty}{\gamma_y(\tau)e^{-j\omega\tau}}$$

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/spUNpyF58BY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Example: spectrum of the white noise
Given the white noise $e(t) \sim EN(\mu,\lambda^2)$ which has the covariance function:
$$
\gamma_e(\tau)= \begin{cases}
   \lambda^2 &\text{if } \tau=0 \newline
   0 &\text{if } \tau\neq0
\end{cases}
$$
The spectrum is:
$$\Gamma(\omega)=\sum_{\tau=-\infty}^{+\infty}{\gamma_e(\tau)e^{-j\omega\tau}}=\gamma_e(\tau)e^{-j\omega0}=\lambda^2$$

### Example: spectrum of MA(1) process
Consider the process $y(t)=e(t)+ce(t-1)$, his covariance function is:
$$
\gamma_y(\tau)= \begin{cases}
   (1^2+c^2)\lambda^2 &\text{if } \tau=0 \newline
   (1 \times c)\lambda^2 &\text{if } \tau=\pm1 \newline
   0 &\text{if } \tau\neq0
\end{cases}
$$
The spectrum of the process is then:
$$\Gamma(\omega)=\sum_{\tau=-\infty}^{+\infty}{\gamma_y(\tau)e^{-j\omega\tau}}=(1+c^2)\lambda^2e^{-j\omega0}+c\lambda^2e^{-j\omega1}+c\lambda^2e^{-j\omega(-1)}=\lambda^2[1+c^2+c(e^{-j\omega}+e^{j\omega})]$$
Since we know that: $e^{j\omega}=cos(\omega)+jsin(\omega)$ and then $e^{-j\omega}=cos(\omega)-jsin(\omega)$
We can rewrite the spectrum as: $\Gamma(\omega)=\lambda^2(1+c^2+2cos(\omega))$

## Properties of the spectrum
The properties of the spectrum are inherited from the properties of $\gamma_y(\tau)$.

1. $\Gamma(\omega) \in \mathbb{R} \text{ } \forall\omega$ the spectrum is **real valued**. This happens, intuitivelly, because since $\gamma_y(\tau)$ = $\gamma_y(-\tau)$ then the immaginary parts cancel out.
2. $\Gamma(\omega) \ge 0  \text{ } \forall\omega$ the spectrum is **positive**.
3. $\Gamma(\omega) = \Gamma(-\omega)  \text{ } \forall\omega$ the spectrum is an **even function**.
4. $\Gamma(\omega) = \Gamma(\omega +2k\pi)  \text{ } \forall\omega,k=0,\pm1,...$ the spectrum is **periodic with period $2\pi$**.

## Spectrum of output of digital filters
Given the well defined stationary stochastic process $y(t)=W(z)v(t)=\frac{A(z)}{B(z)}v(t)$ we can compute the covarianca function and then the spectrum.

There exists an easier way... an important theorem states that:
$$\Gamma_y(\omega)=|W(e^{jw})|^2\Gamma_v(\omega)$$
Which means that the spectrum of the output is the spectrum of the input multiplied by the transfer function evaluated for $z=e^{jw}$ absolute value square.

### Example: spectrum of MA(1) using digital filter th.
Given the $MA(1)$ process $y(t)=e(t)+ce(t-1)=(1+cz^{-1})e(t)$ with $e(t) \sim EN(\mu,\lambda^2)$ the spectrum of the process is:
$$\Gamma_y(\omega)=|W(e^{jw})|^2\Gamma_e(\omega)=|1+ce^{-jw}|^2\lambda^2=\lambda^2(1+c^2+2cos(\omega))$$

## Questions from past exams
##### What is the spectrum of a stationary stochastic process and explain the most important properties.
See above.

##### Give the definition of spectral density of a stationary stochastic process. Then, prove that the spectral density of the sum of two uncorrelated stationary processes is equal to the sum of the spectral densities.
As far as I know we did not see this proof in class. Probably starting from the definition it can be worked out.