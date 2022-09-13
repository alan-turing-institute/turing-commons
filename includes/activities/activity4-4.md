# Activity 9: Designing Model Reports

In this activity you will consider what criteria or information ought to be included in a model report for the case studies that you have been working with over the course of this chapter.

When thinking about what to add, you can consult the following resources:

```{dropdown} TRIPOD Statement
The TRIPOD statement was designed to systematise the reporting of models developed (or validated) in a *medical research context* {cite}`collins2015`. Therefore, many of the items will be very specific but could also be helpful for inspiration—[Link to Checklist](https://www.tripod-statement.org/wp-content/uploads/2020/01/Tripod-Checklist-Prediction-Model-Development-and-Validation-PDF.pdf).
```

```{dropdown} Model Card Template
The [Model Cards for Model Reporting](https://modelcards.withgoogle.com/about) project, by Google, and first presented in {cite}`mitchell2019`, presents a helpful summary of features to include in a model report (or, "model card").
![Model Cards](../../../images/graphics/model-cards.png)
```

```{dropdown} The Data Nutrition Project
Inspired by the food nutrition labels, this project—led by Assembly, a program run by the MIT Media Lab and the Berkman Klein Center— seeks to develop a simple summary of the features that are salient for datasets. 

[Visit Site](https://datanutrition.org/)

![Example of a Data Nutrition Label](../../../images/graphics/datafacts.png)
```

However, you should also think about the specific context in which your model is likely to be deployed and the domain-specific risks that need to be considered.
Therefore, you should also consider each item's inclusion carefully and discuss whether there may be any issues by including the information.
For instance, does including the full list of features used by the model pose an intellectual property risk or a representational risk to stakeholders?
If so, should the model report only be shared with specific parties?

Some example questions that you could ask include:

- Are there limits on transparency or disclosure of information? If so, is there another form of assurance that can be provided?
- If your model has been trained on sensitive information, does your model reporting risk violation of data privacy or protection principles?
- Should your model report be published publicly, or does this increase the risk of security breaches (e.g. model inversion attacks)?
- If your model is presented in a research context, do other research teams have sufficient information to reproduce or replicate your model?
- Who is the primary audience of your model? What information are they likely to benefit from having access to?

We will use HackMD to collaboratively design these cards.

<!---

### Activity 8: Designing Model Cards

In this activity you will design hypothetical model reports for the case studies that you have been considering throughout the chapter.

Please visit https://bit.ly/3B4VllZ to view the associated instructions.

--->