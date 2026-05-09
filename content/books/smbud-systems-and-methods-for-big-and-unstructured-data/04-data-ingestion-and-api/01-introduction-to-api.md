---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 04-data-ingestion-and-api
chapter_title: 04 Data ingestion and API
created_at: '2021-12-26T10:08:00.000000Z'
id: 10
priority: 0
slug: 01-introduction-to-api
title: 01 Introduction to API
type: page
updated_at: '2022-01-11T22:51:59.000000Z'
---

# 01 Introduction to API

# Data ingestion
Data ingestion is the first and fundamental step of any Data Analysis Pipeline.
The focus of this section is on how is it possible to collect data from publicly
available sources over the web.
It is in fact a common practice nowadays to integrate the proprietary data
coming from OLTP databases with data coming from public web resources in
order to also have a data source which isn’t coming from the Company domain
and (and could as such be biased in many ways).

The **goal of both web scraping and APIs is to access web data**. Web scraping allows
you to extract data from any website through the use of web scraping software. On the other
hand, APIs give you direct access to the data you’d want

# Definition of API
## What
"An API (Application Program Interface) is a set of routines, protocols and tools for building software application"

A WebAPI is just an HTTP based API.

## Why
- Separation between model and presentation
- Regulate access to the data
	- Traceable accounts
    - Enable access to only a portion of the available data
    - Impose limits
- Avoid direct access to the platform website
- Request throttling
- Provide paid access to full (or higher volume) data

## Limitations
1. **Availability and Lack of Customization**: Not all websites have an API today. Then APIs do not provide access to all the data available.
2. **Rate Limits**: Considering that the website provides an API, it doesn’t necessarily mean that you can
harvest as much data as you want. Rate limits are a major problem for APIs. 
3. **Legality**: With data scraping, you will always face the issue of legality. API supporters often claim
that data scraping with API is completely legal and doesn’t violate any rules. However, this
is not always the case

# HTTP requests
Following the HTTP protocol when making a request you need to specify the verb and the url.

Some of the most used verbs are: 
- GET
- POST
- PUT
- DELETE
- ...

## Parameters
An endpoint can be tweaked using parameters appending to the url some encoded strings.