---
book_slug: ml-machine-learning-Zyp
book_title: ML Machine Learning
created_at: '2023-06-05T16:09:34.000000Z'
id: 193
priority: 4
slug: learning-theory
title: learning theory
type: page
updated_at: '2023-06-17T10:52:57.000000Z'
---

# learning theory

## Questions
### Explain what is the VC dimension of a hypothesis space and what it is used for. (6)
As needed background we need to define:
- A dichotomy of a set $S$ is a partition of $S$ into two disjoint subsets
- A set of instances $S$ is shattered by the hypothesis space $H$ is and only if for every dichotomy of $S$ there exists some hypothesis $h \in H$ consistent with the dichotomy

The Vapnik-Chervonenkis dimension, $VC(H)$, of hypothesis space $H$
defined over instance space $X$ is the size of the largest finite subset of $X$ shattered by $H$. If arbitrarily large finite sets of $X$ can be shattered by $H$, then $VC(H) ≡ \infty$.

The $VC(H)$ dimension is use to construct a probably approximately correct bound for the true error given the train error of an hypothesis $h \in H$ when $H$ is continuos. In particular the bound is:
$$
L_{true}(h) \le L_{train}(h) + \sqrt{\frac{VC(H)(\ln \frac{2N}{VC(H)} +1)+ \ln \frac{4}{\delta}}{N}}
$$
Where this bound means that with probability $1-\delta$ the gap between the true error $L_{true}$ and the train error $L_{train}$ of $h \in H$ is smaller or equal than some value which depends on:
- $VC(H)$ the VC dimension of the hypothesis space
- N the number of training samples
- $\delta$ how much we want to be sure about the bound

The lower bound on the number of samples $N$ to guarantee error of at most $\epsilon$ with probability $(1-\delta)$ is:
$$
N \ge \frac{1}{\epsilon} (4 \log_2 (\frac{2}{\delta}) + 8 VC(H) \log_2 (\frac{13}{\delta}))
$$

Some other important properties of VC dimension are:
- The VC dimension of a finite hypothesis space is bounded: $VC(H) \le \log_2(|H|)$
- A concept class $C$ with $VC(C) = \infty$ is not PAC-learnable.