---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 06-graph-stores
chapter_title: 06 Graph Stores
created_at: '2021-12-26T13:08:24.000000Z'
id: 19
priority: 1
slug: 02-graph-databases
title: 02 Graph Databases
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 02 Graph Databases

# Motivations
The table based structure of relational databases makes it hard to represent
relationships between rows in the same table,and moreover whenever someone
needs to find a relationship between records of different tables the db has to
perform a **JOIN operation, which is usually very expensive**.

So for the use cases in which relationships are the most important feature of our
data (e.g. social network friendships) it would be best to go with a technology
who can implement relationships in a native and efficient way,and that’s where
graph dbs come in.

# Definition
"Database that uses graph structures with nodes, edges and
properties to store data"

Graphs provides **index-free adjacency**: every node is a pointer to its adjacent element. Edges hold most of the important information.

In these kind of storage systems data are represented as entities connected by
information rich relations,just like in a real graph.
[![](../../../images/542b1c0c59_BikidkYjIG43PQnB-image-1640524437323.png)](../../../images/542b1c0c59_BikidkYjIG43PQnB-image-1640524437323.png)

# Query model
The typical query based approach for managing data in relational databases isn’t
a good fit for graph dbs,in these cases it’s preferred a different approach called
**Graph Matching**, or more in general **Pattern Matching**. In these technique the
user specifies a particular shape or structure he wants to find in the graph, and
the system searches for and returns all the subgraphs that match that request.