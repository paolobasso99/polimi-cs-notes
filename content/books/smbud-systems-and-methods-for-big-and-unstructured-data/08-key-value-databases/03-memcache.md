---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 08-key-value-databases
chapter_title: 08 Key-value Databases
created_at: '2021-12-28T14:51:52.000000Z'
id: 35
priority: 2
slug: 03-memcache
title: 03 Memcache
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 03 Memcache

Memcache is a free & open source, high-performance,
distributed memory object caching system that works as **key/value dictionary**. It is **generic in nature**, intended for use in
speeding up dynamic web applications by
alleviating database load.

It is useful to store:
- high demand (used often)
- expensive results (hard to compute)
- common (shared accross users)

It is implemented as a server which provides access over TCP or UDP and it follows these principles:
- Fast network access (memcached servers close to other
application servers)
- No persistency (if your server goes down, data in memcached is
gone)
- No redundancy / fail-over
- No replication (single item in cache lives on one server only)
- No authentication (not in shared environments)
- 1 key is maximum 1MB
- keys are strings of 250 characters (in
application typically MD5 of user readable
string)
- No enumeration of keys (thus no list of
valid keys in cache at certain moment)
- No active clean-up (only clean up when
more space needed, LRU: Least Recently
Used )

Memcache supports **multiget** which fetch multiple keys from memcached in
one single call.