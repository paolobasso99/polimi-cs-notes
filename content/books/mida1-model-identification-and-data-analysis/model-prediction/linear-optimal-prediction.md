---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-prediction
chapter_title: Model prediction
created_at: '2022-03-30T10:45:26.000000Z'
id: 124
priority: 1
slug: linear-optimal-prediction
title: Linear optimal prediction
type: page
updated_at: '2022-07-01T10:34:29.000000Z'
---

# Linear optimal prediction

Starting from an $ARMA$ process $y(t)=W(z)e(t)=\frac{C(z)}{A(z)}e(t)$, wehere $e(t) \sim WN(0,\lambda^2)$ (non zero mean case is an easy extension) we assume:
1. $W(z)$ is asymptotically stable, and so $y(t)$ is well defnined
2. $y(t)=\frac{C(z)}{A(z)}e(t)$ is the **canonical representation**
3. $\frac{C(z)}{A(z)}$ is **minimum phase** ($|zeros|<1$)

We do not lose generality for the first two assumption but we do for the third one. THe last assumption is a mieldly limiting assumption (i.e. some well defined $ARMA$ processes are excluded) but the excluded processes are a small subclass that can be well aprozimated by other $ARMA$ processes.

#### Problem to solve
$y(t)$ is the **output of interest** which can be observed up to the time instant $t$.

We want to use the observed values to predict the value at future time instants.

$\hat{y}(t+k|t)$ is the prediction, based on observation of $y$ up to time $t$, of $y$ at time $t+k$.

##### Abstraction: unlimited sequence
We suppose to have all observations from $-\infty$ up to $t$ (infinite sequence):
$$...,y(-10),...,y(0),y(1),...,y(t)$$
This assumption simplifies the solution to the prediction problem: the solution of a real problem with finite data is an aproximation of the solution of the abstract problem.

### Linearity
The prediction is a function of the observed data:
$$\hat{y}(t+k|t) = f(y(t),y(t-1),...)$$
We focus on **linear functions**:
$$\hat{y}(t+k|t) = \sum_{i=0}^{+\infty}{a_iy(t-i)}=a_0y(t)+a_1y(t-1)+...+a_iy(t-i)+...$$
The coefficients ${a_i}$ are the **parameters** which have to be selected in order to achive the "best" result.

## Prediction metric: Mean Square Error
The intuitive goal is to find $\hat{y}(t+k|t) \approx y(t+k)$.

Observations are thougths of as realizations of a stationary stochastic process: $y(t)=y(t,s)$, and so $y(t+k)=y(t+k,s)$. Then, $\hat{y}(t+k|t)=\hat{y}(t+k|t,s)$ is a function of $f(y(t,s),y(t-1,s),...)$.

This means that there is a **variability with the experiment** while we want a predictor which is good inrespective of the specific realization $s$.

A possible prediction metric is the **Mean Square Error (MSE)**:
$$\mathbb{E}[(y(t+k,s)-\hat{y}(t+k|t,s))^2]$$