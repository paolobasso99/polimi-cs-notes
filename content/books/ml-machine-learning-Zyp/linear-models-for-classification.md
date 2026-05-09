---
book_slug: ml-machine-learning-Zyp
book_title: ML Machine Learning
created_at: '2023-06-05T15:56:05.000000Z'
id: 191
priority: 2
slug: linear-models-for-classification
title: linear models for classification
type: page
updated_at: '2023-06-06T14:06:22.000000Z'
---

# linear models for classification

## Questions
### Describe the Perceptron model and how it is trained. (1)

The Perceptron algorithm is an example of online linear discriminant model. It corresponds to a two classes model:
$$
y(x) = f(w^T \phi(x)) \text{, where } f(a) =
\begin{cases}
    +1, a \ge 0 \\
    -1, a < 0
\end{cases}
$$

The Perceptron criterion assigns zero error to correctly classified points and $w^T \phi(x_n) t_n$ to misclassified samples, this error is proportional to the distance of the sample to the decision boundary. Therefore, the loss to minimize is:
$$
L_P(w) = -\sum_{n \in \mathcal{M}}{w^T \phi(x_n) t_n}
$$
Where $\mathcal{M}$ is the set of misclassified samples.

The minimization is performed using stochastic gradient descent:
$$
w^{(k+1)} = w^{(k)} - \alpha \nabla L_p(w) = w^{(k)} - \alpha \phi(x_n)t_n
$$
Since the algorithm does not change if $w$ is multiplied by a positive constant, the learning rate $\alpha$ can be set to $1$.

The Perceptron algorithm is applied looping multiple times over the samples, updating $w$ with the stochastic gradient descent rule until all the samples are correctly classified, which is checked with a full pass over the samples (epoch).

The Perceptron convergence theorem states that:
> if the training set is linearly separable in the feature space $\Phi$, then the Perceptron algorithm is guaranteed to find a decision boundary which perfectly classifies all samples in a finite number of steps.

However, the number of steps may be substantial and we are not able to distinguish nonseparable problem to slowly converging ones.

Multiple solutions exists and the one found depends on the initialization of $w$ and on the order that is used to consider the samples.

### Describe the logistic regression model and how it is trained. (2)
Logistic regression is a probabilistic discriminative model. For the two classes case, logistic regression models the the posterior probability of the two classes as:
$$
\begin{align*}
    p(C_1|\phi) &= \sigma(w^T \phi) = \frac{1}{1 + exp(-w^T \phi)} \\
    p(C_2|\phi) &= 1 - p(C_1|\phi)
\end{align*}
$$

For a single sample $\{x, t\}$ the probability of getting the right label is:
$$p(t|x, w) = y^t (1-y)^{1-t}$$
where $y = \sigma(w^T \phi)$. 

Given a dataset $D=\{x_n, t_n\}$, $n=1,...,N$; $t_n \in \{0,1\}$, we maximize the probability of getting the right label for all the samples (likelihood):
$$
p(t|X,w) = \prod_{n=1}^N{y_n^{t_n} (1-y_n)^{1-t_n}}
$$
where $y_n = \sigma(w^T \phi_n)$.

To do the maximization we first define a loss called **cross-entropy loss** (to be minimized). The cross-entropy loss is the negative log of $p(t|X,w)$:
$$
L(w) = - \ln p(t|X,w) = -\sum_{n=1}^{N}(t_n \ln y_n + (1-t_n) \ln (1-y_n)) = \sum_{n=1}^N L_n
$$

To minimize the loss function we take the gradient:
$$
\begin{align*}
    \nabla L(w) &= \frac{\partial L(w)}{\partial w} = \sum_{n=1}^N \frac{\partial L_n}{\partial y_n} \frac{\partial y_n}{\partial w} \\
    &= \sum_{n=1}^N (\frac{t_n}{y_n} + \frac{1-t_n}{1-y_n}) y_n (1- y_n) \phi_n \\
    &= \sum_{n=1}^N (y_n - t_n) \phi_n
\end{align*}
$$

The loss function is convex but there is no closed form solution due to the non linearity introduced by the sigmoid. Therefore, we use gradient based approaches to minimize the loss function.

If we are dealing with multiple classes we represent the posterior probabilities of each class as:
$$
p(C_k|\phi) = y_k(\phi) = \frac{exp(w_k^T \phi)}{\sum_j exp(w_j^T \phi)}
$$

As before we use the maximum log likelihood to determine the parameters of this discriminative model. 

The training, as before, is done using a gradient approach to minimize the negative log likelihood (which is the cross-entropy loss).

### Describe the logistic regression algorithm and compare it with the Perceptron algorithm. (1)
The main difference between logistic regression and the Perceptron is that logistic regression is a probabilistic discriminative model while the Perceptron is a discriminant function:
- Logistic regression models $p(C_k|\phi)$ directly, with a parametric approach
- The Perceptron builds a function that directly maps a given sample to a specific class, without modeling the probabilities of all the classes for the sample.

If we swap the logistic function with a step function in the logistic regression algorithm then both algorithm use the same update rule when using stochastic gradient descent:
$$
w^{(k+1)} = w^{(k)} - \alpha(y(x_n, w) -t_n)\phi_n
$$

### Describe the supervised learning technique denominated K–Nearest Neighbor for classification problems. (1)
K-Nearest Neighbor is a non-parametric discriminant function model. It follows the basic idea of looking at the nearby points to predict  the target of a new point.

Given a dataset $D=\{x_n,t_n\}_{i=1}^N$ and a new data point $x$_q, we predict the target as:

$$
i_q \in arg \min_{n \in \{1, ..., N\}}\|x_q - x_n \|_2
$$

Since it is non parametric it does not need to be explicitly trained (there are no parameters to train). However, the dataset needs to be available for querying when we want to predict a target.

There are some important design choices which need to be made for this algorithm:
- Which distance measure to use?
- How many neighbors to consider? The highest the $K$ we chose the highest the regularization (more bias, less variance) we introduce in the model. The appropriate value is chosen by cross-validation.
- For $K>1$ how are the target combined? Usually we use majority voting with tie braking for classification and average target for regression but other approaches exists.

## Other topics not covered by Questions
### Multiple classes classification
### Least squares for classification