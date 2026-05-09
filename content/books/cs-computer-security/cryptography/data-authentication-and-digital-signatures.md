---
book_slug: cs-computer-security
book_title: CS Computer Security
chapter_slug: cryptography
chapter_title: Cryptography
created_at: '2022-06-18T14:54:58.000000Z'
id: 168
priority: 6
slug: data-authentication-and-digital-signatures
title: Data authentication and digital signatures
type: page
updated_at: '2022-06-18T14:59:24.000000Z'
---

# Data authentication and digital signatures

We’d like to be able to verify the authenticity of a piece of data without a pre-shared secret.

Using asymmetric encryption we can build digital signatures, which:
- Provide strong evidence that data is bound to a specific user
- No shared secret is needed to check (validate) the signature
- Proper signatures cannot be repudiated by the user

[![](../../../images/502bce11d6_vkvsmw6pyu4esRYG-image-1655564209228.png)](../../../images/502bce11d6_vkvsmw6pyu4esRYG-image-1655564209228.png)

The computationally hard problems are:
- Sign a message without the signature key
	- this includes splicing signatures from other messages
- Compute the signature key given only the verification key
- Derive the signature key from signed messages

Again, **RSA** is the most used cipher to build digital signatures.