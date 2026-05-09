---
book_slug: cs-computer-security
book_title: CS Computer Security
chapter_slug: introduction-authentication-and-access-control
chapter_title: Introduction, authentication and access control
created_at: '2022-06-17T11:18:18.000000Z'
id: 151
priority: 4
slug: exercises-on-authentication-and-access-control
title: Exercises on authentication and access control
type: page
updated_at: '2022-06-17T13:17:12.000000Z'
---

# Exercises on authentication and access control

## 2021-2022 Demo exam exercise 1 (4 points)
In a company, each employee works in an open space. We need to design proper policies to minimize the
risk that passwords get compromised. Such policies will be enforced whenever a user chooses a new
password. Also, assume that passwords are only used to access a cloud-based email client over TLS.

1. [1 point] What are the main characteristics of a password on which we can act when writing a policy?
2. [2 points] What is the most likely attack scenario against passwords considering the above description of the conditions of each employee? Why?
3. [1 point] Given the answer provided in point 2, what is the most important characteristic that you need to enforce in the password policy (in order to avoid the attack scenario)?

## Question 1
We are designing the password policy for an online banking
website. Which of the following rule sets is more adequate in your
opinion, and why?
- Passwords must be at least 12 characters long, with at least one
lowercase, one uppercase, one number and one special
character. Passwords must be changed at least every 30 days and
cannot match previous ones. Accounts are locked after 3 wrong
attempts.
- Passwords must be at least 8 characters long, and not belong to
a dictionary of common passwords. They must be changed at
least every 30 days and cannot match previous ones. Accounts
are locked after 5 wrong attempts.

1. We are designing the password policy for an online banking website. Which of the
following rule sets is more adequate in your opinion, and why?
<details>
  <summary>Solution</summary>
  
The first seems stronger, because it enforces long (against bruteforcing), non-reused
(against stealing) passwords and mitigates bruteforcing. However, it will lead
users to write down passwords.
  
The second has an additional measure (non dictionary words) that is missing in the
previous scheme. Given that guessing is more likely than cracking, and that
writing down passwords is a pitfall, this scheme is definitely better with respect to
the previous one.
</details>

## Question 2
Consider biometric authentication.

1. Describe (a) how the authentication phase works and (b)
explain the phases that are needed to deploy such an
authentication system in a company.
<details>
  <summary>Solution</summary>
  
It is based on recording features extracted from a biometric characteristic
of each user. At each authentication, the measured features are
compared with the recorded ones. Each user is thus required to measure
the characteristic when a system is deployed.
</details>

2. The company is evaluating whether to use a fingerprint
scanner or iris recognition as a characteristic for
authentication purposes. What are the considerations that
you would make?
<details>
  <summary>Solution</summary>
  
Fingerprint scanning and iris recognition are both very precise
authentication methods. Fingerprint scanning is slightly easier to fool with
counterfeits. Iris recognition is a more invasive procedure which may be
less tolerable by users. Additionally, iris recognition is far more costly.
</details>

3. The geometry of the palm of the hand has been proposed as
a biometric characteristic for authentication purposes.
Discuss what issues do you see in this idea.
<details>
  <summary>Solution</summary>
  
There are two main issues: false positive (another user with the hand geometry
very similar to the legitimate user may be able to authenticate), which may happen
if the features are too generic; false negative (the legitimate user may be unable to
authenticate), which may happen if the features are too specific
</details>

## Question 3
Discuss the following statements related to authentication: are
they true or false? And why?

1. Password authentication is widely used because it is weaker but
cheaper
<details>
  <summary>Solution</summary>
  
True, because it does not require special equipment, and it is even
easier to deploy in many environments.
</details>

2. Biometric systems are not deterministic, and this is an issue
<details>
  <summary>Solution</summary>
  
True, because the biometric features that they measure (e.g.,
fingerprints, hand geometry) may change over time, and
measurement errors can occur. Thus, they need to be carefully
evaluated for false acceptance and false rejection ratios.
</details>

3. Biometric systems identify a person on the basis of their
physical characteristics, making it impossible for an attacker to
impersonate someone else
<details>
  <summary>Solution</summary>
  
False. Attacks have been developed against biometric systems.
For example it is rather easy to duplicate someone's
fingerprints.
</details>

4. Introducing a biometric system to protect a high-value target
will decrease risks for the target, often at the expense of
increasing personal risk for the users
<details>
  <summary>Solution</summary>
  
True, if the system makes attacking a user the most viable way to
access the high value target.
</details>

## Question 4
Discuss the following statements saying if they are true or
false, and give a reason.

1. OTP (one-time passwords) are relatively easy, drop-in
replacements for static passwords
<details>
  <summary>Solution</summary>
  
True, because it requires little equipment and set up effort for
interfacing. The only significant cost is associated to
password/secret code generation (i.e. the cost of the token,
or of sending SMS with codes, etc.)
</details>

2. The only source of error of biometric authentication is the
evolution of the human body characteristics
<details>
  <summary>Solution</summary>
  
False, because measurement
errors can occur during each authentication phase. Also, the
process is non deterministic intrinsically.
</details>

3. A biometric system is more secure than a
password-based system
<details>
  <summary>Solution</summary>
  
False. In order to evaluate the
level of security we need to know more of the system they are
designed to protect. Their level of security could be
comparable, or either could be a better choice than the other.
</details>

## Question 5
In a company, each employee has a private office, where only
authorized people can enter. The workstation is positioned
such that the computer screen faces the wall. Also assume
that passwords are only used to access cloud-based services
over TLS. We need to design proper policies to minimize the
risk that passwords get compromised. Such policies will be
enforced whenever a user chooses a new password.

1. What are the main characteristics of a password on which we
can act when writing a policy?
<details>
  <summary>Solution</summary>
  
Complexity = length, rich character set
Non guessability = not belonging to dictionaries, not user related
Frequency of change
</details>

2. What is the most likely attack scenario against passwords
considering the above description of the conditions of each
employee? Why?
<details>
  <summary>Solution</summary>
  
Guessing, because the office space is confined and accessible only to
authorized personnel. Cracking is the second most-likely attack. Snooping
is certainly not an option here.
</details>

3. Given the previous answer, what is the most important
characteristic that you need to enforce in the password policy
(in order to avoid the attack scenario)?
<details>
  <summary>Solution</summary>
  
Against guessing, we must enforce that passwords are not related to the user and, in general, not belonging to
dictionaries or common passwords
</details>

## Question 6
In a company, each employee works in an open space. We
need to design proper policies to minimize the risk that
passwords get compromised. Such policies will be enforced
whenever a user chooses a new password. Also, assume that
passwords are only used to access a cloud-based email client
over TLS.

1. What is the most likely attack scenario against passwords considering
the above description of the conditions of each employee? Why?
<details>
  <summary>Solution</summary>
  
Snooping because the configuration of the space
</details>
2. Given the previous answer, what is the most important characteristic
that you need to enforce in the password policy (in order to avoid the
attack scenario)?
<details>
  <summary>Solution</summary>
  
Against snooping frequent change is the most important policy
</details>

## Question 7
What are the differences between MAC and DAC?
Make an example of real-world MAC system and at
least one example of real-world DAC system.

<details>
  <summary>Solution</summary>
  
Key difference: in DAC owner assigns control over resource, in MAC
security admin sets levels.
  
Example of MAC: classification of secret documents in the military.
  
Examples of DAC, you name it, any OS.
</details>

## Question 8
What are the differences between access control lists and
capability lists?

<details>
  <summary>Solution</summary>
  
ACLs are efficient with per-object operations, but cannot be used to assign
multiple owners to the same object (this can be partially addressed with groups).
Capabilities are efficient with per-subject operations, which make them inefficient
when objects change frequently.
</details>