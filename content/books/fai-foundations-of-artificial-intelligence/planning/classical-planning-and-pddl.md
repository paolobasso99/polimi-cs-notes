---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: planning
chapter_title: Planning
created_at: '2022-01-01T15:25:41.000000Z'
id: 75
priority: 0
slug: classical-planning-and-pddl
title: Classical Planning and PDDL
type: page
updated_at: '2022-01-24T12:40:58.000000Z'
---

# Classical Planning and PDDL

Classical planning is defined as the task of finding a sequence of actions to accomplish a
goal in a discrete, deterministic, static, fully observable environment.

We have seen two
approaches to this task: the problem-solving agent and the hybrid
propositional logical agent. Both share two limitations:
1. They both
require ad hoc heuristics for each new domain: a heuristic evaluation function for search,
and hand-written code for the hybrid wumpus agent. 
2. They both need to explicitly
represent an exponentially large state space. 

In response to these limitations, planning researchers have invested in a factored
representation using a family of languages called **PDDL, the Planning Domain Definition
Language**.

## PDDL
Basic PDDL can handle
classical planning domains, and extensions can handle non-classical domains that are
continuous, partially observable, concurrent, and multi-agent. 

In PDDL, a state is represented as a conjunction of ground atomic fluents. Recall that
“ground” means no variables, “fluent” means an aspect of the world that changes over time,
and “ground atomic” means there is a single predicate, and if there are any arguments, they
must be constants. 

### Assumptions
- **Unique Name Assumption (UNA)**: different constants always denote different objects
- **Domain Closure Assumption (DCA)**: the environment includes only those objects that are
denoted by a constant
- **Closed World Assumption (CWA)**: all literals that are not explicitly mentioned in the description
of the state are assumed to be false (i.e., their negation is assumed to be true). 

### Actions and action  schemas
An action schema represents a family of ground actions.

The schema consists of the action name, a list of all the variables used in the schema, a
**precondition** and an **effect**. The precondition and the effect are each conjunctions of literals
(positive or negated atomic sentences). We can choose constants to instantiate the variables,
yielding a ground (variable-free) action.

A ground action a is applicable in state s if s entails the precondition of a; that is, if every
positive literal in s the precondition is in and every negated literal is not.

The result of executing applicable action a in state s is defined as a state which is
represented by the set of fluents formed by starting with s, removing the fluents that appear
as negative literals in the action’s effects (what we call the **delete list** or DEL(a)), and adding
the fluents that are positive literals in the action’s effects (what we call the **add list** or
ADD(a))

### Goals
- Conjunction of literals, $Clean(𝑅_1) \land Clean(𝑅_2)$
	- PDDL: negative literals are allowed (e.g., $¬Clean(𝑅_1) \land Clean(𝑅_2)$)
	- Literals are called sub-goals
- No disjunctions $Clean(𝑅_1) \lor Clean(𝑅_2)$
- A goal 𝐺 is satisfied in a state 𝑆 when all the positive literals of 𝐺 are contained in the
representation of 𝑆 and all the negative literals of 𝐺 are not contained in 𝑆
- Goals can contain variables

## STRIPS
STRIPS is another planning language. It is different from PDLL because **no negative literals allowed**.

# Exam questions
### 2020 02 13 Q4.1
To put the air conditioning to work one has to press the START button when the ON-OFF switch is ON
and the air conditioning is not already working. Initially, the ON-OFF switch is OFF and the air conditioning is not working. The
goal is to put the air conditioning to work.

Use PDDL to represent the problem. List all the problem-dependent symbols that you introduce and briefly explain the
meaning of each of them. (Be careful to introduce the smallest possible set of symbols.) Then specify the initial state, the
goal, and the action schemes that are strictly necessary to solve the problem.



<details>
  <summary>Solution</summary>
  
Predicates:
- $On$ the switch is ON
- $Working$ the air conditioner is working

Initial state: $\lnot On  \land \lnot Working$
  
Goal state: $Working$
Actions:
- switchOn()
	- Precond: $\lnot On$
    - Eff: $On$
- start()
	- Precond: $On \land \lnot Working$
    - Eff: $Working$
</details>

### 2019 01 18 Q4
In their representation of states, systems like STRIPS adopt ”database semantics”, and in particular the Closed
World Assumption. Explain what the Closed World Assumption amounts to and why it is adopted.

<details>
  <summary>Solution</summary>

The Closed World Assumption amounts to consider as false all the sentences that are not known to be true. In
STRIPS, this means that all the predicates not listed in the representation of a state are considered false. This is possible thanks to the closed-world assumption.
</details>

On a table there are three beer bottles and a bottle opener. A two-armed robotic waiter can: pick up from the table any object (either a bottle or the bottle opener) with either hand (provided the hand is free); put back an object to the table (provided it holds the object with either hand); and open a bottle with the opener (provided
the bottle is held in the left hand and the opener is held in the right hand). Initially, both the waiter's hands are free and all the bottles are closed. The goal is to have all the bottles open on the table. Using STRIPS:
- introduce a suitable set of constants and predicates, describing their intuitive meaning;
- specify a set of action schemas sufficient to solve the above planning problem;
- represent the initial state and the goal of the above planning problem.

<details>
  <summary>Solution</summary>

Constants: 
- $L$, $R$ the hands
- $B1$, $B2$, $B3$ the botles
- $O$ the opener

Predicates:
- $OnTable(x)$ x on table
- $Open(x)$ x is open
- $Botle(x)$ x is a botle
- $Closed(x)$ x is closed
- $Free(x)$ hand x is free
- $Hold(x, y)$ hand x holds object y

Actions:
- $open(x)$
	- precond: $Botle(x) \land Closed(x) \land Hold(L, x) \land Hold(R, O)$
    - effect: $Open(x) \land \lnot Closed(x)$
- $pickUp(x, y)$
	- precond: $Free(x) \land OnTable(y)$
    - effect: $\lnot Free(x) \land \lnot OnTable(y) \land Hold(x, y)$
- $putDown(x)$
	- precond: $Hold(x,y)$
    - efect: $\lnot Hold(x,y) \land Free(x) \land OnTable(y)$
    
Initial state: $Free(R) \land Free(L) \land OnTable(B1) \land OnTable(B2) \land OnTable(B3) \land OnTable(O) \land Closed(B1) \land Closed(B2) \land Closed(B3) \land Botle(B1) \land Botle(B2) \land Botle(B3)$

Goal state: $OnTable(B1) \land OnTable(B2) \land OnTable(B3) \land Open(B1) \land Open(B2) \land Open(B3)$
</details>