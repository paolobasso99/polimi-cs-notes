---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-prediction
chapter_title: Model prediction
created_at: '2022-03-30T12:17:41.000000Z'
id: 126
priority: 3
slug: long-k-step-division-method
title: Long k-step division method
type: page
updated_at: '2022-03-30T12:30:00.000000Z'
---

# Long k-step division method

The steady state solution of an $ARMA$ process can be obtained with a long k-step division of $C(z)$ and $A(z)$ seen as polynomial of $z$ performing only k-steps.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/tt2VvO6joD4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

$$\frac{C(z)}{A(z)}=E(z)+\frac{z^{-k}F(z)}{A(z)}$$
Where:
- $E(z)$ is the quotient
- $z^{-k}F(z)$ is the reminder

Then:
$$\hat{y}(t+k|t)=\frac{z^{-k}F(z)}{A(z)}e(t+k)=\frac{F(z)}{A(z)}e(t)$$

**IDEA OF PROOF (complete in notes)**

If we sobstitute $\frac{C(z)}{A(z)}=E(z)+\frac{z^{-k}F(z)}{A(z)}$ inside:
$$y(t+k)=\frac{C(z)}{A(z)}e(t+k)$$
and then considering $E(z)=w_0+w_1z^{-1}+...+w_{k-1}z^{-k+1}$,w e obtain:
$$y(t+k)=w_0e(t+k)+...+w_{k-1}e(t+1)+\frac{z^{-k}F(z)}{A(z)}e(t+k)$$
Dropping the unpredictable part:
$$\hat{y}(t+k|t)=\frac{z^{-k}F(z)}{A(z)}e(t+k)=\frac{F(z)}{A(z)}e(t)$$