---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-classes
chapter_title: Model classes
created_at: '2022-03-26T19:26:00.000000Z'
id: 115
priority: 4
slug: when-arma-is-well-defined
title: When ARMA is well defined?
type: page
updated_at: '2022-03-26T19:39:36.000000Z'
---

# When ARMA is well defined?

Given the steady state output of the recursive equation defined by the transfer function $W(z)$ fed by the stochastic process $v(t)$: $$y(t)=W(z)v(t)$$
Then $y(t)$ is well defined iff:
1. $v(t)$ is stationary
2. $W(z)$ is assintotically stable

So ARMA process $y(t)=W(z)e(t)$ with $e(t) \sim WN(0,\lambda^2)$ is well defined if $W(z)$ is assintotically stable (because the white noise is stationary by definition).

### Idea of proof
1. Suppose $A(z)=1$:
$$y(t)=C(z)v(t)=c_0v(t)+c_1v(t-1)+...+c_nv(t-n)$$
the result is true by direct verification.
2. Suppose:
$$y(t)=\frac{1}{1-az^{-1}}v(t)=\frac{z}{z-a}v(t)$$
then there is a single pole $z=a$ and a direct computation of the steady state solution reveals that if $|a|<1$ then $y(t)$ is well defined and stationary.
3. Consider now the general case:
$$y(t)=\frac{C(z)}{A(z)}v(t)=\frac{C(z)}{(z-p_1)(z-p_2)...(z-p_m)}v(t)=C(z)\frac{1}{(z-p_1)}\frac{1}{(z-p_2)}...\frac{1}{(z-p_m)}v(t)$$
it is a series of simple operators which correspond to case 1 or 2.