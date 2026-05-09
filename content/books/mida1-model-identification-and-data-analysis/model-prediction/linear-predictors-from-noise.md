---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-prediction
chapter_title: Model prediction
created_at: '2022-03-30T11:24:52.000000Z'
id: 125
priority: 2
slug: linear-predictors-from-noise
title: Linear predictors from noise
type: page
updated_at: '2022-03-30T12:17:33.000000Z'
---

# Linear predictors from noise

Starting from an $ARMA$ process $y(t)=W(z)e(t)=\frac{C(z)}{A(z)}e(t)$, wehere $e(t) \sim WN(0,\lambda^2)$ we know that $y(t)$ is a steady state solution and $y(t) \sim MA(\infty)$, so:
$$y(t) = w_0e(t)+w_1e(t-1)+...+w_ie(t-i)+...=\sum_{i=0}^{+\infty}{w_ie(t-i)}$$

Where $w_i = f(\text{parameters of }C(z)\text{ and }A(z))$.

The predictor: $\hat{y}(t+k|t) = a_0y(t)+a_1y(t-1)+...+a_iy(t-i)+...$ can be written as:
$$\hat{y}(t+k|t) = a_0[\sum_{i=0}^{+\infty}{w_ie(t-i)}] + a_1[\sum_{i=0}^{+\infty}{w_ie(t-1-i)}] + ... =$$
$$= a_0[w_0e(t)+w_1e(t-1)+...]+a_1[w_0e(t-1)+w_1e(t-2)+...] + ...$$

Arranging the terms:
$$\hat{y}(t+k|t) = \beta_0 e(t) + \beta_1 e(t-1) + ... = \sum_{i=0}^{+\infty}{\beta_ie(t-i)}$$
Where:
$$
\beta_0 = a_0w_0 \newline
\beta_1 = a_0w_1 + a_1w_1 \newline
...
$$

The predictor is computed as an infinite regression over the past values of the white noise underlying the generation of $y$: $\beta_i$ is a function of the parameters of ARMA and the predictor.

## Optimal solution from noise
The optimal predictor from noise is:
$$\hat{y}(t+k|t) = \sum_{i=0}^{+\infty}{w_{k+i}e(t-i)}$$

**IDEA OF PROOF (complete in the notes)**

It is found starting from the linear predictor:
$$\hat{y}(t+k|t) = \sum_{i=0}^{+\infty}{\beta_ie(t-i)}$$

Minimizing the MSE:
$$\min_{\lbrace\beta_i\rbrace}\mathbb{E}[(y(t+k)-\hat{y}(t+k|t))^2]=\min_{\lbrace\beta_i\rbrace}\mathbb{E}[(y(t+k)-\sum_{i=0}^{+\infty}{\beta_ie(t-i)})^2]$$

Considering thath $y(t)$ is an $ARMA$ it is a $MA(\infty)$, then:
$$y(t)=\sum_{i=0}^{+\infty}{w_ie(t-i)} \text{ } \forall t$$
So:
$$y(t+k) = \sum_{i=0}^{k-1}{w_ie(t+k-i)}+\sum_{j=k}^{+\infty}{w_ie(t+k-i)}$$

And pugging this int the MSE we find that the minimization coincides with:
$$\hat{y}(t+k|t) = \sum_{i=0}^{+\infty}{w_{k+i}e(t-i)}$$

#### Interpretation
$$y(t+k) = \sum_{i=0}^{k-1}{w_ie(t+k-i)}+\sum_{j=k}^{+\infty}{w_ie(t+k-i)}$$
We can divide the two sum:
1. The first sum is a function of the **future values** of the white noise which are unknown and unpredictable at time $t$
2. The second sum is a function of **past values** of the white noise, the values are aviable at time $t$ and so they are predictable
The unpredictable part (first sum) is therefore dropped.