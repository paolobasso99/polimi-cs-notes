---
book_slug: ml-machine-learning-Zyp
book_title: ML Machine Learning
created_at: '2023-06-05T16:08:48.000000Z'
id: 192
priority: 3
slug: bias-variance-model-selection-and-model-ensembles
title: bias-variance, model selection and model ensembles
type: page
updated_at: '2023-06-06T14:06:22.000000Z'
---

# bias-variance, model selection and model ensembles

## Questions
### Describe the PCA technique and what it is used for. (3)
Principal Component Analysis (PCA) is a linear dimensionality reduction technique. The idea is to project the data onto the input subspace which accounts for the most variance.

The steps of the PCA algorithm are:
1. Mean center the data: $\bar{x} = \frac{1}{N} \sum_{n=1}^N x_n$
2. Compute the covariance matrix $\mathcal{S} = \frac{1}{N-1}\sum_{n=1}^N (x_n - \bar{x})(x_n - \bar{x})^T$
3. Calculate the eigenvectors and eigenvalues of the covariance matrix
4. The eigenvectors $e_i$ with the largest eigenvalues $\lambda_i$ will be the principal components, we can decide how many principal components to use. The variance captured by th $i$-th principal component is $\lambda_i / \sum_j \lambda_j$. The comulative variance with $k$ components on a $d$-dimensional dataset is:
$$
\frac{\sum_{j=1}^k \lambda_j}{\sum_{j=1}^d \lambda_j}
$$

If we would keep all the principal components we would have the same dimensions from which we started but in a new orthogonal basis for the features space for which the axes are aligned with the maximum variance of the original data.

If we keep $k$ of the first principal components ($E_k = (e_1,...,e_k)$) we have reduction in the dimensionality of the representation: $X' = E_k X$.

We call:
- input dataset $X$
- loadings $E_k = (e_1,...,e_k)$ the matrix of the principal components
- scores $X'=E_k X$ the matrix of the transformed input dataset

We lose some information with the reduction and, if we transform the reduced dimensionality projection into the original space the reconstruction we obtain will contain some error. The inverse transformation is: $X = X' E_k^T$.

PCA can be useful as a way to visualize high dimensional data.
Another use case is as a preprocessing step:
- Reduce computational complexity
- Reduced dimensions means a smaller hypothesis space
- Can be seen as a noise reduction

Some important considerations:
- PCA fails when data consists of multiple clusters
- Direction of largest variance may not be the most informative
- Computational problems if there are many dimensions
- PCA computes only linear combinations of features which is not ideal when the data lies on a nonlinear manifold

### Provide an overview of the feature selection methods that you know and explain their pros and cons. (1)
**Best subset selection**: it is a way of trying all the possible subsets of features and selecting the best one. In particular, we start with the null model $\mathcal{M}_0$ which contains no input features (it predicts the mean over the observations).

Then, for $k=1,...,M$ we fit all $M \choose k$ possible models with exactly $k$ features. We can then pick the best model with exactly $k$ features $\mathcal{M}_k$ with the smallest RSS (or loss function).

Finally, we select the best model among $\mathcal{M}_0, ..., \mathcal{M}_M$ using some criterion (cross-validation, AIC, BIC, ...).

The problem of this method is that when $M$ is large (which is usually the case) the computational cost is too hight, and it is also prone to overfitting.

**Filter method**: with this method we rank the features according to some scoring function (e.g. Pearson correlation coefficient between the feature's values and the targets); then we select the features with the best score. We can decide how many features to keep according to some criterion (cross-validation, AIC, BIC, ...).

This method is very fast and efficient (if the scoring function is) but it is a greedy selection of the best features. Moreover, the scoring function usually considers one feature at the time which may not be ideal in some problems where combinations of features considered together are valuable. Finally, depending on the scoring function, we may have a different ranking of the features.

**Embedded methods**: some models have feature selections built-in. This means that the learning algorithm will exploit his own variable selection technique. 

An example of such methods is the LASSO linear regression. Using the $L_1$ norm of the parameters in the loss function it pushes some parameters to zero, excluding them and therefore performing a selection of the features.

The advantage of this method is that no additional feature selection step is needed before running the model. However, the feature selection is usually controlled by some hyperparameter which must be carefully tuned.

**Wrapper methods**: with this methods we evaluate only some subset of features using some search heuristic with the objective of finding the best subset without trying all the possible combinations. The two most common approaches are forward and backward features selection methods. In forward feature selection we start from the empty model and add the most useful feature one-at-a-time. On the other hand, with backward feature selection we start with all the features and delete the least useful feature one-at-a-time.

The most or least useful feature is usually selected evaluating the loss function on a validation set, but other approaches exists.

Wrapper methods are usually a good compromise between an exhaustive search and other, faster approaches, like filter methods.

### Explain the cross-validation procedure and for what it can be used. (1)
The training error is not useful for selecting the hyperparameters of the model (including the features to use) because the more complex the model the smaller the training error will be. However, the model with the smallest training error may (and usually is not) the best one due to overfitting on the training set.

Therefore, we need to test different configurations using a different dataset, not seen by training and testing (final evaluation). If we use a fixed validation set the problem is that we may overfit it, and select hyperparameters which are good for the specific set but not for other datasets (including the test one).

The most common way to approach this problem is using a cross-validation procedure. The extreme case of cross validation is Leave-One-Out in which we train the model in the whole dataset excluding one sample, estimating the error in the one sample validation set and then repeating the procedure for all the samples, averaging the estimated error at the end. The advantage is that this approach is almost unbiased (slightly pessimistic). The main drawback is the high computational cost required to train the model as many times as the number of samples available.

The most common way to do cross validation in practice is to use $k$-folds. We randomly divide the dataset in $k$ folds, we train using $k-1$ folds and then we evaluate on the remaining one. We repeat for all the folds and we average the results. With respect to LOO this is much faster as we train the model less times but the procedure is more pessimistically biased. Moreover, we need to select an appropriate value for $k$, usually a default values is $k=10$.

### Describe and compare the Bagging and Boosting meta-algorithms. (1)
Bagging and boosting are two meta-algorithms which follow the basic ideas of creating an ensemble (a combination) of several models instead of learning one single model.

Bagging has the goal of decreasing the variance without increasing the bias of unstable learners which vary significantly with small changes in the dataset. It works by generating $B$ bootstrap samples of the training data using random sampling with replacement. Then a classifier or a regressor is trained on each bootstrap sample. For prediction we use majority voting for classification and average in regression. Bagging improve the variance (due to averaging different dataset) of unstable learners, but it does not help much with high bias.
Bagging can also be easily parallelized because we can train the different models in parallel.

Boosting has the goal of achieving small bias on simple (weak) learners. The idea is to sequentially train weak learners, which are learners with a performance only slightly better than chance. The sequential learning works in the following way:
- Give an equal weight to all samples in the train set
- Train a weak learner on the weighted training set
- Compute the error of the trained model on the weighted training set
- Increase the weights of samples missclassfied by the model
- Repeat until some criteria is met

The ensemble of models learned can be applied on new samples by computing the weighted prediction of each model (more accurate models weight more).

Finally, comparing bagging and boosting:
- Bagging reduces variance using unstable learners
- Boosting reduces bias using weak learners
- Bagging does not work well with stable models, boosting can still be applied
- Boosting might hurt performance on noisy datasets. Bagging doesn’t
have this problem
- In practice bagging almost always helps but the improvement may be small
- On average, boosting helps more than bagging, but it is also more common for boosting to hurt performance
- Bagging is easier to parallelize while boosting is usually run in sequence

### Illustrate the AdaBoost algorithm, explain its purpose and in which case it is useful. (1)
AdaBoost, short for Adaptive Boosting, is a classification meta-algorithm based on boosting. It can be used in conjunction with many other types of learning algorithms to improve performance. The output of the other learning algorithms ('weak learners') is combined into a weighted sum that represents the final output of the boosted classifier.

AdaBoost is adaptive in the sense that subsequent weak learners are tweaked in favor of those instances misclassified by previous classifiers. In some problems it can be less susceptible to the overfitting problem than other learning algorithms. The individual learners can be weak, but as long as the performance of each one is slightly better than random guessing, the final model can be proven to converge to a strong learner. 

AdaBoost refers to a particular method of training a boosted classifier. A weak learner (e.g.  a decision stump) is made on top of the training data based on the weighted samples. Here, the weights of each sample indicate how important it is to be correctly classified. Initially, for the first learner, we give all the samples equal weights ($\frac{1}{N}$).

A weight is assigned to each classifier based on the accuracy of the classifier.

The samples weights are updated so that more weight is assigned to the incorrectly classified samples, this makes it more likely that they're classified correctly in by the next weak learner.

We repeat this until all data is correctly classified or the maximum number of iterations is reached (or other criterions).

### Describe the Bias-Variance tradeoff for regression problems. Explain how is it possible to evaluate the bias-variance tradeoff by looking at the train error and at the test error. (1)