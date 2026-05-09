---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 09-columnar-databases
chapter_title: 09 Columnar Databases
created_at: '2021-12-29T10:09:25.000000Z'
id: 39
priority: 3
slug: 04-cassandra-query-language
title: 04 Cassandra Query Language
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 04 Cassandra Query Language

To query the data stored within Cassandra, a dedicated query language named
Cassandra Query Language (CQL) was developed.

CQL offers a model similar to MySQL under many different aspects
- It is used to query data stored in tables
- Each table is made by rows and columns
- Most of the operators are the ones used in MySQL

CQL commands and queries can either be run in the console or by reading a textual file
with the corresponding command.

## Keyspace
```cql
CREATE KEYSPACE population
WITH replication = {‘class’: ‘SimpleStrategy’,
                    ‘replication_factor’: 3};
```
The **DESCRIBE** command can be used to check whether a keyspace (or a table) has
been correctly created. It can also be applied to other elements.
```cql
DESCRIBE keyspaces;
```
To be able to perform the operations on the tables (that we still have to create), we must
choose in which keyspace we want to work. The command **USE** covers such need.
```cql
USE population;
```
Keyspaces can be also modified (**ALTER**) and deleted (**DROP**) with the corresponding
commands.
```cql
ALTER KEYSPACE <identifier> WITH <properties>;
```
```cql
DROP KEYSPACE <identifier>;
```
## Tables
```cql
CREATE TABLE <table_name> (
  <column_name> <column_type>,
  <column_name> <column_type>,
  ...
)
```
Optionally, some options can be included by using **WITH \<options>**.

```cql
CREATE TABLE person (
  personal_id text,
  name text,
  age varint,
  birth_date text,
  gender text,
  PRIMARY KEY (personal_id, text)
);
```
```cql
DESCRIBE tables;
DESCRIBE person;
```
When creating the **PRIMARY KEY** of the table as the last definition within the CREATE
TABLE operation, the columns that you put within the PRIMARY KEY statement have
different meaning depending on the order and the brackets.

The first value (or set of values) is named **Partition Key(s)**. It defines the way in which the data is partitioned within the cassandra nodes.
The second value (or sets of values) is named **Clustering Key(s)**. It is used to define the
way in which the data is stored within a partition. A table can employ many different Clustering and/or Partition Keys.

When creating a table, clustering keys can be used to define an ordering.
```cql
CREATE TABLE person (...)
WITH CLUSTERING ORDER BY (text ASC, ...);
```

Tables can be also modified through the **ALTER** command:
```cql
ALTER TABLE <table_name> <instructions>;
ALTER TABLE <table_name> ADD <column_name> <column_type>;
ALTER TABLE <table_name> DROP <column_name>;
```

Tables can be also deleted through the **DROP** command:
```cql
DROP TABLE <table_name>;
```
Rather than deleting the table, it is possible to empty it through the **TRUNCATE** command:
```cql
TRUNCATE TABLE <table_name>;
```

## Indexes
Indexes are one of the most important elements of a table in Cassandra. They allow to
query the column efficiently.

**Secondary Indexes** are created with the following command:
```cql
CREATE INDEX <identifier>
ON <table_name> (<column_name>);
```
```cql
CREATE INDEX person_name
ON person (name);
```
```cql
DROP INDEX index_name
```

## Data
Insert:
```cql
INSERT INTO <tablename>(<column_name1>,
<column_name2>, ...)
VALUES (<column_value1>, <column_value2>....)
USING <option>;
```
```cql
INSERT INTO person(personal_id, address, age,
birth_date, gender, name)
VALUES (‘FRNTRZ95E12F675T’, ‘Via Milano 12’,
26, ‘12-05-1995’, ‘Male’, ‘Francesco Terzani’);
```
Select:
```cql
SELECT <field_list>
FROM <table_name>
WHERE <conditions>
```
```cql
SELECT *
FROM person
WHERE personal_id = ‘FRNTRZ95E12F675T’
```
Being Cassandra a column-oriented database, all the operations
are optimized to extract data from columns. To solve this issue, it’s **necessary to query with
respect to the attributes included in the primary key or to create a secondary index**.

Update:
```cql
UPDATE <table_name>
SET <column_name> = <new_value>, ...
WHERE <condition>;
```
```cql
UPDATE person
SET address = ‘Via Milani 13’
WHERE personal_id = ‘FRNTRZ95E12F675T’;
```
Delete (only on primary key):
```cql
DELETE
FROM <table_name>
WHERE <condition>;
```
```cql
DELETE
FROM person
WHERE personal_id = ‘FRNTRZ95E12F675T’;
```
Batch:
```cql
BEGIN BATCH
<insert_statement>;
<update_statement>;
<delete_statement>;
APPLY BATCH;
```

## Utilities
The **CAPTURE** command followed by the path of the folder in which store the results and
the name of the file.
```cql
CAPTURE D:/Program Files/Cassandra/Outputs/output.txt;
```
```cql
CAPTURE off;
```
The **EXPAND** command provides extended outputs within the console when performing
queries. It must be executed before the query to enable it.
```cql
EXPAND on;
```
```cql
EXPAND off;
```
The **SOURCE** command allows you to run queries from textual files. The command
accepts the path to the file with the query.
```cql
SOURCE D:/Program Files/Cassandra/Queries/query_1.txt;
```

## Data Types
Cassandra supports many different data types, like text, varint, float, double, Boolean, etc.

In particular, it supports two particular data types
- collections
- user-defined data types

Collections are pretty easy to define and update:
```cql
CREATE TABLE test(email list<text>, ...);
UPDATE test SET email = email + [...] WHERE ...;
```

To create a user-defined data type:
```cql
CREATE TYPE <type_name> (
  <column_definition>
  ...
);
DESCRIBE TYPE <type_name>;
```