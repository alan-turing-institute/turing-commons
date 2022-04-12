# Preprocessing and Feature Engineering

Pre-processing and feature engineering is a vital but often lengthy process, which overlaps with the design tasks in the previous section—most notably the data analysis activities.
It also shares with them the potential for human choices to introduce biases and discriminatory patterns into the ML/AI workflow.
Tasks at this stage include (additional) data cleaning, data wrangling or normalisation, and data reduction or augmentation.
Whereas data analysis is oriented towards a provisional understanding the dataset (e.g., analysing possible relationships between variables), preprocessing is directed towards the model development tasks.

It is well understood that the methods employed for each of these tasks can have a significant impact on the model's performance (e.g. removing rows or columns can affect the predictive power of the model). As Ashmore et al. {cite:p}`ashmore2019` note, there are also various desiderata that motivate the tasks, such as the need to ensure the dataset that will feed into the subsequent stages is relevant, complete, balanced, and accurate.

Furthermore, at this stage, human decisions about how to group or disaggregate input features (e.g. how to carve up categories of gender or ethnic groups) or about which input features to exclude altogether (e.g. leaving out deprivation indicators in a predictive model for clinical diagnostics) can have significant downstream influences on the fairness and equity of an ML/AI system.
