---
book_slug: ml-machine-learning-Zyp
book_title: ML Machine Learning
created_at: '2023-06-05T15:53:12.000000Z'
id: 190
priority: 1
slug: linear-models-for-regression
title: linear models for regression
type: page
updated_at: '2023-06-17T10:49:33.000000Z'
---

# linear models for regression

## Questions
### Describe and compare Ridge regression and LASSO algorithms to solve linear regression problems. (8)
These two regularization techniques differ from ordinary least squares because they introduce a model complexity penalization term in the loss function:
$$
\begin{align*}
    L(w) &= L_D(w) + \lambda L_W(w) \\\\
    L_D &= \text{error on the data} \\\\
    L_W &= \text{model complexity penalization}
\end{align*}
$$

For ridge we take $L_w(w) = \frac{1}{2}w^Tw = \frac{1}{2} \lVert w \rVert \_{2}^2$:
$$
L(w) = \frac{1}{2}\sum_{i=1}^{N}{(t_i - w^T\phi(x_i))^2+\frac{\lambda}{2} \lVert w \rVert _2^2}
$$

Using this loss we are taking into account model complexity penalizing large values of the parameters, it is a parameters shrinkage method. This allows to reduce the variance of the model.

This is used to tame the overfitting of a model. A model tends to overfit using large values of the parameters which allows to capture the noise in the data at the expense of generalization. Ridge regression is therefore a biased model, and increasing $\lambda$ allows to decide how much bias we want to introduce, reducing the variance.

Lasso is another regularization technique which uses the loss:
$$
L(w) = \frac{1}{2}\sum_{i=1}^{N}{(t_i - w^T\phi(x_i))^2+\frac{\lambda}{2}\lVert w \rVert _1}
$$

The difference is that the penalization term uses the $L_1$ norm instead of the $L_2$ norm. This introduces a non-linearity in the $t_i$ and no closed form solution exists. However, the model can still be trained using iterative procedures and one optimal solution exists as the loss in convex.

Lasso differs from ridge as it pushes the values of some parameters to zero, leading to sparse models, which may be a desiderable attribute in some situations (e.g. if we have too many dimensions and we want to perform feature selection).

As before, $\lambda$ is used to tune the bias-variance trade off.

### Describe the Bayesian Linear Regression method and how it compares to Ridge Regression. (3)
### Describe and compare ordinary least squares and Bayesian linear regression. (1)
In the bayesian approach we formulate a model that expresses our knowledge about the problem. The model will have some unknown parameters, we have some assumptions about these parameters that we capture with the formulation of a prior distribution over the parameters.

We then take observed data into account to update our assumption about the parameters, computing the posterior distribution which we will the use, with the model, for our tasks.

When we want perform linear regression with the bayesian approach we consider the parameters as drawn from some distribution.

If we assume a Gaussian likelihood model, the conjugate prior is a Gaussian too:
$$
p(w)= \mathcal{N}(w|w_0, S_0)
$$

Given the data $D$, the posterior is still a Gaussian:
$$
\begin{align*}
    p(w|t, \Phi, \sigma^2) &= \mathcal{N}(w|w_N, S_n) \\\\
    w_N &= S_N (S_0^{-1} w_0 + \frac{\Phi^T t}{\sigma^2}) \\\\
    S_N^{-1} &= S_0^{-1} + \frac{\Phi^T \Phi}{\sigma^2}
\end{align*}
$$

In Gaussian distributions the mode and the mean coincide (because of the symmetry), so the maximum a posteriori (MAP) is the mean of the Gaussian $w_N$.

If our prior has infinite variance (completely uninformative prior) then $w_N$ reduces to the maximum likelihood estimator (so MAP = ML).

We can define the posterior predictive distribution marginalized the distribution of the new target value given the model over the posterior of the parameters given the data:
$$
\begin{align*}
    p(t|x,D,\sigma^2) &= \int \mathcal{N}(t|w^T \phi(x), \sigma^2) \mathcal{N}(w|w_N,S_n) dw\\\\
    &= \mathcal{N}(t|w_N^T \phi(x), \sigma_N^2(x)) \\\\
    \text{where} \\\\
    \sigma_N^2 &= \sigma^2 + \phi(x)^T S_N \phi(x) \\\\
    \sigma^2 &= \text{noise in target values} \\\\
    \phi(x)^T S_N \phi(x) &= \text{uncertainty in parameters}
\end{align*}
$$

If we assume as prior $w_0 = 0$ and $S_0 = \tau^2 I$ then  the prior distribution is $\mathcal{N}(w|0, \tau^2 I)$ and the MAP estimator $w_N$ is equal to a ridge estimate with $\lambda = \frac{\sigma^2}{\tau^2}$.

Using the bayesian approach has the advantage of computing a distribution of the parameters instead of a single value. This information may be useful in varius situations, for example to estimating the confidence of the model. Moreover, if prior knowledge is available it is easier to implement modeling the prior.

The drawbacks of this approach is that choosing a right model and a right prior for the parameters is difficult, and most of the times hyperparameters are used for the prior.

Futhermore, computing the posterior distribution becomes very expensive when we move away from conjugate priors, which are usually suitable only for simpler problems. Most of the time numerical algorithms like Monte Carlo Markow chain with Gibbs sampling are applied in these cases (other approaches exists).