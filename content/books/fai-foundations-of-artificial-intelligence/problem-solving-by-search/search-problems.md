---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: problem-solving-by-search
chapter_title: Problem Solving by Search
created_at: '2022-01-02T17:05:39.000000Z'
id: 78
priority: 0
slug: search-problems
title: Search problems
type: page
updated_at: '2022-01-19T11:15:34.000000Z'
---

# Search problems

A search problem can be defined formally as follows:
- A set of possible **states** that the environment can be in. We call this the **state space**.
- The **initial state** that the agent starts in. 
- A set of one or more **goal states**. Sometimes there is one goal state,
sometimes there is a small set of alternative goal states, and sometimes the goal is
defined by a property that applies to many states (potentially an infinite number).
- The **actions** available to the agent. Given a state $s$, $Actions(s)$ returns a finite set of
actions that can be executed in $s$. We say that each of these actions is **applicable** in $s$.
- A **transition model**, which describes what each action does. $Result(s,a)$ returns the state
that results from doing action $a$ in state $s$.
- An **action cost function**, denoted by $ActionCost(s,a,s')$ when we are programming or
when we are doing math, that gives the numeric cost of applying action $a$ in
state $s$ to reach state $s'$.

A sequence of actions forms a **path**, and a **solution** is a path from the initial state to a goal
state. We assume that action costs are additive; that is, the total cost of a path is the sum of
the individual action costs. An **optimal solution** has the lowest path cost among all
solutions.

The state space can be represented as a **graph** in which the vertices are states and the
directed edges between them are actions.

# Exam questions
### 2020 02 13 Q1
While organizing the Oscars’ Night gala dinner you have to assign seats to 𝑛 guests around a round table
with 𝑛 places. For every pair of guests 𝑖 and 𝑗 you know a positive value Pleasure(𝑖, 𝑗) that measures how much guest 𝑖 likes
sitting next to guest 𝑗. For simplicity, assume that Pleasure(𝑖, 𝑗) =  Pleasure(𝑗, 𝑖). Your objective is to find the seat assignment
that maximizes the total pleasure of guests.

(1) Formulate the above problem as a search problem. First, illustrate how you represent the states. Then, specify the initial
state, the ACTIONS() function, the RESULT() function, the goal test, and the step cost. (Hint: be especially careful in defining the
step cost.)

<details>
  <summary>Solution 1</summary>
  
  A possible formulation is the following:
- States represent partial assignments of guests to seats. Guests are indicated with numbers 1, 2, ... , 𝑛. A state 𝑠 is a vector of
  𝑛 seats, indexed from 1 to 𝑛. Each element of the vector that can take values 0 (meaning that the corresponding seat is
  empty) or 𝑖 (𝑖 ∈ {1,2, ... , 𝑛}, meaning that the corresponding seat is occupied by guest 𝑖).
  Note that the vector representing the state is intended to be circular: the element with index 1 is adjacent to the element
  with index 𝑛.
- Initial state: all seats are empty, represented as a vector of 𝑛 values equal to 0, [0,0, ... ,0].
- ACTIONS(𝑠) function takes a state 𝑠 and returns all the possible assignments of one guest to an empty seat (element equal to
  0 in 𝑠) that is adjacent to an occupied seat. If the seats are all unoccupied, namely when 𝑠 is the initial state, the function
returns all possible assignments of one guest to the seat with index 1.
- RESULT(𝑠, 𝑎) function trivially takes a state 𝑠 and an assignment 𝑎 of one guest to an empty seat (as returned by ACTIONS())
  and returns the updated state 𝑠′ (which is a vector with one less element equal to 0 with respect to 𝑠).
- Goal test checks if each guest has a seat (or, equivalently, if each seat is occupied by a guest and there is not any element
  equal to 0 in 𝑠).
- Step cost of an action that assigns guest 𝑗 to a seat adjacent to that occupied by guest 𝑖 is given by the value
  1/Pleasure(𝑖, 𝑗) . The inversion is motivated by the fact that the search process attempts to minimize the cost of the solution,
  while the problem asks for the maximum value of pleasure. When an action assigns guest 𝑗 to a seat that is adjacent to seats
  occupied by guests 𝑖 and 𝑙, the step cost accounts for both pleasures: 1/Pleasure(𝑖, 𝑗) + 1/Pleasure(𝑘, 𝑗). When an action
  assigns a guest 𝑗 to a seat and no other seat is occupied, the step cost is 0.
</details>

(2) Does your formulation allow to generate multiple nodes in the search tree that correspond to the same state? If yes,
illustrate a variant of your formulation that prevents these repetitions to happen. If no, explain why.


<details>
<summary>Solution 2</summary>
The above formulation allows to have multiple nodes in the search tree that correspond to the same state. For example,
two nodes corresponding to the state [1,2,0,0, ... ,0,3] can be generated as successors of nodes corresponding to states
[1,0,0,0, ... ,3] and [1,2,0,0, ... ,0], respectively.
This can be avoided by modifying the ACTIONS() function: it takes a state 𝑠 and returns all the possible assignments of one guest
to the empty seat with the smallest index.
</details>