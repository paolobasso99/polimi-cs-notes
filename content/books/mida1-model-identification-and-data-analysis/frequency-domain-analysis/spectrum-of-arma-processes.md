---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: frequency-domain-analysis
chapter_title: Frequency Domain Analysis
created_at: '2022-03-26T22:16:31.000000Z'
id: 123
priority: 4
slug: spectrum-of-arma-processes
title: Spectrum of ARMA processes
type: page
updated_at: '2022-03-28T20:30:50.000000Z'
---

# Spectrum of ARMA processes

Given the $ARMA$ process $y(t)=\frac{C(z)}{A(z)}e(t)$ with $e(t) \sim WN(0,\lambda^2)$ the spectrum is given by:
$$\Gamma_y(\omega)=\mid\frac{C(e^{j\omega})}{A(e^{j\omega})}\mid^2\times\lambda^2$$
Since both $C(z)$ and $A(z)$ are polynomial the result is a **rational spectrum** (ratio of polynomials of $e^{j\omega}$):

$$\Gamma_y(\omega)=\frac{\beta_0+\beta_1e^{j\omega}+\beta_2e^{2j\omega}+...}{\alpha_0+\alpha_1e^{j\omega}+\alpha_2e^{2j\omega}+...}$$

**THEOREM**

If the spectrum of a stationary stochastic process is rational then the process is an $ARMA$ process.

Let $y(t)$ be a SSP with rational spectrum. There exists a digital filter $W(z)$ and a white noise $e(t)$ with suitable mean $\mu$ and variance $\lambda^2$ such that $y(t)=W(z)e(t)$.

The **representation is not unique**: if the process $y(t)$ is an $ARMA$ process then there are an infinite moltitude of transfer function $W(z)$ and white noises $e(t)$ such that $y(t)=W(z)e(t)$.

## Canonical representation of ARMA processes (Spectral Factorization Theorem)
Let $y(t)$ be a SSP with rational spectrum. There exists a **unique** $ARMA$ representation, that is a unique pair of transfer function $W(z)=\frac{C(z)}{A(z)}$ and white noise $e(t)$, such that:
1. $C(z)$ and $A(z)$ are **monic**: the coefficient of the term with the highest power is 1
2. $C(z)$ and $A(z)$ have **null relative degree**: the highest power in the numerator is the same of the one in the denominator
3. $C(z)$ and $A(z)$ are **coprime**: they do not have common factors
4. Poles have absolute values < 1 and zeros have absolute values less or equal than 1.
$$
|poles|<1\newline
|zeros|\le1
$$

### How to find the canonical representation
Given an $ARMA$ process $y(t)=W(z)e(t)$ with $e(t) \sim WN(\mu,\lambda^2)$ the following operations are applicable in order to find the canonical representation:
1. With $\alpha \in \mathbb{R}$:
$$
\bar{W(z)}=\alpha W(z)\newline
\bar{e(t)}=\frac{1}{\alpha}e(t) \sim WN(\frac{\mu}{\alpha}, \frac{\lambda^2}{\alpha^2})
$$
2. With $k=\pm1,\pm2,...$:
$$
\bar{W(z)}=z^{-k} W(z)\newline
\bar{e(t)}=z^{k}e(t) \sim WN(\mu, \lambda^2)
$$
3. With $p$ a pole of $W(z)$:
$$
\bar{W(z)}=W(z)\frac{z-p}{z-p}\newline
\bar{e(t)}=e(t) \sim WN(\mu, \lambda^2)
$$
4. We can use the all pass filter to move a zero/pole which is outside the immaginary unit disk to inside it. From:
$$
W(z)=\frac{C(z)}{A(z)}=\frac{(z-q_1)(z-q_2)...(z-q_n)}{(z-p_1)(z-p_2)...(z-p_m)}=W_1(z)(z-q)
$$
Then:
$$
y(t)=W_1(z)(z-\frac{1}{q})\frac{z-q}{z-\frac{1}{q}}e(t)
$$
Which results in:
$$
\bar{W(z)}=W_1(z)(z-\frac{1}{q})\newline
\bar{e(t)}=\frac{z-q}{z-\frac{1}{q}}e(t) \sim WN(-q\mu, q^2\lambda^2)
$$

## Questions from past exams
##### By means of an example, show that the ARMA representation of a stationary stochastic process with rational spectral density is not unique. Enunciate then the Spectral Factorization Theorem and give some comments.
See above.

##### Prove that the steady state output of an all-pass filter feb by a white noise Is a white noise itself. Illustrate why all-pass filters are useful to obtain canonical forms of ARMA.
The all pass filter is $\frac{z-q}{z-\frac{1}{q}}$. See above on why they are useful to obtain the canonical form.

Given the white noise $e(t) \sim WN(\mu,\lambda^2)$, if we applu an all pass filter to it:
$$\bar{e}(t)=\frac{z-q}{z-\frac{1}{q}}e(t)$$
It is well defined for $|q|>1$ and it is still a white noise since:
$$
\Gamma_{\bar{e}(t)}(\omega)=\mid \frac{e^{j\omega}-q}{e^{j\omega}-\frac{1}{q}} \mid^2 \Gamma_{e(t)}(\omega)=\frac{e^{j\omega}-q}{e^{j\omega}-\frac{1}{q}} \frac{e^{-j\omega}-q}{e^{-j\omega}-\frac{1}{q}}  \lambda^2=
$$
$$
=\frac{1+q^2-q(e^{j\omega}+e^{-j\omega})}{1+\frac{1}{q^2}-\frac{1}{q}(e^{j\omega}+e^{-j\omega})} \lambda^2=q^2\frac{1+\frac{1}{q^2}-\frac{1}{q}(e^{j\omega}+e^{-j\omega})}{1+\frac{1}{q^2}-\frac{1}{q}(e^{j\omega}+e^{-j\omega})} \lambda^2=
$$
$$
=q^2\lambda^2
$$
Which is constant $\forall \omega$ (as the white noise).

For the mean:
$$\bar{e}(t)=\frac{z-q}{z-\frac{1}{q}}e(t)$$
$$\bar{e}(t+1)-\frac{1}{q}\bar{e}(t)=e(t+1)-qe(t)$$
$$\mathbb{E}[\bar{e}(t+1)-\frac{1}{q}\bar{e}(t)]=\mathbb{E}[e(t+1)-qe(t)]$$
$$m_{\bar{e}}-\frac{1}{q}m_{\bar{e}}=\mu-q\mu$$
$$m_{\bar{e}}=\frac{1-q}{1-\frac{1}{q}}\mu=-q\frac{1-\frac{1}{q}}{1-\frac{1}{q}}\mu=-q\mu$$