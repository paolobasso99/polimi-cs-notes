---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-prediction
chapter_title: Model prediction
created_at: '2022-03-30T14:35:04.000000Z'
id: 129
priority: 6
slug: armax-predictors
title: ARMAX predictors
type: page
updated_at: '2022-03-30T18:02:13.000000Z'
---

# ARMAX predictors

Starting from an $ARMAX$ process $y(t)=\frac{B(z)}{A(z)}u(t-d)+\frac{C(z)}{A(z)}e(t)$, wehere $e(t) \sim WN(0,\lambda^2)$ and $\frac{C(z)}{A(z)}$ is canonical and minimum phase then we assume that the input signal $u(t-d)$ is either:
- completely known from $t=-\infty$ to $t=+\infty$
- $d\ \ge k$: the delay is bigger than the prediction horizon

Then the predictor is:
$$\hat{y}(t+k|t)=\frac{F(z)}{C(z)}y(t)+\frac{B(z)E(z)}{C(z)}u(t+k-d)$$

### Proof of the predictor of ARMAX
We define the process $z(t)$:
$$z(t)=y(t)-\frac{B(z)}{C(z)}u(t-d)=\frac{C(z)}{A(z)}e(t)$$
which is an $ARMA$ and is canonical. We now consider:
$$\frac{C(z)}{A(z)}=E(z)+\frac{z^{-k}F(z)}{A(z)}$$
So the predictor of $z$:
$$\hat{z}(t+k|t)=\frac{F(z)}{C(z)}z(t)$$
Since $y(t+k)=z(t+k)+\frac{B(z)}{A(z)}u(t+k-d)$ but $\frac{B(z)}{A(z)}u(t+k-d)$ is function of past values of the input process which, under our hypotesis, is known at time $t$; the predictor of $y(t)$ becomes:
$$\hat{y}(t+k|t)=\hat{z}(t+k|t)+\frac{B(z)}{A(z)}u(t+k-d)=\frac{F(z)}{C(z)}z(t)+\frac{B(z)}{A(z)}u(t+k-d)$$
Sobstitute the definition of $z(t)$:
$$\hat{y}(t+k|t)=\frac{F(z)}{C(z)}\left[y(t)-\frac{B(z)}{C(z)}u(t-d)\right]+\frac{B(z)}{A(z)}u(t+k-d)$$
$$=\frac{F(z)}{C(z)}y(t)-\frac{F(z)}{C(z)}\frac{B(z)}{A(z)}u(t-d)+\frac{B(z)}{A(z)}u(t+k-d)$$
Considering $u(t-d)=z^{-k}u(t+k-d)$ and aranging the terms:
$$\hat{y}(t+k|t)=\frac{F(z)}{C(z)}y(t)+\frac{B(z)}{A(z)}\left[1-\frac{z^{-k}F(z)}{C(z)}\right]u(t+k-d)=$$
$$=\frac{F(z)}{C(z)}y(t)+\frac{B(z)}{C(z)}\left[\frac{C(z)}{A(z)}-\frac{z^{-k}F(z)}{A(z)}\right]u(t+k-d)$$
If we consider that $\frac{C(z)}{A(z)}=E(z)+\frac{z^{-k}F(z)}{A(z)}$ then the predictor is:
$$\hat{y}(t+k|t)=\frac{F(z)}{C(z)}y(t)+\frac{B(z)E(z)}{C(z)}u(t+k-d)$$