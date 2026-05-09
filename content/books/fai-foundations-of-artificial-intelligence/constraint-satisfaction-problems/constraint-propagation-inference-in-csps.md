---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: constraint-satisfaction-problems
chapter_title: Constraint Satisfaction Problems
created_at: '2021-12-30T12:47:09.000000Z'
id: 55
priority: 1
slug: constraint-propagation-inference-in-csps
title: 'Constraint Propagation: Inference in CSPs'
type: page
updated_at: '2022-01-24T17:14:39.000000Z'
---

# Constraint Propagation: Inference in CSPs

A CSP algorithm has choices. It can generate successors by
choosing a new variable assignment, or it can do a specific type of inference called
**constraint propagation**: using the constraints to reduce the number of legal values for a
variable, which in turn can reduce the legal values for another variable, and so on.

Constraint propagation may be intertwined with search, or it may be done as a
preprocessing step, before search starts. Sometimes this preprocessing can solve the whole
problem, so no search is required at all.

## Node consistency
A single variable (corresponding to a node in the CSP graph) is node-consistent if all the
values in the variable’s domain satisfy the variable’s unary constraints.

It is easy to eliminate all the unary constraints in a CSP by reducing the domain of variables
with unary constraints at the start of the solving process. It is also
possible to transform all n-ary constraints into binary ones. 

## Arc consistency
A variable in a CSP is arc-consistent if every value in its domain satisfies the variable’s
binary constraints. More formally, $X_i$ is arc-consistent with respect to another variable $X_j$ if
for every value in the current domain $D_i$ there is some value in the domain $D_j$ that satisfies
the binary constraint on the arc $(X_i, X_j)$. A graph is arc-consistent if every variable is arc-consistent with every other variable.

The most popular algorithm for enforcing arc consistency is called **AC-3**.

To make every variable arc-consistent, the AC-3 algorithm maintains a queue of arcs to
consider. Initially, the queue contains all the arcs in the CSP. (Each binary constraint
becomes two arcs, one in each direction.) AC-3 then pops off an arbitrary arc $(X_i, X_j)$ from
the queue and makes $X_i$ arc-consistent with respect to $X_j$.

If this leaves $D_i$ unchanged, the
algorithm just moves on to the next arc. But if this revises $D_i$(makes the domain smaller),
then we add to the queue all arcs $(X_k, X_i)$ where $X_k$ is a neighbor of $X_i$ and $(k\neq j)$. We need to do that
because the change in $D_i$ might enable further reductions in $D_j$, even if we have previously
considered $X_k$. If is revised down to nothing, then we know the whole CSP has no
consistent solution, and AC-3 can immediately return failure. Otherwise, we keep checking,
trying to remove values from the domains of variables until no more arcs are in the queue.

At that point, we are left with a CSP that is equivalent to the original CSP—they both have
the same solutions—but the arc-consistent CSP will be faster to search because its variables
have smaller domains.

The complexity of AC-3 can be analyzed as follows. Assume a CSP with $n$ variables, each
with domain size at most $d$, and with $d$ binary constraints (arcs). Each arc $(X_k, X_i)$ can be
inserted in the queue only $d$ times because $X_i$ has at most $d$ values to delete. Checking
consistency of an arc can be done in $O(d^2)$ time, so we get total $O(cd^3)$ worst-case time.

## Path consistency
Arc consistency tightens down the domains (unary constraints) using the arcs (binary
constraints). Path consistency tightens the binary constraints by using implicit constraints
that are inferred by looking at triples of variables.

## K-consistency
Stronger forms of propagation can be defined with the notion of k-consistency.

# Exam questions
### 2020 01 20 Q2 (8 points)
Consider the following Constraint Satisfaction Problem (CSP):
- variables: $v_1$, $v_2$, $v_3$
- domains: $D_1$ = $D_2$ = $D_3$ = $\lbrace 0, 1, 2, 3, 4, 5 \rbrace$,
- constraints: $v_1 + v_2 = 3$, $v_1 \le v_3$, $v_2 +v_3 \le 3$.

1. Apply the arc consistency algorithm AC-3 to the above CSP. Report the state of the queue and the updated domains at each
step of the algorithm.

<details>
  <summary>Solution 1</summary>

Each binary constraint becomes two arcs, one in each direction so the initial queue is:
$$ v_1 \to v_2, v_2 \to v_1, v_1 \to v_3, v_3 \to v_1, v_2 \to v_3, v_3 \to v_2 $$
AC-3 pops off an arbitrary arc and makes it arc-consistent (restrict the domain so every value satisfies the constraint):
- $v_1 \to v_2$ restricts $D_1 = \lbrace 0, 1, 2, 3 \rbrace$, no arc must be added to the queue because this was the first arc popped. Queue: $v_2 \to v_1, v_1 \to v_3, v_3 \to v_1, v_2 \to v_3, v_3 \to v_2 $.
- $v_2 \to v_1$ restricts $D_2 = \lbrace 0, 1, 2, 3 \rbrace$, no arc added because $v_3 \to v_2$ is already present. Queue: $v_1 \to v_3, v_3 \to v_1, v_2 \to v_3, v_3 \to v_2$.
- $v_1 \to v_3$ $D_1$ unchanged. Queue: $v_3 \to v_1, v_2 \to v_3, v_3 \to v_2$.
- $v_3 \to v_1$ $D_3$ unchanged. Queue: $v_2 \to v_3, v_3 \to v_2$.
- $v_2 \to v_3$ already restricted to $D_2 = \lbrace 0, 1, 2, 3 \rbrace$ so unchanged. Queue: $v_3 \to v_2$.
- $v_3 \to v_2$ restricts $D_3 = \lbrace 0, 1, 2, 3 \rbrace$. Arc $v_1 \to v_3$ is added to the queue. Queue: $v_1 \to v_3$
- $v_1 \to v_3$ already restricted to $D_1 = \lbrace 0, 1, 2, 3 \rbrace$ so unchanged.

The final domains are: $D_1 = D_2 = D_3 = \lbrace 0, 1, 2, 3 \rbrace$.
</details>