---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-classes
chapter_title: Model classes
created_at: '2022-03-26T20:10:57.000000Z'
id: 118
priority: 7
slug: non-zero-mean-arma
title: Non zero mean ARMA
type: page
updated_at: '2022-03-26T20:24:40.000000Z'
---

# Non zero mean ARMA

Consider the ARMA process $y(t)=\frac{C(z)}{A(z)}e(t)$ where is a **non zero mean** white noise$e(t) \sim WN(\mu,\lambda^2)$.

## Gain theorem
If $W(z)=\frac{C(z)}{A(z)}$ is assintotically stable, then:
$$m_y=\mathbb{E}[y(t)]=\frac{C(1)}{A(1)}\mu$$

## Unbiased processes
Considering $y(t)$ we can defined the unbiased processes as:
$$\tilde{y}(t)=y(t)-m_y$$
$$\tilde{e}(t)=e(t)-\mu$$
which are both zero mean processes:
$$\mathbb{E}[\tilde{y}]=\mathbb{E}[y(t)-m_y]=m_y-m_y=0$$
$$\mathbb{E}[\tilde{e}]=\mathbb{E}[e(t)-\mu]=\mu-\mu=0$$

We can then sobstitute these processes in the recursive equation:
$$\tilde{y}(t)=\frac{C(z)}{A(z)}\tilde{e}(t)$$
Which is a zero mean ARMA.

If we compute the covariance function of $\tilde{y}(t)$:
$$
\gamma_{\tilde{y}}(\tau)=\mathbb{E}[\tilde{y}(t)\tilde{y}(t-\tau)]=\newline
\mathbb{E}[(y(t)-m_y)(y(t-\tau)-m_y)]=\gamma_y(\tau)
$$

So the unbiased process $\tilde{y}(t)$ has the same covariance of $y(t)$.