---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 11-hadoop
chapter_title: 11 Hadoop
created_at: '2022-01-01T12:55:45.000000Z'
id: 66
priority: 6
slug: scheduling
title: Scheduling
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# Scheduling

By default, Hadoop uses **FIFO** to schedule
jobs.
Alternate scheduler options:
*capacity* and *fair*

## Capacity Scheduler
- Jobs are submitted to queues
- Jobs can be prioritized
- Queues are allocated a fraction of the total resource
capacity
- Free resources are allocated to queues beyond their
total capacity
- No preemption once a job is running

## Fair scheduler
- Provides fast response times for small jobs
- Jobs are grouped into Pools
- Each pool assigned a guaranteed minimum share
- Excess capacity split between jobs
- By default, jobs that are uncategorized go into a
default pool.
- Pools have to specify the minimum number of map
slots, reduce slots, and a limit on the number of
running job