---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: uninformed-search-algorithms
chapter_title: Uninformed Search Algorithms
created_at: '2021-12-27T12:55:06.000000Z'
id: 26
priority: 5
slug: bidirectional-search
title: Bidirectional search
type: page
updated_at: '2022-01-02T16:54:21.000000Z'
---

# Bidirectional search

Simultaneously searches forward from the initial state and backwards from the goal state(s),
hoping that the two searches will meet. The motivation is that $b^{d/2} + b^{d/2}$ is much less than $b^d$.

For this to work, we need to keep track of two frontiers and two tables of reached states, and
we need to be able to reason backwards. We
have a solution when the two frontiers collide.

There are many different versions of bidirectional search, just as there are many different
unidirectional search algorithms.