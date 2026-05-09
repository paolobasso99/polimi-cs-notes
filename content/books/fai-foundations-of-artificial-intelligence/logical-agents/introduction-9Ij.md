---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: logical-agents
chapter_title: Logical Agents
created_at: '2021-12-30T16:00:15.000000Z'
id: 57
priority: 0
slug: introduction-9Ij
title: Introduction
type: page
updated_at: '2022-01-04T15:24:10.000000Z'
---

# Introduction

A logical agent is an agent that is capable of using **logical sentences** to represent knowledge of
states and actions, and to exploit such representation to decide what to do

By logical sentence we mean a sentence (i.e., a well-formed formula) of the formal language of a
logical system, like Propositional Logic (PL), First Order Logic (FOL), systems of Modal Logic, etc.

## Knowledge-based agents
Knowledge-based agents use a process of reasoning over an internal representation of
knowledge to decide what actions to take.

The central component of a knowledge-based agent is its knowledge base, or KB. A
knowledge base is a set of sentences. (Here “sentence” is used as a technical term. It is
related but not identical to the sentences of English and other natural languages.) Each
sentence is expressed in a language called **knowledge representation language** and
represents some assertion about the world. When the sentence is taken as being given
without being derived from other sentences, we call it an **axiom**.

There must be a way to add new sentences to the knowledge base and a way to query what
is known. The standard names for these operations are **TELL** and **ASK**, respectively. Both
operations may involve **inference**—that is, deriving new sentences from old.

### Statements and objects
- Statements can be true or false (no third option!) in a given situation
	- A = “the engine is getting gas”
- Statements can be composed into complex sentences
- Statements can be rules (∀𝑥∀𝑦 𝑀(𝑥, 𝑦) → 𝑃(𝑥, 𝑦)) or facts (𝑀(Lulu, Fifi))
- Objects denote entities that populate a given situation

## Logic
Logics are formal languages for representing information such that conclusions can be drawn
- **Syntax** defines the sentences in the language
- **Semantics** define the “meaning” of sentences (namely, define truth of a sentence in a world)

## Entailment
Idea that a sentence
follows logically from another sentence. In mathematical notation, we write:
$$ \alpha \models \beta$$
iff in every world where a is true, b is
also true

### Proving entailment
1. **Model checking**:
	- For every possible world, if $\alpha$ is true check whether $\beta$ is true too
    - Works for propositional logic (finitely many worlds); not easy for first-order logic
2. **Theorem-proving**:
	- Search for a sequence of proof steps (applications of inference rules) leading from $\alpha$ to $\beta$
    
A proof is a demonstration of entailment between $\alpha$ and $\beta$ using an algorithm $A$,
we write $\alpha \vdash_A \beta$. An algorithm is:
- **Sound**: everything it claims to prove is in fact entailed: $\alpha \vdash_A \beta \implies \alpha \models \beta$
- **Complete**: everything that is entailed can be proved: $\alpha \models \beta \implies \alpha \vdash_A \beta$

# Exam questions
### 2019 02 15 Q3.1
Explain the difference between “sentence a entails sentence b” (a ⊨ b) and “sentence b can be derived
from sentence a by inference algorithm i” (a ⊢i b).