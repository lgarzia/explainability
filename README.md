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

Learning about Shapley Values

coalitional game theory
cooperative game theory

different combination of players are _coalition_
difference in scares are _marginal contributions_
_Shapley value_ is average of these contribution over may simulations
_payoff_ contribution of a feature (is reduction in predictive error, ...)
_average marginal contribution by a feature across all possible subset_
brute force - infeasible, leverage sampling of subset (e.g. Monte Carlo Sampling)
Shapley algorithm calculates the features expected value over the entire dataset - serves as baseline

propertiers
Dummy --> feature i, never contributes, Shapley=0
Substitutability --> if i & j contribute equally; Shapleyi = Shapleyj
Additivity --> contribution of i in submodel add up
Efficiency --> All shapley values must add up as the difference between predictions and expected values

No pure SHAP implementation...

SHapley Additive exPlanations -> collection of methods that approximate Shapley

pg 202 - SHAP Explainers

TreeExplainer --> TreeShap --> ... XGBoost, LightGBM, ...
Deep Explainer --> DeepLife --> keras, pytorch
GradientExplainer --> Integrated Gradient --> keras, pytorch
LinearExplainer --> Shapely Regression Value --> sklearn.linear_model
KernelExplainer --> LIME --> Model Agnostic
SamplingExplainer --> Shapely Sampling Values --> Model-Agnostic
PermutationExplainer --> Model-Agnostic
PartitionExplainer --> Model-Agnostic
AdditiveExplainer --> Model-Agnostic

TreeExplainer -> uses conditional expectation instead of marginal -> can assign non-zero values for uninfluential features - ramification if feature collinear
DeepLift -> attributed difference in output when provided a reference neutral input or baseline (feature wise mean)
GradientExplainer -> leverages baseline, reformulate Gradients, which reformulates the integral as an expectations
KernalExplainer -> most popular -> LIME (Local Model-Agnostic Interpretation Methods) - has challenges with dummy features and collinear features
PermutationExplainer -> closest to brute force
ParitionExplainer -> computes SHAP values on a treen; recommended many features belong to a group or category or have highly correlated features
AdditiveExplainer -> fail if model is not Generalized Additive Model

Initializing explainer -> requires fitted model, sometimes data
Computing SHAP values (idea Test and Train to ensure consistency)

Mannings - https://github.com/munnm/XAI-for-practitioners
Finished Chapter 3

- Shapely values, permutation feature importance, tree interpreters, various versions of partial dependence plot

Permutation Feature Imporance - Results can be misleading when features are highly correlated.
perturbation-based feature attribution technique commonly used for tabular datasets
determine impact each feature has on predictions bhy seeing how the models predictions vary
permutation feature importance of a model is the decrease in a model score when a single feature value is randomly shuffled
permutation feature importance is a post hoc, global, model-agnostic explainability technique
scores are relative - only interpreted in relation to one another

Permutation Feature Imporance in Scikit-Learn

Shapely Values
Attributions sum to the total predictive value
Pass all examples X_Test to explainer

Baseline prediction is just the expected value of the model output
that is - the average of the model predictions on all values in test set. SHAP values of all the input
features will sum up to the differences between the baseline model output and the model prediction for that example.
summing the baseline value with the Shapley values gives the model prediction
Shapley values simply indicate relative influence by a feature
Usefu technique is to normalize the Shapley values for all features in a predictions to the range -1 to 1

Interpreting Feature Attributions fromo Shapley Values
3 pieces of information.

1.  numerical contribution to the predictions score
2.  whether feature contributed in the model moving from the baseline prediction score toward the predicted score or away from
3.  relative magnitude of the feature contribution compared to other features

does not necessarily mean a positive attribution contributed to the models prediction in a postive way, may be
that this feature had less impact than other features.

**Managed Shapley Value**
Google Cloud Platform - Explainable AI
CLI, Rest, Vertex AI Python SDK, Vertex AI Notebook ans Workbench

Tree Based Models
Decision trees easliy allow for counterfactual analysis in that a user is able to ask (and answer) what if questions.

Don't do well predicting values that lie outside the range of the training data
models are inherently noncontinuous functions
random forest - since the prediction is the average of the predictions of all the trees in the forest,
the explanation of the prediction is simply the average of the bias terms plus the average of the contribution of each feature
within each tree

library - treeinterpreter
SHAPs TreeExplainer - optimized

Partial Dependence Plots and Related Plots
Partial Dependence Plots (PDPs), Individual Conditional Expectations (ICE) plots and Accumulated Local Effects (ALE) plots are
closely related family of explainability tools that allow for visualizing the causal interaction between features and model predictions.

Applied after model been fully trained and used to visualize the interaction between one or two features of entire training dataset of the model and output label

partial dependence plots are global, individual conditional expectations and accumulated local effects plots are local

PDPs - useful technique to visualize the marginal effect a specific feature has on a model's prediction
When feature is not correlated to other features, it is possibe to infer a causal relationship between the feature and the model predction
Measure how the expected value of the model output changes with respect to the feature value
Plot describes precisely how the predicted output varibale changes on average with respect to given feature
PDP marginal effect a feature has on the predicted probabilities

avoid condition of independence --- use conditional distribution instead of marginal distribution (ALE)

ICE Plots extend partial dependence plots by visualizing the dependence on a feature for each instance in the dataset

partial dependence plot is an average of the model prediction values obtained in the ICE plot

Accumulated Local Effects (ALE)
takes into account conditional dependence of correlated features and by computing the marginal effect by taking differences instead of averages
Unlikely outcomes weighted less.... 5 ft height, 300 lbs

Mitigate this issue by taking the differences of model predictions in place of averags
5.1, 4.9 compute difference

--- Started chapter 5: Explainability for Text (Notes forthcoming)
...
Understanding Interactions - interaction of feature in black box challenging
80/20 rule - most salient interactions among top tiers
top features across different models
correlation analysis - spearman good for linear relationships
point-biserial correlation <-- >=like Spearman but between a dichotomous and a continuous variable

**SHAP dependence plots**
SHAP dependence plot is between the SHAP value for a feature on the y-axis and the feature value on the x-axis.
Model will pick up on obscure interaction - data quality issues

**SHAP force plots**
Used to explain a single prediction. Force plots depict a continuum, where blue features represent forces pushing predictions
in a negative direction and red ones represent forces pushing predictions in a positive direction.
Stack the local interpretations vertically side by side, create global interpretation.

**Accumulated Local Effects (ALE) plots**
take approach by factoring data distributions when calculating the effects of a feature
split feature inot equally sized intervals (typically, quantile)
Compute how much the predictions change, on average, in each of these intervals
Sum the effect across all intervals -
effects relative to an average, centered around 0
isolates one effect from the other

**Global Surrogates**
If you want to distill some insights that are too difficult to interpret by other means - some rules that explain underlying logic

- or coefficients that capture magnitude and direction of a feature for the model
  these features built into intrinisically interpretable models.

white-box model trained with black-box model's predictions
certain models designed to be used as surrogates - TREPAN; BAyesian Rule List Classifier (BRLC)

Used Decision Tree for hierarchy, RuleFit understand rules
