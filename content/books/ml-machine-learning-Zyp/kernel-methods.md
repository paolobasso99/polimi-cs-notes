---
book_slug: ml-machine-learning-Zyp
book_title: ML Machine Learning
created_at: '2023-06-05T16:10:08.000000Z'
id: 194
priority: 5
slug: kernel-methods
title: kernel methods
type: page
updated_at: '2023-06-06T14:06:22.000000Z'
---

# kernel methods

- [CS480/680 Lecture 11: Kernel Methods](https://www.youtube.com/watch?v=nzSBvINmg28)

## Questions from past exams
### Give the definition of valid kernel and describe how valid kernels can be built. Provide an example of a methods that uses kernels and specify the advantages of using them in this specific method. (3)
A valid kernel $k(x, x')$ is any function that can be expressed as $k(x,x') = \phi^T(x)\phi(x')$. This also means that a necessary and sufficient condition for a kernel to be valid is that the Gram matrix $K$, whose elements are given by $k(x_n,x_m)$, is positive semi-definite for all possible choices of set $\{x_n\}$.

A valid kernel can be built, mainly, in three different ways:
1. We choose a feature space mapping $\phi(x)$ and we define the kernel as $k(x,x') = \phi(x)^T \phi(x')$.
2. We choose directly the kernel function $k(x,x')$ and we check that it can be written in the form $\phi^T(x) \phi(x)$
3. We know some valid kernels and we combine or apply functions to them that we know will keep the validity of the kernel. For example if we know that $k_1(x,x')$ is a valid kernel then we also know that $ck_1(x,x')$ is valid as well.

One example of method which uses kernel functions is support vector machines for binary classification. The advantage of using the kernel function is that ...

### Explain what the Kernel Trick is, what it is used for, and in which ML methods it can be used. (1)
### Describe the Gaussian Processes model for regression problems. (1)

### Describe Support Vector Machines (SVMs) for supervised classification problems. In particular explain how do they work, their strengths and weaknesses. Which algorithm can we use to train an SVM? Provide an upper bound to the generalization error of an SVM. (8)