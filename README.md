# Explainability Tutorials & Libraries

## Raw Data - Missouri Highway Patrol Accident Data
Leveraging a real data set scrapped from [MSHP](https://www.mshp.dps.missouri.gov/HP68/SearchAction)

The base schema is:
![Basic Dataflow](./artifacts/MSHP-Explainability.svg)

## Exploratory Data Analysis
Leverage following core libraries
* Generate Automated Reports
  * [dataprep](https://docs.dataprep.ai/index.html#) - last update Jul 7th, 2022
    * Observation: wraps other libraries like connectorx, pandas-profile. The interface is clean
  * [SweetViz](https://pypi.org/project/sweetviz/) - last update June 8th, 2022
    * I like this project a lot, has a correlation among categorical features which is nice. 
  * [pandas profiling](https://pypi.org/project/pandas-profiling/) - deprecated for ydata-profiling
  * [ydata-profiling - replace pandas profiling](https://github.com/ydataai/ydata-profiling) - last update a couple days ago <-- does Spark too
    * Note - report of ydata_profiling looks similiar to dataprep
    * fairly robust, nice interface to attract data and get alerts about potential issues like 'constant'
* Exploratory Inspections
  * [Lux](https://github.com/lux-org/lux) <-- last update May, 2022
    * One of my favorite projects; see enhancements like chart me but it's buggy on my data set. Parking lot idea - perhaps incorporate best of ideas. 
  * [Chart Me](https://pypi.org/project/chart_me/) <-- My project, similar to dataprep - more control 
* Explore other candidates
  * [autoviz](https://pypi.org/project/autoviz/)
  * [yopo](https://pypi.org/project/yopo/)
    * Looks interesting - Flask/Dash currently has dependency issues on Werkzeug. I don't want to triage. 

## Data Cleansing and Feature Engineering
  * [dataprep](https://docs.dataprep.ai/index.html#)

## Microsofts InterpretML
[Interpret.Ml](https://interpret.ml/)
[Whitepaper](https://www.microsoft.com/en-us/research/uploads/prod/2020/05/InterpretML-Whitepaper.pdf)
InterpretML helps users gain a better understanding of their model's overall behavior 
* (“global explanation”), understand the reasons behind
* individual predictions (“local explanation”), and debug their model’s predictions by exploring what
* similar data instances have received different outcomes.
**Explainable Boosting Machine (EBM)**
* EBMs produce exact explanations and are editable by domain experts.

* Interpretability Technique	Type
  * Explainable Boosting	glassbox model
  * Decision Tree	glassbox model
  * Decision Rule List	glassbox model
  * Linear/Logistic Regression	glassbox model
  * SHAP Kernel Explainer	blackbox explainer
  * LIME	blackbox explainer
  * Morris Sensitivity Analysis	blackbox explainer
  * Partial Dependence	blackbox explainer

