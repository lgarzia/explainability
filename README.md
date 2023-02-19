# explainability

Interpret models using model-agnostic and deep learning methods

- Feature Importance and Impact
- Global Model-Agnostic Interpretation
- Local Model-Agnostic Interpretation Methods
- Anchor and Counterfactual Explanations
- Visualizing Convolutional Neural Networks
- Interpretation Methods for Multivariate Forecasting and Sensitivity Analysis

**What matters most to the model and how does it matter?**

_Permutation Feature Importance_ --> rank the features intuitively and dependably
_Partial Dependence Plots_ --> Convey marginal impact of a single feature on prediction
_Individul Conditional Expectation (ICE)_ plots to explain changes with a prediction when a feature changes

feature importance - more reliable - permutation-based method called PFI
examine marginal impact to the outcome of the most important features with PDPs - tell which features values correlate the most with predictions
ICE Plot -> more granular visualization of how individual features impact the model predictions

Objective --> leverage the models capacity to unearth latent relationships

NIR -> No Information Rate -> Just guess most common category/average

MCC - Mathew Correlation Coefficient -> -1 if everyone of our predictions were wrong to 1; 0 is random

knowledge discovery tools

Tree Based Models - feature importance has already been calculated using a weighted sum of decreases in node impurity
100% impure balanced across classes, 0% belongs to single class

Best interpret features as relative measure, compare one feature with others but not across different models

Since impurity-based - disadvantage because impurity makes them biased towards higher-cardinality features

There's no consensus on how to extract feature importance from the intrinsic parameters of a neural network

How to calculate feature importance for any model? PFI - Permutation Feature Importance

PFI -> measures the increase in prediction error once the values of each feature have been shuffled.
The theory for PFI is based on the logic that if the feature has a relationship with target variable
shuffling will disrupt it and increate the error. Then if you rank features by those whose shuffling increases the error
the most, you'll appreciate which ones are most important to the model

Can be used with unseen data; model agnostic; tell features most important once you introduce unseen data

Scikit learn - permutation_importance functions - inpute - fitted_model, features, labels...

Main disadvantages of PFI --> won't pick up on the impact of features correlated with each other; multicollinearity will trump feature importances.

Interpreting PDPs... Partial Dependence Plots:
