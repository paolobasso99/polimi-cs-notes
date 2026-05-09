---
book_slug: cs-computer-security
book_title: CS Computer Security
chapter_slug: introduction-authentication-and-access-control
chapter_title: Introduction, authentication and access control
created_at: '2022-06-17T09:15:31.000000Z'
id: 148
priority: 0
slug: introduction-to-computer-security
title: Introduction to computer security
type: page
updated_at: '2022-06-17T12:59:47.000000Z'
---

# Introduction to computer security

## CIA Paradigm
The CIA paradigm for information security states three desiderata:
- **Confidentiality**: information should be accessed only by authorized entities.
- **Integrity**: information should be modifies only by authorized entities, and only in the way such entities are entitled to modify it.
- **Availability**: information must be available to all the parties who have a right to access it, within specified time constraints.

## Vulnerabilities and exploits
A **vulnerability** is something that allows to violate one of the constraints of the CIA paradigm.

An **exploit** is a *specific way* to use one or more vulnerabilities to accomplish a specific objective that violates the constraints.

## Risk assesment
To properly define risk we need to define first:
- An **asset** identifies what is valuable for an organization. For example: hardware equipments, software, data, reputation.
- A **threat** is a circumstance which could potentially cause a CIA violation. For example: denial of service, identity theft, data leak.
- An **attack** is an intentinal use of one or more exploits with the objective of compromising a system's CIA.
- A **threat agent** is whoever may cause an attack to occur.

With these definitions we can say that **risk** is the statistical and economical evaluation of the exposure to damage because of the presenc of vulnerabilities and threats.
$$ \text{Risk} = \text{Asset} \times \text{Vulnerabilities} \times \text{Threats} $$

Where the controllable variable are the asset (value, potential damage) and vulnerabilities (which will always be present in some degree), while the threats is the not controllable varialbe.

**Security** is, in essence, the balance between the reduction of vulnerabilities + damage controll and the **cost**. Increasing the level of security has a cost, both direct (management, operational, equipment) and indirect (usability, performance, privacu, productivity).

## Trust and assumptions
We must set bundaries: part of the system will be **assumed** secure. This parts will be **trusted elements**.

We are forced to define a **trusted bundary** because there is no end to how deep we could look into things.

Trusted elements are not "trustworthy" but are assumed secure because we need to do so at some point.