---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: constraint-satisfaction-problems
chapter_title: Constraint Satisfaction Problems
created_at: '2021-12-30T12:25:05.000000Z'
id: 54
priority: 0
slug: introduction-PMC
title: Introduction
type: page
updated_at: '2022-01-02T16:54:21.000000Z'
---

# Introduction

**Factored representation** for each
state: a set of variables, each of which has a value. A problem is solved when each variable
has a value that satisfies all the constraints on the variable. A problem described this way is
called a **constraint satisfaction problem**, or **CSP**.

CSP search algorithms take advantage of the structure of states and use general rather than
domain-specific heuristics to enable the solution of complex problems. The main idea is to
eliminate large portions of the search space all at once by identifying variable/value
combinations that violate the constraints. CSPs have the additional advantage that the
actions and transition model can be deduced from the problem description.

## Definition
A constraint satisfaction problem consists of three components, $X$, $D$, and $C$:
- $X$ is a set of **variables** $\lbrace X_1, ..., X_n \rbrace$
- $D$ is a set of **domains** $\lbrace D_1, ..., D_n \rbrace$. A domain, $D_i$, consists of a set of allowable values, $\lbrace v_1, ..., v_n \rbrace$, for variable $X_i$.
- $C$ is a set of **constraints** that specify allowable combinations of values. Each $C_j$ constraint consists of a pair $\lang scope, rel \rang$, where $scope$
is a tuple of variables that participate in the constraint and $rel$ is a **relation** that defines
the values that those variables can take on. A relation can be represented as an explicit set
of all tuples of values (E.g. $\lbrace 1, 2, 3 \rbrace$) that satisfy the constraint, or as a function (E.g $X_1 > X_2$) that can compute whether a
tuple is a member of the relation.

CSPs deal with assignments of values to variables, $\lbrace X_i=v_i, X_j=v_j, ... \rbrace$

An assignment
that does not violate any constraints is called a **consistent** or legal assignment. A **complete**
assignment is one in which every variable is assigned a value, and a **solution** to a CSP is a
consistent, complete assignment. A **partial assignment** is one that leaves some variables
unassigned, and a **partial solution** is a partial assignment that is consistent. Solving a CSP is
an **NP-complete** problem in general, although there are important subclasses of CSPs that
can be solved very efficiently.