---
book_slug: cs-computer-security
book_title: CS Computer Security
chapter_slug: software-security
chapter_title: Software security
created_at: '2022-06-18T23:37:44.000000Z'
id: 172
priority: 1
slug: introduction-to-software-security
title: Introduction to software security
type: page
updated_at: '2022-06-19T09:27:49.000000Z'
---

# Introduction to software security

Security is a **non-functional** requirement of software engineering. Creating inherently secure applications is a fundamental, yet often unknown, skill for a good developer or software engineer.

A **vulnerability** is software is an unmet security specification. Bug-free software does not exist and not all bugs lead to vulnerabilities.

Even if a vulnerability exists, there may not be an **exploit** for it.

The key issues in secure designs are:
- Reduce privileged parts to a minimum
- Keep it simple
- Discard privileges definitively as soon as possible
- Open design: not rely on obscurity
- Take care of concurrency and race conditions
- Fail-safe and default deny.
- Filter the input and the output.
- Use trusted libraries
- Use trusted entropy sources such as /dev/urandom