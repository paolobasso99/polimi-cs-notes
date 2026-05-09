---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 05-nosql-introduction
chapter_title: 05 NoSQL introduction
created_at: '2021-12-26T12:03:39.000000Z'
id: 15
priority: 1
slug: 02-transactional-properties-in-nosql
title: 02 Transactional Properties in NoSQL
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 02 Transactional Properties in NoSQL

# Transaction is SQL, ACID
In the relational world we are used to having the concept of a transaction, an
elementary unit of work encapsulated by begin and commit commands characterized by **ACID properties**:
- **Atomicity**: the operations contained in a transaction either all fail or all
succeed
- **Consistency**: the state of the db is respects the integrity constraints before
and after the transaction is executed
- **Isolation**: every transaction doesn’t affect and isn’t affected by other con-
current transactions
- **Durability**: a transaction produces durable changes in a db

These properties are very important and often even fundamental in a traditional
SQL based **OLTP application**, which are capable of providing the
definition and execution of transactions on behalf of multiple, concurrent
applications.

## Well formed transactions
- begin transaction
- code for data manipulation (reads and writes)
- commit work – rollback work
- no data manipulation after commit - rollback
- end transaction

# Transactions in NoSQL, CAP
Big Data systems who have an architecture based on horizontal scalability and
distributed systems unfortunately can’t give complete ACID transactions guarantees.

CAP is a word composed by the initials of 3 important features in distributed
systems:
- **Consistency**: all nodes see the same data at the same time
- **Availability**: Node failures do not prevent other survivors from continu-
ing to operate (a guarantee that every request receives a response about
whether it succeeded or failed)
- **Partition Tolerance**: the system continues to operate despite arbitrary
partitioning due to network failures (e.g., message loss)

The CAP theorem says that **a distributed system can satisfy any two of these guarantees at the same time
but not all three.**

In big data system who rely heavily on network comunication
**Partition Tolerance is essential**, so designing a distributed system means having
to handle a tradeoff between Availability and Consistency.

The extreme choice
would be to abandon completely one between this 2 features, but in real system
the data engineer needs to finetune the level of Consistency and Availability to
the need of the service.

- **AP**: A partitioned node returns a correct value, if in a consistent state;
a timeout error or an error, otherwise e.g., DynamoDB, CouchDB, and
Cassandra (banking applications)
- **CP**: A partitioned note returns the most recent version of the data, which
could be stale. e.g., MongoDB, Redis, AppFabric Caching, and MemcacheDB (media streaming, statistics, social media, news)

## BASE features
A new, weaker, and generic set of characteristics called BASE has been invented to describe features of big data systems.

- **Basic Availability**: the system can always fulfill requests, but the answer
could be partially consistent
- **Soft State**: The solid state of relational system is abandoned
- **Eventual Consistency**: At some point in the future data will converge to
a consistent state (consistent state is not granted immediately but eventually)

These features are voluntarily vague and generic since they can be finetuned to
the needs of the application as stated by the CAP theorem.

Some notes about BASE vs ACID:
- Given BASE’s loose consistency, developers need to be more
knowledgeable and rigorous about consistent data if they choose a BASE
store for their application.
- Planning around BASE limitations can sometimes be a major disadvantage
when compared to the simplicity of ACID transactions.
- A fully ACID database is the perfect fit for use cases where data reliability
and consistency are essential.

# ORM - Object-Relational Mapping
When developing applications the most used paradigm is object-oriented programming. However, using SQL, data is not stored as objects but as table with columns and rows.

There is a mismatch on the handling of data from the storage to the use in an application.

This mismatch can be solved in the NoQL world, breaking ACID.