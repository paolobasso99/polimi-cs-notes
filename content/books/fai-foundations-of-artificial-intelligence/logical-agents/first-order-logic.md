---
book_slug: fai-foundations-of-artificial-intelligence
book_title: FAI - Foundations of Artificial Intelligence
chapter_slug: logical-agents
chapter_title: Logical Agents
created_at: '2022-01-19T10:10:16.000000Z'
id: 88
priority: 2
slug: first-order-logic
title: First order logic
type: page
updated_at: '2022-01-19T11:15:34.000000Z'
---

# First order logic

Whereas propositional logic assumes the world contains statements, first-order logic (like
natural language) assumes the world contains:
- **objects** 
- statements in form of **relations** (predicates) between objects

## Syntax
### Basic elements
- **Constant symbols**: KingJohn, 2, POLIMI, ...
- **Predicate symbols**: Brother, >, ...
- **Function symbols**: Sqrt, LeftLegOf, ...
- **Variables**: 𝑥, 𝑦, 𝑎, 𝑏, ...
- **Connectives**: $\lnot$, $\to$, $\land$, $\lor$, $\iff$
- **Equality**: $=$
- **Quantifiers**: $\forall$, $\exists$

### Terms and sentences
A **term** denotes an object in the form: *function(term1,...,termn)*, *constant*, *variable*.

An **atomic sentence** is in the form *predicate(term1,...,termn)* or *term1 = term2*.

A **complex sentence** is made from atomic sentences using connectives, for example: $\lnot \alpha$, $\alpha \land \beta$, $Brother(KingJohn,Richard) \to Brother(Richard,KingJohn)$

## Semantics
Sentences are **true** with respect to a **model** and an **interpretation**.

The model contains objects (domain elements) and relations among them while the interpretation specifies referents for:
- constant symbols → objects
- predicate symbols → relations
- function symbols → functions

An atomic sentence predicate(term1,...,termn) is true when the objects referred to by
term1,...,termn are in the relation referred to by predicate and a complex sentence is true with the usual rules for connectives.

### Universal quantification
Everyone at POLIMI is smart: $\forall x At(x, POLIMI) \to Smart(x)$

$\forall x P$ is true in a model $M$ $\iff$ $P$ is true with $x$ being **each** possible object in the model. Roughly speaking, universal quantification is equivalent to the **conjunction** of instantiations of 𝑃.

Typically, $\to$ is the main connective with $\forall$. A common mistake is using $\land$ as the main connective with $\forall$: $\forall x At(x, POLIMI) \land Smart(x)$ means "Everyone is at POLIMI and everyone is smart".

### Existential quantification
Someone at POLIMI is smart: $\exists x At(x, POLIMI) \land Smart(x)$

$\exists x P$ is true in a model $M$ $\iff$ $P$ is true with $x$ being **some** possible object in the model. Roughly speaking, universal quantification is equivalent to the **disjunction** of instantiations of 𝑃.

Typically, $\land$ is the main connective with $\exists$. A common mistake is using $\to$ as the main connective with $\exists$: $\exists x At(x, POLIMI) \to Smart(x)$.

### Properties of quantifiers
$\forall x \forall y$ is the same as $\forall y \forall x$ and $\exists x \exists y$ is the same as $\exists y \exists x$.

$\forall x \exists y$ is not the same as $\exists x \forall y$:
- $\exists x \forall y Loves(𝑥, 𝑦)$ means “There is a person who loves everyone in the world”
- $\forall x \exists y Loves(𝑥, 𝑦)$ means “Everyone in the world is loved by at least one person”

**Quantifier duality**: each can be expressed using the other:
- $\forall 𝑥 Likes(𝑥, IceCream) ≡ \lnot \exists 𝑥 \lnot Likes(𝑥, IceCream)$
- $\exists 𝑥 Likes(𝑥, Broccoli) ≡ \lnot \forall 𝑥 \lnot Likes(𝑥, Broccoli)$

## Translation from first order logic to propositional logic
The translation is possible when the domain of discourse contains only a finite number of
objects.

1. Systematically replace all variables with the available constants, considering that in case, e.g., of constants $A_1$ to $A_n$:
	- $\forall x P(x)$ becomes $P(A_1) \land ... \land P(A_n)$
	- $\exists x P(x)$ becomes $P(A_1) \lor ... \lor P(A_n)$
2. The atomic sentences $P(A_i)$ are replaced by propositional symbols:
	- $P(A_1) \land ... \land P(A_n)$ becomes $PA_1 \land ... \land PA_n$
	- $P(A_1) \lor ... \lor P(A_n)$ becomes $PA_1 \lor ... \lor PA_n$
    
The number of propositional symbols can be limited by considering that some assignments of
constant to variables are meaningless.

Examples:
| Natural language | First order logic | Propositional logic |
| - | - | - |
| Those who like opera, like both music and theatre | $\forall x (L(x, O) \to L(x,M) \land L(x,T))$ | $(𝐿𝐴𝑂 → 𝐿𝐴𝑀 ∧ 𝐿𝐴𝑇) ∧ (𝐿𝐵𝑂 → 𝐿𝐵𝑀 ∧ 𝐿𝐵𝑇)$ |
| Alice likes music, but she does not like theatre | $L(A,M) \land \lnot L(A,T)$ | $𝐿𝐴𝑀 ∧ ¬𝐿𝐴𝑇$ |
| Bob likes exactly the same things that Alice likes | $\forall x (L(A,x) ↔ L(B,x))$ | $(𝐿𝐵𝑀 ↔ 𝐿𝐴𝑀) ∧ (𝐿𝐵𝑂 ↔ 𝐿𝐴𝑂) ∧ (𝐿𝐵𝑇 ↔ 𝐿𝐴𝑇)$ |
| Bob does not like opera | $\lnot L(B,O)$ | $¬𝐿𝐵𝑂$ |