---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: uninformed-search-algorithms
chapter_title: Uninformed Search Algorithms
created_at: '2021-12-26T21:02:52.000000Z'
id: 23
priority: 2
slug: uniform-cost-search
title: Uniform-cost search
type: page
updated_at: '2022-01-12T14:00:11.000000Z'
---

# Uniform-cost search

When actions have different costs, an obvious choice is to use best-first search where the
evaluation function is the cost of the path from the root to the current node.

The idea is that while breadth-first search spreads out in
waves of uniform depth—first depth 1, then depth 2, and so on—uniform-cost search spreads
out in waves of uniform path-cost.

## Complexity
The complexity of uniform-cost search is characterized in terms of the cost of the
optimal solution $C^\*$, and $\epsilon$, a lower bound on the cost of each action, with $\epsilon$ > 0. Then the
algorithm’s worst-case time and space complexity is
$$O(b^{1+[\frac{C^*}{\epsilon}]})$$

Uniform-cost search is **complete and is cost-optimal**, because the first solution it finds will
have a cost that is at least as low as the cost of any other node in the frontier. Uniform-cost
search considers all paths **systematically in order of increasing cost**, never getting caught
going down a single infinite path (assuming that all action costs are $> \epsilon > 0$).