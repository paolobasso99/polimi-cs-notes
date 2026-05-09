---
book_slug: cs-computer-security
book_title: CS Computer Security
chapter_slug: web-security
chapter_title: Web security
created_at: '2022-06-17T16:06:18.000000Z'
id: 160
priority: 3
slug: cookies-and-sessions
title: Cookies and sessions
type: page
updated_at: '2022-06-17T16:40:49.000000Z'
---

# Cookies and sessions

HTTP is stateless and almost uniderectionl. Web application, on the other hand, need to keep a state.

Cookies is a client side information storage, a reliable mechanism to keep stateful information.

Cookies are used for session creation:
[![](../../../images/9a240c5ae6_gwHEgTuP3oCBIUES-image-1655483789055.png)](../../../images/9a240c5ae6_gwHEgTuP3oCBIUES-image-1655483789055.png)

The cookie will also be used for session identification.

## Issues with cookies and sessions
- Concurrency: what if two clients access the site simulaneously?
- Session termintation: when and how to terminate sessions?
- Data storage on the server side
- The token must be unpredictable