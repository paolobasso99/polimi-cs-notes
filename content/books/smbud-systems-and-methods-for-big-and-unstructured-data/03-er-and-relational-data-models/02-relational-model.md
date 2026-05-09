---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 03-er-and-relational-data-models
chapter_title: 03 ER and Relational Data Models
created_at: '2021-12-24T21:24:55.000000Z'
id: 9
priority: 1
slug: 02-relational-model
title: 02 Relational Model
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 02 Relational Model

## Keys
**Superkey**: a set of attributes K is a superkey for a relation r if r does not contain two distinct tuples t1 and t2 with t1[K]=t2 [K];

**Key**: K is a key for r if K is a minimal superkey (that is, there exists no other superkey K’ of r that is contained in K as proper subset)

**Primary Keys**: A selected key of the relation which has no null values.
Primary keys are used to identify relation instances and to correlate data in different relations (**Foreign key**)

## Referential constraints
A referential constraint imposes to the values on a set X of
attributes of a relation R1 to appear as values for the primary
key of another relation R2

## Normal Forms and Normalization
The goal of normalization is to create a set of relational
tables that are free of redundant data and that can be
consistently and correctly modified or updated.

This means that all tables in a relational database should
be in the third normal form (3NF).

### Functional Dependencies
A column, Y, of the relational table R is said to be functionally dependent
upon column X of R if and only if each value of X in R is associated with
precisely one value of Y at any given time.

It is the same as saying the values of column X identify the values of column
Y.

If column X is a primary key, then all columns in the relational table R must
be functionally dependent upon X.

### First Normalization Form 1FN
Eliminate duplicative columns from the same table.
No multivalued attributes
Every attribute value is atomic
(i.e. no sets of values within a column)

Create separate tables for each group of related data and
identify each row with a unique column or set of columns (the
primary key).

### Second normal form 2NF
Any non-key columns must depend on the entire primary
key. In the case of a composite primary key, this means
that a non-key column cannot depend on only part of the
composite key.

A relation R is in 2nf if every non-primary attribute A in R
is fully Functionally dependent on the primary key.

### Third normal form 3NF
Remove columns that are not dependent upon the
primary key.

Third Normal Form (3NF) requires that all columns
depend directly on the primary key.

2NF plus no transitive dependencies (functional
dependencies on non-primary-key attributes)

### BCNF
Boyce–Codd normal form (or BCNF or 3.5NF) is a
slightly stronger version of the 3NF.

For every one of its dependencies X → Y, at least
one of the following conditions hold:
- X → Y is a trivial functional dependency (Y ⊆ X)
- X is a superkey for schema R