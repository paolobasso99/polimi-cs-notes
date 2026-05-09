---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
created_at: '2022-03-26T18:01:01.000000Z'
id: 113
priority: 3
slug: shift-operators
title: Shift operators
type: page
updated_at: '2022-03-26T18:08:16.000000Z'
---

# Shift operators

The shift operators are:
- $z^{-1}$ **backward shift operator**
- $z^1$ **forward shift operator**

Given a stochastic process $y(t,s)$ then $z^-1y(t,s)=y(t-1,s)$ which has the same realization shifted one time instant backwards.

## Properties
The shift operators:
1. are **linear**:
$$z^{-1}(av(t)+by(t))=az^{-1}v(t)+bz^{-1}y(t)$$
2. can be **recursively combined**:
$$z^{-1}(z^{-1}(z^{-1}(y(t))))=z^{-3}y(t)$$