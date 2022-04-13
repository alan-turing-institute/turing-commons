# Data Extraction and Procurement

![An image depicting several people and digital avatars with varying levels of fidelity.](../../../assets/images/illustrations/representation-background.png)

Ideally, the project team should have a clear idea in mind (from the planning and problem formulation stages) of what data are needed prior to collection, extraction, or procurement.
This can help mitigate risks associated with over-collection of data (e.g. increased privacy or security concerns) and help align the project with values such as *data minimisation* {cite:p}`ico2020`.
Of course, this stage may need to be revisited after carrying out subsequent tasks (e.g. data analysis, preprocessing, model testing) if it is clear that insufficient or imbalanced data were collected to achieve the project's goals.

Where data is procured, questions about provenance arise (e.g. legal issues, concerns about informed consent of human data subjects).
For instance, what information about the dataset is necessary to provide sufficient assurance to the team that they are procuring data that has been reliably collected by another party.
Or, will they be able to reuse and repurpose the data for their intended project.
The procured data will need to be sufficiently representative of the intended target domain of the project if it is to be useful.

Generally, addressing these issues and ensuring responsible data extraction and procurement requires the incorporation of myriad forms of expertise into decision-making. This can include,

- legal expertise (e.g., data protection officer) who is able to inform the project team of the relevant lawful bases for data collection and help;
- ethical expertise (e.g., whether the various rights and freedoms of data subjects have been properly respected);
- domain expertise (e.g., whether the method of original data collection, the expected quantity of data, and the variety of features, will be sufficient based on the problem being addressed, as formulated in the previous stage); and
- personal expertise (e.g., whether the data subjects are likely to be willing to provide access to all the data being requested)

## The FAIR Principles

At this stage in a research project, it is also important to address the long-term sustainability of your work.
One component of research sustainability is the active support of reproducibility of research.
To this end, the [FAIR guiding principles](https://www.go-fair.org/fair-principles/) for scientific data management and stewardship were developed, as a means to improve the *F*indability, *A*ccessibility, *I*nteroperability, and *R*euse of research data and digital assets.

In summary, data should be,

### Findable

> The first step in (re)using data is to find them. Metadata and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services.

### Accessible

> Once the user finds the required data, she/he/they need to know how can they be accessed, possibly including authentication and authorisation.

### Interoperable

> The data usually need to be integrated with other data. In addition, the data need to interoperate with applications or workflows for analysis, storage, and processing.

### Reusable

> The ultimate goal of FAIR is to optimise the reuse of data. To achieve this, metadata and data should be well-described so that they can be replicated and/or combined in different settings.

We won't delve into these principles in any further detail, as it is beyond the scope of this course.
However, there is more information on the [Go-FAIR website](https://www.go-fair.org/fair-principles/) and a great guide over on the [Turing Way](https://the-turing-way.netlify.app/welcome.html) {cite}`community2019`.
