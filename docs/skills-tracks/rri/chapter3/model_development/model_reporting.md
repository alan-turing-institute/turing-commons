# Model Reporting

Over the course of the previous activities, your project team will have created many diverse artefacts and forms of documentation.
For example, during project planning you may have created a series of risk and impact assessments, or during exploratory data analysis you will have developed a set of notebooks explaining how you imported, cleaned, and analysed your data.
In some cases, the artefacts will be by-products (e.g., system logs).
In other cases, they will be the specific goal of the associated activity.
Model reporting is an example of this latter set.

In short, model reporting is a process of developing and integrating documentation and evidence about the processes by which your model was designed and developed (e.g., trained, tested, and evaluated), as well as how it ought to be used or deployed.

What information you need to include is going to vary based on the type of project you are undertaking, and the intended use context. For example, a model developed by a private company that is sold to the NHS in England for the purpose of supporting radiologists when carrying out diagnosis in a hospital will need to be more thoroughly documented than a NLP model used as in a simple chatbot UI to support customer queries on an e-commerce website.

In general, however, a model report is likely to include information about the data (e.g., size, source, method of collection, any sensitive attributes), the datasets used to train, test, and validate the model (e.g. training-testing distributions), the performance measures selected for evaluating the model (e.g. decision thresholds for classifiers, accuracy metrics), the intended use of the model, and any legal or ethical considerations associated with the model's use (e.g. fairness constraints, use of politically sensitive demographic features).

There are several templates (and tools) that exist to help researchers and developers identify what information ought to be documented, but there are typically advantages and disadvantages associated with each of them.
To give just a few examples:

- Datasheets for Datasets
- TRIPOD statement
- Model Cards for Model Reporting
- Factsheets

When evaluating whether to use or repurposes tools such as these, it is important to consider the context in which you are developing.
A model produced within the context of a publicly-funded research project may have certain disclosure obligations that are not mandatory for models developed in a commercial context.
Alternatively, it may just be best practice to support reproducibility by considering how your model report adheres to principles such as the FAIR guidelines.

In the next activity, we will reflect on the scope and content of some hypothetical model reports and grapple with ethical questions, such as the trade-off between transparency and privacy.
