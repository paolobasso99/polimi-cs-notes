---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 08-key-value-databases
chapter_title: 08 Key-value Databases
created_at: '2021-12-28T14:28:02.000000Z'
id: 33
priority: 0
slug: 01-introduction-815
title: 01 Introduction
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 01 Introduction

In many applications **performance is an essential priority**, and often a small
delay in response time could mean a big financial loss.

For these kind of needs key-value stores were built, a type of db which guarantees
the best possible lookup time of any storage system.

Key-value stores are build upon the assumption that any entity can be seen as
a value pointed by a key, and so when you are looking for a certain value you
need to search for the key associated to it.

In these contest keys are just used to retrieve a specific value, unlike relational
databases where primary and foreign keys are means to do searches and mapping
between tables; this obviously grants a significant speed boost during reads.

Key-Value stores can be used to improve performance at many different levels:
- Database
- Caching Layers
- Message Brokers

# Caching
A cache is a collection of data
duplicating original values stored elsewhere or computed
earlier, where the original data is expensive to fetch
(owing to longer access time) or to compute, compared to
the cost of reading the cache.

Caches are only efficient when the benefits
of faster access outweigh the overhead of
checking and keeping your cache up to date.

> There are only two hard things in Computer Science: cache invalidation and naming things.
-- Phil Karlton.