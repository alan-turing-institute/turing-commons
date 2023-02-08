# Introducing the Project Lifecycle (A Sociotechnical Approach)

There are many ways of carving up the lifecycle for a data science or AI project (hereafter, ‘project lifecycle’).[^assurance]
For instance,[@sweenor2020] break it into four stages: Build, Manage, Deploy & Integrate, Monitor.[^mlops]
Ashmore[@ashmore2019] also identify four stages, which have a more specific focus on data science: data management, model learning, model verification, and model deployment.

[^assurance]: The following text is adapted from a publication titled, 'Ethical Assurance: A practical approach to the responsible design, development, and deployment of data-driven technologies'.[@burr2021]

[^mlops]: These four stages are influenced by an ‘ML OPs’ perspective.
The term ‘MLOps’ refers to the application of DevOps practices to ML pipelines.
The term is often used in an inclusive manner to incorporate traditional statistical or data science practices that support the ML lifecycle, but are not themselves constitutive of machine learning (e.g. exploratory data analysis), as well as deployment practices that are important within business and operational contexts (e.g. monitoring key performance indicators).

The multiplicity of approaches is likely a product of the evolution of diverse methods in data mining/analytics, the significant impact of ML on research and innovation, and the specific practices and considerations inherent to each of the various domains where ML techniques are applied.
While there are many benefits of existing frameworks, they do not tend to focus on the wider social or ethical aspects that interweave throughout the various stages of a ML lifecycle.

[Project-lifecycle](../chapter3/index.md), therefore, presents a model of a *typical* lifecycle for a project involving data science or the production of an ML/AI system.
We have designed this model to support the ethical reflection and deliberation that is characteristic of responsible data science and AI, while remaining faithful to the technical details.
However, it is important to note that the model is a heuristic for reflection and deliberation.
Therefore, it is not intended to be perfectly capture of describe the processes for all data science or AI projects.

<figure markdown>
  ![A model of a typical data science and AI project](../../assets/images/graphics/project-lifecycle.png){ align="center" }
  <figcaption>The Project Lifecycle. The overarching stages of design, development, and deployment (for a typical data-driven project) can be split into indicative tasks and activities. In practice, both the stages and the tasks will overlap with their neighbours, and may be revisited where a particular task requires an iterative approach. The spiral indicates that this is a diachronic, macroscopic process that evolves and develops over time, and as the deployment stage finishes, a new iteration is likely to begin.</figcaption>
</figure>

To begin, the inner circle breaks the project lifecycle into three processes:

1. (Project) Design
2. (Model) Development
3. (System) Deployment

These terms are intended to be maximally inclusive.
For example, the design stage encompasses any project task or decision-making process that scaffolds or sets constraints on later project stages (i.e. design system constraints).
Importantly, this includes ethical, social, and legal constraints, which we will discuss later.

Each of the stages shades into its neighbours, as there is no clear boundary that differentiates certain project design activities (e.g. data extraction and exploratory analysis) from model design activities (e.g. preprocessing and feature engineering, model selection).
As such, the design stage overlaps with the development stage, but the latter extends to include the actual process of training, testing, and validating a ML model.
Similarly, the process of productionalising a model within a system can be thought of as both a development and deployment activity.
And, so, the deployment stage overlaps with the ‘development’ stage, and also overlaps with the ‘design’ stage because the deployment of a system should be thought of as an ongoing process (e.g. where new data are used to continuously train the ML model, or, the decision to de-provision a model may require the planning and design of a new model if the older (legacy) system becomes outdated).
For these reasons, the project lifecycle is depicted as a spiral.
However, despite the unidirectional nature of the arrows, we also acknowledge that ML/AI research and innovation is frequently an iterative process.
Therefore, the singular direction is only present at a macroscopic level of abstraction (i.e., the overall direction of progress for a project), and allows for some inevitable back and forth between the stages at the microscopic level.

The three higher-level stages can be thought of as a useful heuristic for approaching the project lifecycle.
However, each higher-level stage subsumes a wide variety of tasks and activities that are likely to be carried out by different individuals, teams, and organisations, depending on their specific roles and responsibilities (e.g. procurement of data).
Therefore, it is important to break each of the three higher-level stages into their (typical) constituent parts, which are likely to vary to some extent between specific projects or within particular organisations.
In doing so, we expose a wide range of diverse tasks, each of which give rise to a variety of ethical, social, and legal challenges.

[Chapter 3](../chapter3/index.md) is dedicated to exploring each specific stage and activity in detail. The remainder of this chapter covers some topics that apply to the project lifecycle as a whole.
