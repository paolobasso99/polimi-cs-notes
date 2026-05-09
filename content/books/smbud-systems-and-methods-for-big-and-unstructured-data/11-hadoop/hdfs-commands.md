---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 11-hadoop
chapter_title: 11 Hadoop
created_at: '2021-12-31T14:01:16.000000Z'
id: 62
priority: 2
slug: hdfs-commands
title: HDFS Commands
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# HDFS Commands

## Shell Commands
There are two types of shell commands:
1. **User Commands**
	- `hdfs dfs` – runs filesystem commands on the HDFS
	- `hdfs fsck` – runs a HDFS filesystem checking command
2. **Administration Commands**
	- `hdfs dfsadmin` – runs HDFS administration commands
    
The generic command line syntax is:
```bash
hdfs command [genericOptions] [commandOptions]
```
    
### User Commands
List directory contents
```bash
hdfs dfs –ls
hdfs dfs -ls /
hdfs dfs -ls -R /var
```
Display the disk space used by files
```bash
hdfs dfs -du -h /
hdfs dfs -du /hbase/data/hbase/namespace/
hdfs dfs -du -h /hbase/data/hbase/namespace/
hdfs dfs -du -s /hbase/data/hbase/namespace/
```
Copy data to HDFS
```bash
hdfs dfs -mkdir tdata
hdfs dfs -ls
hdfs dfs -copyFromLocal tutorials/data/geneva.csv tdata
hdfs dfs -ls –R
```
Copy the file back to local filesystem
```bash
cd tutorials/data/
hdfs dfs –copyToLocal tdata/geneva.csv geneva.csv.hdfs
md5sum geneva.csv geneva.csv.hdfs
```
List acl for a file
```bash
hdfs dfs -getfacl tdata/geneva.csv
```
List the file statistics – (%r – replication factor)
```bash
hdfs dfs -stat "%r" tdata/geneva.csv
```
Write to hdfs reading from stdin
```bash
echo "blah blah blah" | hdfs dfs -put - tdataset/tfile.txt
hdfs dfs -ls –R
hdfs dfs -cat tdataset/tfile.txt
```
Removing a file
```bash
hdfs dfs -rm tdataset/tfile.txt
hdfs dfs -ls –R
```
List the blocks of a file and their locations
```bash
hdfs fsck /user/cloudera/tdata/geneva.csv -
files -blocks –locations
```
Print missing blocks and the files they belong to
```bash
hdfs fsck / -list-corruptfileblocks
```

## Adminstration Commands
Comprehensive status report of HDFS cluster
```bash
hdfs dfsadmin –report
```
Prints a tree of racks and their nodes
```bash
hdfs dfsadmin –printTopology
```
Get the information for a given datanode (like ping)
```bash
hdfs dfsadmin -getDatanodeInfo localhost:50020
```
Get a list of namenodes in the Hadoop cluster
```bash
hdfs getconf –namenodes
```
Dump the NameNode fsimage to XML file
```shell
cd /var/lib/hadoop-hdfs/cache/hdfs/dfs/name/current
hdfs oiv -i fsimage_0000000000000003388 -o
/tmp/fsimage.xml -p XML
```