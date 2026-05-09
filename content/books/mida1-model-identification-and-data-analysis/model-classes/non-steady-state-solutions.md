---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: model-classes
chapter_title: Model classes
created_at: '2022-03-26T19:41:12.000000Z'
id: 116
priority: 5
slug: non-steady-state-solutions
title: Non steady state solutions
type: page
updated_at: '2022-03-28T19:56:28.000000Z'
---

# Non steady state solutions

<div drawio-diagram="136"><img src="../../../images/921ec47e3b_6l1WrfCZ8TZQQFcP-drawing-1-1648323952.png"></div>

If we consider a **stationary** stochastic process $v(t)$ and an assintotically stable transfer function $W(z)$ then the steady state solution of the recursive equation defined by the transfer function $W(z)$ is a well defined stationary stochastic process $y(t)$.

If we now consider a differnt non-null initialization of the recursive equations the output $y'(t)$ is a different process, that is $y'(t)\ne y(t)$, and it is **not stationary**.

But since the transfer function is assintotically stable the different (not null) initialization tends to vanish over time: $$y'(t) \xrightarrow[t \to +\infty]{} y(t)$$
In particular the convergence to $y(t)$ is exponentially fast.

## Questions from past exams
##### Say what we mean for steady state output of a digital filter W(z) fed by a stochastic process v(t) and specify the conditions under which the steady state output is stationary. What happens with a generic initialization of the filter W(z), explain in particular how the obtained output is in relation with the seady state output.
See above.