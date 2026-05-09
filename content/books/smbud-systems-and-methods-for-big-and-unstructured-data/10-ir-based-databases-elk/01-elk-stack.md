---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 10-ir-based-databases-elk
chapter_title: 10 IR Based Databases - ELK
created_at: '2021-12-29T10:52:41.000000Z'
id: 40
priority: 0
slug: 01-elk-stack
title: 01 ELK stack
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 01 ELK stack

- **Kibana**: Visualize and Manage
- **Elasticsearch**: Store, Search and Analyze
- **Logstash + Beats**: Ingest
[![](../../../images/e4137a62e7_OwnBOxjQ1aixYcIK-image-1640775233861.png)](../../../images/e4137a62e7_OwnBOxjQ1aixYcIK-image-1640775233861.png)

## Elasticsearch
Elasticsearch is the core of the Elastic Stack.

It’s a search and analytic engine
- Near real-time
- Full-text search
- Distributed (JSON format data storage)
- RESTful

## Logstash
- Streaming ETL engine
- Provides centralized data collection,
processing and enrichment on the fly
- Data agnostic
- Wide range of integrations and
processors
- Ready-to-use monitoring and
administrative panes built in Kibana

## Beats
- Platform for data shippers
- Collect and ship logs and metrics
from hosts or containers
- Many available
	- Filebeat
	- Metricbeat
    - Packetbeat
    - Heartbeat

## Kibana
- Kibana is an open source data visualization dashboard
- It provides visualization capabilities on top of the content
indexed on an Elasticsearch cluster.
- Kibana is simple and pretty intuitive to begin with. Despite
such simplicity, it is highly customizable, allowing complex
and detailed representations.