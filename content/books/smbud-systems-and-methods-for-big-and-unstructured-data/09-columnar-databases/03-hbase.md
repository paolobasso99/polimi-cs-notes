---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 09-columnar-databases
chapter_title: 09 Columnar Databases
created_at: '2021-12-29T10:01:22.000000Z'
id: 38
priority: 2
slug: 03-hbase
title: 03 HBase
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 03 HBase

[![](../../../images/f53121877f_auhe0vmXIiXebRzD-image-1640772201172.png)](../../../images/f53121877f_auhe0vmXIiXebRzD-image-1640772201172.png)

- **HBase Table**: Split it into multiple regions: replicated across servers.
- One Store per ColumnFamily (subset of columns with similar query patterns)
per region.
- Memstore for each Store: in-memory updates to Store; flushed to disk when full.
- StoreFiles (**HFile**) for each store for each region: where the data live 

**Strong consistency** (different from Cassandra): **HBase Write-Ahead Log**