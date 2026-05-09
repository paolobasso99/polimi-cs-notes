---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 11-hadoop
chapter_title: 11 Hadoop
created_at: '2021-12-31T14:09:28.000000Z'
id: 63
priority: 3
slug: hadoop-20
title: Hadoop 2.0
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# Hadoop 2.0

## YARN
- Splits up the two major functions of JobTracker
	- **Global Resource Manager** - Cluster resource management
	- **Application Master** - Job scheduling and monitoring (one per application).
- The Application Master negotiates resource containers from the Scheduler,
tracking their status and monitoring for progress. Application Master itself
runs as a normal container.
	- Tasktracker
	- NodeManager (NM) - A new per-node slave is responsible for launching
the applications’ containers, monitoring their resource usage (cpu,
memory, disk, network) and reporting to the Resource Manager.
- YARN maintains compatibility with existing MapReduce applications and
users.

[![](../../../images/93582cc752_V156l9Vls0PpIZls-image-1640959887162.png)](../../../images/93582cc752_V156l9Vls0PpIZls-image-1640959887162.png)

### Classic MapReduce vs. YARN
**Fault Tolerance and Availability**:
- Resource Manager
	- No single point of failure – state saved in ZooKeeper
	- Application Masters are restarted automatically on RM restart
- Application Master
	- Optional failover via application-specific checkpoint
	- MapReduce applications pick up where they left off via state saved in HDFS

**Wire Compatibility**:
- Protocols are wire-compatible
- Old clients can talk to new servers
- Rolling upgrades

Support for programming paradigms other than MapReduce (**Multi tenancy**)