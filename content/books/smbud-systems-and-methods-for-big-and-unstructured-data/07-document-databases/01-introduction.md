---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 07-document-databases
chapter_title: 07 Document Databases
created_at: '2021-12-28T12:55:33.000000Z'
id: 30
priority: 0
slug: 01-introduction
title: 01 Introduction
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 01 Introduction

Document databases deviate from the entity-based
denormalized data model of relational dbs and prefer an approach based on **denormalized and aggregated data** typical of business document.

A document is a complex object made up of what would be many different SQL
tables, and so it can be composed of different pieces of data with different struc-
tures.

Some of the advantages of document stores are:
- **Flexible** structure that handles well schema changes
- **Solves mismatches impedance problems**: document structure is more in line with how developers construct classes
- **JSON compatibility**, which guarantees very ease of integration with web technologies

## Sharding
Sharding is a means of partitioning data across servers to enable:
- **Scale**: needed by Modern applications to support massive workloads and data volume.
- **Geo-Locality**: to support geographically distributed deployments to support optimal UX for customers across vast geographies.
- **Hardware Optimizations**: on Performance vs. Cost
- **Lower Recovery Times**: to make “Recovery Time Objectives” (RTO) feasible.

Sharding involves a **shard key** defined by a data modeler that
describes the partition space of a data set.

Data is partitioned into **data chunks** by the shard key, and these
chunks are **distributed evenly across shards** that reside across
many physical servers