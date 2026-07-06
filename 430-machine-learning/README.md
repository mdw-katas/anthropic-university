# CS 430 — Machine Learning

**Prerequisites:** MATH 240, MATH 360
**Language:** Python (NumPy first, then scikit-learn)

## Course Description

Learning from data: the core algorithms of classical machine learning, the
mathematics that makes them work, and the discipline of evaluating them
honestly. Models are implemented from scratch in NumPy before any library
is allowed — the point is to own the math from MATH 240 and MATH 360, not
to drive a black box.

## Learning Objectives

- Formulate problems as supervised or unsupervised learning with an
  explicit loss function.
- Implement linear and logistic regression with gradient descent from
  scratch, and explain every term in the update rule.
- Explain the bias-variance tradeoff and control overfitting with
  regularization and validation.
- Train, tune, and honestly evaluate models: train/validation/test splits,
  cross-validation, metrics beyond accuracy, leakage.
- Use the classical toolbox: decision trees and ensembles, k-NN, naive
  Bayes, SVMs (survey), k-means, PCA.

## Topic Outline

1. The learning problem: hypotheses, loss, generalization; ML as function
   approximation.
2. Linear regression: least squares (the MATH 240 connection), gradient
   descent.
3. Logistic regression and classification; maximum likelihood (the
   MATH 360 connection).
4. Overfitting, bias-variance, regularization (L1/L2), validation and
   cross-validation.
5. Feature engineering, preprocessing, and data leakage.
6. Evaluation: precision/recall, ROC/AUC, calibration, baselines.
7. Decision trees; ensembles: bagging, random forests, boosting.
8. k-nearest neighbors and naive Bayes; the curse of dimensionality.
9. Support vector machines and kernels (survey).
10. Unsupervised learning: k-means, hierarchical clustering, PCA.
11. Neural networks introduced: the perceptron, multilayer networks,
    backpropagation derived by hand — the bridge to CS 440.
12. ML in production (survey): pipelines, drift, and honest reporting.
