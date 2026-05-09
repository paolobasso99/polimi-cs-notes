---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 14-data-wrangling
chapter_title: 14 Data Wrangling
created_at: '2021-12-29T12:44:12.000000Z'
id: 45
priority: 0
slug: 01-the-challange-and-importance-of-data-wrangling
title: 01 The challange and importance of data wrangling
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# 01 The challange and importance of data wrangling

The step after Data Acquisition and before Analysis in the data management
flow is Data Wrangling, also called Data Cleaning or Data Preparation.

In this step data is cleaned, tested and prepared to be the best input possible
for the analysis process. In other words,we need to ensure that our data has high
quality, which is a property defined by this metrics:
- **Accuracy**: The data was recorded correctly.
- **Completeness**:All relevant data was recorded.
- **Uniqueness**:Entities are recorded once.
- **Timeliness**: The data is kept up to date (and time consistency is granted).
- **Consistency**: The data agrees with itself.

Unfortunately it isn’t easy to measure and define these metrics. In fact, these metrics could be:
- **Unmeasurable**: Accuracy and completeness are extremely difficult, per-
haps impossible to measure.
- **Context independent**: No accounting for what is important. E.g., if you
are computing aggregates,you can tolerate a lot of inaccuracy.
- **Incomplete**: What about interpretability, accessibility, metadata, analysis,
etc.
- **Vague**: The conventional definitions provide no guidance towards practi-
calimprovements of the data.

For these reasons data wrangling is often the most crucial, difficult and predominant task of a data scientist/engineer.

If the data wrangling step is done poorly, it may lead to analysis being run on
bad data which could in turn lead to bad decision making in company and bad
business.

[![](../../../images/35b08bdffa_1uYgRfI2sF76uBwt-image-1640782123293.png)](../../../images/35b08bdffa_1uYgRfI2sF76uBwt-image-1640782123293.png)