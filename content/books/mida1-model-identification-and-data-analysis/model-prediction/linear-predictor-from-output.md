---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-prediction
chapter_title: Model prediction
created_at: '2022-03-30T12:30:21.000000Z'
id: 127
priority: 4
slug: linear-predictor-from-output
title: Linear predictor from output
type: page
updated_at: '2022-03-30T14:26:13.000000Z'
---

# Linear predictor from output

In the real world we cannot measur the white noise, the only aviable information is the values of the process up to time $t$.

We **need to construct the white noise** underlyning the generation of the process from the values of the process itself up to time $t$. This means that if we are able to define:
$$e(t)=h_0y(t)$$
$$e(t)=h_0y(t)+h_1y(t-1)+...= \sum_{i=0}^{+\infty}{h_iy(t-i)}$$
Then the optimal predictor from noise can be written as a predictor from output:
$$\hat{y}(t+k|t)=\sum_{i=0}^{+\infty}{w_{k+i}[\sum_{j=0}^{+\infty}{h_jy(t-i-j)}]}$$

## Reconstructing WN from output
Since we imposed that $\frac{C(z)}{A(z)}$ is minimum phase then $\frac{A(z)}{C(z)}$ is asymptotically stable and:
$$e(t)=\frac{C(z)}{A(z)}y(t)=\sum_{i=0}^{+\infty}{h_iy(t-i)}$$.
So:
$$\hat{y}(t+k|t)=\frac{F(z)}{C(z)}y(t)$$