---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 10-ir-based-databases-elk
chapter_title: 10 IR Based Databases - ELK
created_at: '2021-12-29T11:23:12.000000Z'
id: 42
priority: 2
slug: 03-elasticsearch-operations
title: 03 Elasticsearch operations
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 03 Elasticsearch operations

Creating and index: `PUT /index_name`

Define a mapping:
```json
PUT /my_index/_mapping
{
  "properties": {
    "<field_name>": {
      "type": "text"
    }
  }
}
```

Retrieve a document using its _id: `GET /nyc-restourants/_doc/xxxxxxxxxx`

## Search
Match: 
```json
GET /nyc-restourants/_search
{
  "query": {
    "match": {
      "<field>": <value>
    }
  }
}
```
Boolean:
```json
GET /nyc-restourants/_search
{
  "query": {
    "bool": {
      "must": [{}],
      "must_not": [{}],
      "should": [{}]
    }
  }
}
```

### Filters
- Exact match
- For fields that are not analyzed
- No relevance
- The filter is either satisfied or not
- Cacheable
```json
GET /nyc-restourants/_search
{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "<field>": <value>
        }
      }
    }
  }
}
```
```json
GET /nyc-restourants/_search
{
  "query": {
    "bool": {
      "filter": {
        "prefix": {
          "<field>": <value>
        }
      }
    }
  }
}
```

## Count
```json
GET /nyc-restourants/_count
{
  "query": {
    "match": {
      "<field>": <value>
    }
  }
}
```

## Aggregations
```json
GET /nyc-restourants/_search
{
  "size": 0,
  "aggs": {
    "score_group": {
      "term": {
        "field": "<field_name>"
      }
    }
  }
}
```