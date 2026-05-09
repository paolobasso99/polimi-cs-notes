---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-prediction
chapter_title: Model prediction
created_at: '2022-03-30T14:26:30.000000Z'
id: 128
priority: 5
slug: prediction-of-non-zero-mean-arma
title: Prediction of non zero mean ARMA
type: page
updated_at: '2022-03-30T14:34:42.000000Z'
---

# Prediction of non zero mean ARMA

Starting from an $ARMA$ process $y(t)=W(z)e(t)=\frac{C(z)}{A(z)}e(t)$, wehere $e(t) \sim WN(\mu,\lambda^2)$ that is canonical and minimum phase we need to compute the **unbiased processes**:
$$
\tilde{y}=y(t)-M_y\newline
\tilde{e}(t)=e(t)-\mu
$$
The resulting arma process $\tilde{y}(t)=\frac{C(z)}{A(z)}\tilde{e}(t)$ is still canonical and minimum phase.

We can compute its predictor $\hat{\tilde{y}}(t+k|t)$ and then:
$$\hat{y}(t+k|t)=\hat{\tilde{y}}(t+k|t)+m_y=\frac{F(z)}{C(z)}y(t)+(1-\frac{F(1)}{C(1)})m_y$$