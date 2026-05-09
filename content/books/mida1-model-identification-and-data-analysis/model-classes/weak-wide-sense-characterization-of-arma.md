---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-classes
chapter_title: Model classes
created_at: '2022-03-26T19:58:14.000000Z'
id: 117
priority: 6
slug: weak-wide-sense-characterization-of-arma
title: Weak (wide sense) characterization of ARMA
type: page
updated_at: '2022-03-26T20:09:38.000000Z'
---

# Weak (wide sense) characterization of ARMA

Given the ARMA process:
$$y(t)=\frac{c_0+c_1z^{-1}+...+c_nz^{-n}}{1-a_1z^{-1}-...-a_mz^{-m}}e(t)=\frac{C(z)}{A(z)}e(t)$$

We can compute the weak (wide sense) characterization for a  well defined $y(t)$ ($W(z)$ assintotically stable):
- $\mathbb{E}[y(t)]=m_y$ constant mean function (SSP)
- $\gamma_y(\tau)=\mathbb{E}[(y(t)-m_y)(y(t-\tau)-m_y)]$ which is time invariant (SSP)

### Mean of ARMA
$$
m_y=\mathbb{E}[y(t)]=\mathbb{E}[a_1y(t-1)+...+a_m(y-m)+c_0e(t)+c_1e(t-1)+...+c_ne(t-n)]=\newline
=a_1\mathbb{E}[y(t-1)]+...+a_m\mathbb{E}[y(t-m)]+c_0\mathbb{E}[e(t)]+c_1\mathbb{E}[e(t-1)]+...+c_n\mathbb{E}[e(t-n)]=\newline
=a_1m_y+...+a_mm_y
$$
So $$(1-a_1-...-a_m)m_y = 0 \iff m_y=0$$

### Covariance of ARMA
Look notes 03 02 2022.