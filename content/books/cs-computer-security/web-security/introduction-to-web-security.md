---
book_slug: cs-computer-security
book_title: CS Computer Security
chapter_slug: web-security
chapter_title: Web security
created_at: '2022-06-17T15:26:05.000000Z'
id: 156
priority: 0
slug: introduction-to-web-security
title: Introduction to web security
type: page
updated_at: '2022-06-17T16:06:39.000000Z'
---

# Introduction to web security

[![](../../../images/1abb988d40_ERIdJChbJ63R4OPg-image-1655479599783.png)](../../../images/1abb988d40_ERIdJChbJ63R4OPg-image-1655479599783.png)

Web application are built on top of HTTP, which is a **stateless** protocol that has only weak authentication built in. State and authentication are emulted by the application, they are not embedded in the protocol.

In this environment the golden rule is that the **client is never trustworthy**: we need to **filter** anche check carefully anything that it is sent to us.

The problem is that **filtering is hard**. There are varius way of filtering:
- **whitelisting**: only allowing through what we expect
- **blacklisting**: discard known bad stuff
- **escaping**: transform special characters into something else less dangerous

The basic rule is that *whitelisting is safer than blacklisting**.