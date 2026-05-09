---
book_slug: cs-computer-security
book_title: CS Computer Security
chapter_slug: cryptography
chapter_title: Cryptography
created_at: '2022-06-18T14:59:32.000000Z'
id: 169
priority: 7
slug: the-public-key-binding-problem-and-digital-certificates
title: The public key binding problem and digital certificates
type: page
updated_at: '2022-06-18T15:03:24.000000Z'
---

# The public key binding problem and digital certificates

Both in asymmetric encryption and digital signatures, the public key must be
bound to the correct user identity.

If public keys are not authentic:
- A MITM attack is possible on asymmetric encryption
- Anyone can produce a signature on behalf of anyone else

The public key authenticity is guaranteed with... another signature
- We need someone to sign the public-key/identity pair
- We need a format to distribute signed pairs

For this reasons digital certificates were born. They bind a public key to a given identity, which is:
- for humans: an ASCII string
- for machines: either the CNAME or IP address

Digital certificates specify the intended use for the public key contained to avoid ambiguities when a key format is ok for both an encryption and a signature algorithm.

They contain a time interval in which they are valid.

## Certification authorities
The certificate signer is a trusted third party, the CA. The CA public key is authenticated... with another certificate.

[![](../../../images/433e64ef8f_E5WwuYHHnF7mXQRx-image-1655564552258.png)](../../../images/433e64ef8f_E5WwuYHHnF7mXQRx-image-1655564552258.png)

[![](../../../images/eca2128c7a_YUBiSUQBgjiohWBL-image-1655564576002.png)](../../../images/eca2128c7a_YUBiSUQBgjiohWBL-image-1655564576002.png)