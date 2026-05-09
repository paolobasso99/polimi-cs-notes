---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: uncertainty
chapter_title: Uncertainty
created_at: '2023-01-05T14:50:52.000000Z'
id: 188
priority: 4
slug: uncertainty-over-time
title: Uncertainty over time
type: page
updated_at: '2023-01-06T14:44:07.000000Z'
---

# Uncertainty over time

We consider the **Markov assumption**: The current state $X_t$ depends on only
a finite fixed number of previous states.

A **Markov chain** is a sequence of random variablesfor which the distribution of each variable
follows the Markov assumption.

We can define a **transition model**, for example:
[![](../../../images/535111e45a_NLiurMqegNZpmR1y-image-1673015429940.png)](../../../images/535111e45a_NLiurMqegNZpmR1y-image-1673015429940.png)

In many cases we have an hidden state which is not observable but we can observe some variables. For example:
- We want to know the robot position but we can observe only the sensors data
- We want to know the words spoken but we observe only the audio waveforms
- We want to know the weather outside but we can only see how many people have an umbrella

An **hidden Markov model** is a Markov model for a system with hidden
states that generate some observed event.
[![](../../../images/b18162fc9a_5lhePsF9GBtkouUf-image-1673015619095.png)](../../../images/b18162fc9a_5lhePsF9GBtkouUf-image-1673015619095.png)

**Sensor Markov assumption**: the evidence variable depends only the corresponding state
[![](../../../images/9a4df84a38_YnPXQE4mX9HbzNTR-image-1673015951763.png)](../../../images/9a4df84a38_YnPXQE4mX9HbzNTR-image-1673015951763.png)

The possible tasks we could want to do in this context are:
[![](../../../images/1a7e67c449_IW3QR6iC78vZ4YrQ-image-1673016211731.png)](../../../images/1a7e67c449_IW3QR6iC78vZ4YrQ-image-1673016211731.png)