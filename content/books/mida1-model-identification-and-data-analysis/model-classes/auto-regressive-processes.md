---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-classes
chapter_title: Model classes
created_at: '2022-03-26T17:20:30.000000Z'
id: 112
priority: 2
slug: auto-regressive-processes
title: Auto regressive processes
type: page
updated_at: '2022-03-28T19:58:34.000000Z'
---

# Auto regressive processes

## AR processes
Given a zero mean white noise $e(t) \sim WN(0, \lambda^2)$ then the stochastic process $y(t)$ is an auto regressive process if $y(t)$ is stationary and satisfies the **recursive equation**: $$y(t)=a_1y(t-1)+a_2y(t-2)+...+a_ny(t-n)+e(t)$$ which is a regression over the past values of the process itself.

$a_1,...a_n$ are **real parameters** and $n$ is the **order** of the process.

The recursive equation may admit multiple solutions, which is the one that gives th auto regressive process?

### Steady state solution
We define $Y(t_0)=(y(t_0-1),y(t_0-2),...,y(t_0-n))$ as the **initial values** needed to construct all future values of the process using the recursive equation.

The steady state solution is obtained **imposing the initial value to zero**: $Y(t_0)=0=(0,...,0)$ and then taking the limit for $t_0\to-\infty$:
$$\lim_{t_0 \to -\infty}{y_{t_0}(t)}=y(t)$$
which is the steady state solution (i.e. the AR process).

#### Example: AR(1)
Consider the following process:
$$y(t)=ay(t-1)+e(t) \text{ where } e(t) \sim WN(0, \lambda^2)$$

If we explicit $y(t-1)=ay(t-2)+e(t-1)$ then:
$$y(t)=e(t)+ae(t-1)+a^2y(t-2)$$

We can repeat the recursion util we reach:
$$y(t)=e(t)+ae(t-1)+a^2y(t-2)+...+a^{t-t_0}e(t_0)+a^{t-t_0+1}y(t_0-1)$$

With the steady stete initialization: $Y(t_0)=y(t_0-1)=0$ we obtain:
$$y(t)=e(t)+ae(t-1)+a^2y(t-2)+...+a^{t-t_0}e(t_0)$$

If we then take the limit:
$$
y(t)=\lim_{t_0\to-\infty}{y_{t_0}(t)}=\newline
=\lim_{t_0\to-\infty}{e(t)+ae(t-1)+a^2y(t-2)+...+a^{t-t_0}e(t_0)}=\sum_{i=0}^{-\infty}{a^i e(t-i)}
$$

We have obtained the steady state solution.

#### Steady state solution is an MA(inf) process
The steady state solution is an MA(inf) process with coefficients that are functions of the parameters of the recursive equation. In our example $c_i = a^i$.

The solution is then well defined when the condition under which a general $MA(\infty)$ process is well defined:
$$\sum_{i=0}^{-\infty}{c_i^2} < +\infty$$

Which in our example means:
$$\sum_{i=0}^{-\infty}{(a^i)^2} < +\infty$$

Which is a geometric serie that converges if $a^2<1$.

This result is valid in general, that is that the seady state solution is a well defined $MA(\infty)$ process for $-1<a<+1$ and it is an AR process.

## ARMA processes
Steady state solution to:
$$y(t)=a_1y(t-1)+...+a_my(t-m)+c_0e(t)+c_1e(t-1)+...+c_ne(t-n)$$
where $e(t) \sim WN(0,\lambda^2)$ and:
- $a_1,...,a_m,c_0,c_1,...,c_m$ are real parameters
- $m$ and $n$ are the orders of the process which we will denote $ARMA(m,n)$.

### Steady state solution
Is computed in the same way we computed the one of an $AR$ process:
$$
y(t)=a_1y(t-1)+...+a_my(t-m)+c_0e(t)+c_1e(t-1)+...+c_ne(t-n)=\newline
\text{substitute } y(t-1) \newline
\text{substitute } y(t-2) \newline
...
$$
Untill the initial condition is reached. Then take the limit for $t_0 \to -\infty$.

$ARMA(m,n)$ is an $MA(\infty)$ process whose coefficients are functions of $a_1,...,a_m,c_0,c_1,...,c_m$.

### Operatorial representation of ARMA
$$y(t)=a_1y(t-1)+...+a_my(t-m)+c_0e(t)+c_1e(t-1)+...+c_ne(t-n)$$
Can be written with the shift operators:
$$(1-a_1z^{-1}-...-a_mz^{-m})y(t)=(c_0+c_1z^{-1}+...+c_nz^{-n})e(t)$$

#### Transfer function (digital filter)
We can define an operator which takes a $WN$ as input and outputs the steady state solution:
$$y(t)=\frac{c_0+c_1z^{-1}+...+c_nz^{-n}}{1-a_1z^{-1}-...-a_mz^{-m}}e(t)=\frac{C(z)}{A(z)}e(t)$$