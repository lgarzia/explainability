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
PDP conveys the marginal effect of a feature on the prediction throughout all possible values for that feature

- visually demonstrate the impact of a feature and the nature of the relationship with the target
- can extend to two features - to illustrate interaction
- one variation of the PDP - centers marginal effect'
- one variation - show distribution of the feature

Disadvantage of PDP
only display up to two features at a time and assumed independence of features

Accumulated Local Effect (ALE) - use to avoid issues of independence
Results based on aggregation over averages

ICE - look at each individual observations rather than an average

Individul Conditional Expectation (ICE)
What if my PDP plots obscure the variance in my feature-target relationship?

Disadvantage of ICE - assumes independence of features, can't interact with two continuous or high-cardinality features.
hard to ascertain the average relationship betweeo a feature and a target

Global Model-Agnostic Interpretation Methods

permutation feature importance - better alternative to leveraging intrinsic model parameters
learned partial dependence plots
individual conditional expectation plots
**All above sensitive to collinear features**

1. Shapley Additive exPlanations (SHAP) <-- derived from coalitional game theory
2. Accumulated Local Effects (ALE) plot <-- conditional marginal distribution
   Both provide better alternatives to Partial Dependence Plots (PDPs)
3. Global surrogates: white-box models that approximate back-box models

Approach

1. Prepare all the features - no nulls and are all numerical
2. Determine features ability to predict target variable
3. Ensure not overfitting
4. Use SHAP to understand how conclusion reached
5. Perform some statistical test to examine bivariate associations further and rule out any spurious correlations and systematic bias
6. Explore feature effects on models more with ALE plots
7. Gain further understanding of the underlying rules of the model with global surrogates

XGBoost has three different algorithms to compute feature importance

1. How often feature appears in the tree (weight)
2. Average reduction in error due to a feature (gain)
3. number of observations affected by a split involving a feature(cover)
