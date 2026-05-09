---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 12-13-hadoop-subprojects
chapter_title: 12-13 Hadoop Subprojects
created_at: '2022-01-01T14:02:28.000000Z'
id: 73
priority: 7
slug: sqoop
title: Sqoop
type: page
updated_at: '2022-01-01T14:07:35.000000Z'
---

# Sqoop

Sqoop is a command-line interface application for **transferring data between relational databases and Hadoop**.

Sqoop **supports incremental loads** of a single table or a free form SQL query as well as saved jobs which can be run multiple times to import updates made to a database since the last import. Imports can also be used to populate tables in Hive or HBase. Exports can be used to put data from Hadoop into a relational database. Sqoop got the name from **"SQL-to-Hadoop"**.

## Command Line Instructions
```shell
sqoop import \
--connect jdbc:mysql://localhost:3306/nseProd \
--username=qt \
--password=password \
--table=tradingDays \
--target-dir /mysql/nseProd \
--m 1
```

Sqoop uses the primary key to decide how
many mappers to use, and for splitting the
rows among mappers.

Instead of full tables Sqoop supports a query based importer:
`--query 'select year, month, day from
tradingDays where year=2016 and $CONDITIONS'`

Can define jobs:
```shell
sqoop job \
--create myjob \
--import \
--connect jdbc:mysql://localhost:3306/nseProd \
--username=qt \
--password=password \
--table=tradingDays \
--target-dir /mysql/nseProd \
--m 1
```

Which can be incremental: `--incremental lastmodified
—check-column ts`

Jobs can then be executed: `sqoop job --exec myjob`