# Transparency and Explainability

<figure markdown>
  ![phone-peel](../../assets/images/illustrations/phone-peel-background.png){ align="center" }
</figure>

## Introduction to transparency and explainability

## Defining transparent AI

Transparency as a principle of AI ethics differs a bit in meaning from the everyday use of the term. The common dictionary understanding of transparency defines it as either 

(1) the quality an object has when one can see clearly through it or 

(2) the quality of a situation or process that can be clearly justified and explained because it is open to inspection and free from secrets. 
 
Transparency as a principle of AI ethics encompasses both of these meanings:
 
On the one hand, transparent AI involves the interpretability of a given AI system, i.e. the ability to know how and why a model performed the way it did in a specific context and therefore to understand the rationale behind its decision or behaviour. This sort of transparency is often referred to by way of the metaphor of ‘opening the black box’ of AI. It involves content clarification and intelligibility or explicability.
 
On the other hand, transparent AI involves the justifiability of both of the processes that go into its design and implementation and of its outcome. It therefore involves the soundness of the justification of its use. In this more normative meaning, transparent AI is practically justifiable in an unrestricted way if one can demonstrate that both the design and implementation processes that have gone into the particular decision or behaviour of a system and the decision or behaviour itself are sustainable, safe, fair, and driven by responsibly managed data. 

## Process-based vs outcome-based

The two-pronged definition of transparency as a principle of AI ethics asks that the project team thinks about transparent AI 

- in terms of the process behind it (the design and implementation practices that lead to an algorithmically supported outcome); and,

- in terms of its product (the content and justification of that outcome).

This also means that explanations are provided to impacted stakeholders that demonstrate how the team and all others involved in the development of the system acted responsibly when choosing the processes behind its design and deployment; and make the reasoning behind the outcome of that decision clear.

**Process-based explanation** of AI systems are about demonstrating that good governance processes and best practices have been followed throughout the design, development and use of the AI system. This entails demonstrating that considerations of sustainability, safety, fairness, and responsible data management were operative end-to-end in the project lifecycle. 

For example, if trying to explain the fairness and safety of a particular AI-assisted decision, one component of this explanation will involve establishing that adequate measures across the system’s production and deployment have been taken to ensure that its outcome is fair and safe.
 
**Outcome-based explanations** of AI systems are about clarifying the results of a specific decision. They involve explaining the reasoning behind a *particular algorithmically generated outcome* in plain, easily understandable, and everyday language that is socially meaningful to impacted stakeholders (understandable in terms of the contextual factors and relationships that it implicates). 

- If there is meaningful human involvement in the decision-making process, 
it should also be made clear to the affected individual how and why a human judgement that is assisted by an AI output was reached.

In addition, an adequate explanantion will also need to confirm that the actual outcome of an AI decision meets criteria previously established in the design process to ensure that the AI system is being used in a fair, safe, and ethical way. An explanation to affected stakeholders should also include a demonstration that a specific decision or behaviour of the system is sustainable, safe, fair, and driven by data that has been responsibly managed. 

<figure markdown>
  ![phone-peel](../../assets/images/illustrations/lifecycle-stylised-alt.png){ align="center" }
</figure>


## Six main types of explanations

!!! abstract

    1. Rationale explanation
    2. Responsibility explanation
    3. Data explanation
    4. Fairness explanation
    5. Safety and performance explanation
    6. Impact explanation

### Rationale explanation
What does this explanation help people understand?
 
**It is about the ‘why?’ of an AI decision.** It helps people understand the reasons that led to a decision outcome, in an accessible way.
 
What does this type of explanation include?

- How the system performed and behaved to get to that decision outcome.

- How the different components in the AI system led it to transform inputs into outputs in a particular way. This will help communicate which features, interactions, and parameters were most significant.

- How these technical components of the logic underlying the result can provide supporting evidence for the decision reached.

- How this underlying logic can be conveyed as easily understandable reasons to decision recipients.

- How do the system’s results apply to the concrete context and life situation of the affected individual.
 
What rationale explanations might answer:

- Will the selected algorithmic model, or set of models, provide a degree of interpretability that corresponds with its impact on affected individuals?

- Are the supplementary explanation tools being used to help make the complex system explainable good enough to provide meaningful and accurate information about its underlying logic?
 
**What information goes into rationale explanations**

As with the other types of explanation, rationale explanations can be process-based or outcome-based.

Process-based explanations clarify:
 
- How the procedures set up help provide meaningful explanations of the underlying logic of the AI model’s results.

- How these procedures are suitable given the model’s particular domain context and its possible impacts on the affected decision recipients and wider society.

- How the system’s design and deployment workflow has been set up so that it is appropriately interpretable and explainable, including its data collection and preprocessing, model selection, explanation extraction, and explanation delivery procedures.
 
Outcome-based explanations provide:

- The formal and logical rationale of the AI system – how the system is verified against its formal specifications. In this way, one can verify that the AI system will operate reliably and behave in accordance with its intended functionality.

- The technical rationale of the system’s output – how the model’s components (its variables and rules) transform inputs into outputs, so that the role these components play in producing that output is known. By understanding the roles and functions of the individual components, it is possible to identify the features and parameters that significantly influence a particular output.

- Translation of the system’s workings – its input and output variables, parameters and so on – into accessible everyday language. This enables those in charge of the AI system to clarify, in plain and understandable terms, what role these factors play in reasoning about the real-world problem that the model is trying to address or solve.

- Clarification of how a statistical result is applied to the individual concerned.

### Responsibility explanation
What does this explanation help people understand?
 
It helps people understand **‘who’ is involved in the development and management of the AI model**, and **‘who’ to contact for a human review of a decision**.
 
What does this type of explanation include?
 
- Who is accountable at each stage of the AI system’s design and deployment, from defining outcomes for the system at its initial phase of design, through to providing the explanation to the affected individual at the end.

- Definitions of the mechanisms by which each of these people will be held accountable, as well as how the design and implementation processes of the AI system have been made traceable and auditable.

**What information goes into responsibility explanations**
 
Process-based explanations clarify:
 
- The roles and functions across the organisation that are involved in the various stages of developing and implementing an AI system, including any human involvement in the decision-making. If the system, or parts of it, are procured, thjen information about the providers or developers involved should be included.

- Broadly, what the roles do, why they are important, and where overall responsibility lies for management of the AI model – who is ultimately accountable.

- Who is responsible at each step from the design of an AI system through to its implementation to make sure that there is effective accountability throughout.
 
Outcome-based explanations:
 
Because a responsibility explanation largely has to do with the governance of the design and implementation of AI systems, it is, in a strict sense, entirely process-based. Even so, there is important information about post-decision procedures that should be provided:
 
- Cover information on how to request a human review of an AI-enabled decision or object to the use of AI, including details on who to contact, and what the next steps will be (e.g., how long it will take, what the human reviewer will take into account, how they will present their own decision and explanation).

- Give individuals a way to directly contact the role or team responsible for the review (this does not necessarily have to be a specific individual within the organisation).

### Data explanation

What does this explanation help people understand?
 
Data explanations are about **the ‘what’ of AI-assisted decisions**. They let people know what data about them were used in a particular AI decision, as well as any other sources of data. Generally, they also help individuals understand more about the data used to train and test the AI model. 
 
What does this type of explanation include?
 
- How the data used to train, test, and validate an AI model was managed and utilised from collection through processing and monitoring.

- Which data was used in a particular decision and how.

**What information goes into data explanations**

Process-based explanations include:
 
-  What training/testing/validating data was collected, the sources of that data, and the methods that were used to collect it.

- Who took part in choosing the data to be collected or procured and who was involved in its recording or acquisition. 

- How procured or third-party provided data was vetted.

- How data quality was assessed and the steps that were taken to address any quality issues discovered, such as completing or removing data.

- What the training/testing/validating split was and how it was determined.

-  How data pre-processing, labelling, and augmentation supported the interpretability and explainability of the model.

- What measures were taken to ensure the data used to train, test, and validate the system was representative, relevant, accurately measured, and generalisable.

- How potential bias and discrimination in the dataset have been mitigated.
 
Outcome-based explanations:
 
- Clarify the input data used for a specific decision, and the sources of that data. This is outcome-based because it refers to the AI system’s result for a particular decision recipient.

- In some cases, the output data may also require an explanation, particularly where the decision recipient has been placed in a category which may not be clear to them. For example, in the case of anomaly detection for financial fraud identification, the output might be a distance measure which places them at a certain distance away from other people based on their transaction history. Such a classification may require an explanation.

### Fairness explanation

What does this explanation help people understand?
 
The fairness explanation is about helping people understand the steps have been taken (and will continue to be taken) to ensure an AI decisions are generally unbiased and equitable. 
It also gives people an understanding of whether or not they have been treated equitably themselves.
 
What does this type of explanation include?
 
An explanation of fairness can relate to several stages of the design, development and deployment of AI systems:

 
A) Data fairness: 
The system is trained and tested on properly representative, relevant, accurately measured, and generalisable datasets (note that this dataset fairness component will overlap with data explanation). 

This may include showing that the data used is:

- as representative as possible of all those affected;

- sufficient in terms of its quantity and quality, so it represents the underlying population and the phenomenon being modelled;

- assessed and recorded through suitable, reliable and impartial sources of measurement and has been sourced through sound collection methods;

- up-to-date and accurately reflects the characteristics of individuals, populations and the phenomena that is being modeled; and

- relevant by calling on domain experts to help the team understand, assess and use the most appropriate sources and types of data to serve the project's objectives.
 
B) Design fairness:

It needs to be appropriately shown the AI model's architectures do not include target variables, features,processes, or analytical structures (correlations, interactions, and inferences) which are unreasonable or unjustifiable. 

This may include showing that the following has been done:

- Any underlying structural biases that may play a role in translating the objectives into target variables and measurable proxies have been identified. When defining the problem at the start of the AI project, these biases could influence what system designers expect target variables to measure and what they statistically represent.

- Biases in the data pre-processing phase have been mitigated by taking into account the sector or organisational context in which the AI system is being operated. When this process is automated or outsourced, one should be able to show that what was done has been reviewed and that oversight was maintained throughout. 

- Information on the context of the metadata should also be included, so that those coming to the pre-processed data later on have access to the relevant properties when they undertake bias mitigation.

- Mitigated bias when the feature space was determined (i.e., when relevant features were selected as input variables for your model). Choices made about grouping or separating and including or excluding features, as well as more general judgements about the comprehensiveness or coarseness of the total set of features, may have consequences for protected groups of people.

- Mitigated bias when tuning parameters and setting metrics at the modelling, testing and evaluation stages (i.e., into the trained model). The AI development team should iterate the model and peer review it to help ensure that how they choose to adjust the dials and metrics of the model are in line with your objectives of mitigating bias.

- Mitigated bias by watching for hidden proxies for discriminatory features in the trained model, as these may act as influences on a model’s output. Designers should also look into whether the significant correlations and inferences determined by the model’s learning mechanisms are justifiable.
 
C) Metric-based fairness: 
This is about making sure that the model does not have discriminatory or inequitable impact on the lives of the people it affects. This may include showing that:

- The formal definition(s) of fairness that has been chosen is made explicit, as well as the reason why this decision. Data scientists can apply different formalised fairness criteria to choose how specific groups in a selected set will receive benefits in comparison to others in the same set, or how the accuracy or precision of the model will be distributed among subgroups; and

- the method applied in operationalising theformalised fairness criteria, for example, by reweighting model parameters; embedding trade-offs in a classification procedure; or re-tooling algorithmic results to adjust for outcome preferences.

D) Implementation fairness: 
The AI sysetem is deployed by users sufficiently trained to implement it responsibly and without bias. This may include showing that implementers of the AI system have been appropriately prepared and trained to:

- avoid automation bias (over-relying on the outputs of AI systems) or automation-distrust bias (under-relying on AI system outputs because of a lack of trust in them);

- use its results with an active awareness of the specific context in which they are being applied. They should understand the particular circumstances of the individual to which that output is being applied; and

- understand the limitations of the system. This includes understanding the statistical uncertainty associated with the result as well as the relevant error rates and performance metrics.


**What information goes into fairness explanations**

This explanation is about providing people with appropriately simplified and concise information on the considerations, measures and testing you carry out to make sure that your AI system is equitable and that bias has been optimally mitigated. Fairness considerations come into play through the whole lifecycle of an AI model, from inception to deployment, monitoring and review.

Process-based explanations include:

- the chosen measures to mitigate risks of bias and discrimination at the data collection, preparation, model design and testing stages;

- how these measures were chosen and how managed informational barriers to bias-aware design such as limited access to data about protected or sensitive traits of concern have been managed; and

- the results of the initial (and ongoing) fairness testing, self-assessment, and external validation – showing that the chosen fairness measures are deliberately and effectively being integrated into model design. This can be done by showing that different groups of people receive similar outcomes, or that protected characteristics have not played a factor in the results.
 
Outcome-based explanations include:

- details about how the formal fairness criteria were implemented in the case of a particular decision or output;

- presentation of the relevant fairness metrics and performance measurements in the delivery interface of your model. This should be geared to a non-technical audience and done in an easily understandable way; and

- explanations of how others similar to the individual were treated (i.e., whether they received the same decision outcome as the individual). For example, information generated from counter-factual scenarios could be used to show whether or not someone with similar characteristics, but of a different ethnicity or gender, would receive the same decision outcome as the individual.


### Safety and performance explanation

What does this explanation help people understand?
The safety and performance explanation helps people understand the measures that have been put in place, and the steps that have been taken (and are continuously bein taken) to maximise the accuracy, reliability, security and robustness of the decisions the AI model helps make. It can also be used to justify the type of AI system chosen, such as comparisons to other systems or human decision makers.
 
!!! info "Key concepts:"
 
        **Accuracy:** the proportion of examples for which  model generates a correct output. This component may also include other related performance measures such as precision, sensitivity (true positives), and specificity (true negatives). Individuals may want to understand how accurate, precise, and sensitive the output was in their particular case.
 
        **Reliability:** how dependably the AI system does what it was intended to do. If it did not do what it was programmed to carry out, individuals may want to know why, and whether this happened in the process of producing the decision that affected them.
 
        **Security:** the system is able to protect its architecture from unauthorised modification or damage of any of its component parts; the system remains continuously functional and accessible to its authorised users and keeps confidential and private information secure, even under hostile or adversarial conditions.
 
        **Robustness:** the system functions reliably and accurately in practice. Individuals may want to know how well the system works if things go wrong, how this has been anticipated and tested, and how the system has been immunised from adversarial attacks.

**What information goes into safety and performance explanations**
 
Process-based explanations include:

For accuracy:

- How is accuracy measured (e.g., maximising precision to reduce the risk of false negatives).
- Why those measures were chosen, and what the assurance process behind it was.
- What was done at the data collection stage to ensure that the training data was up-to-date and reflective of the characteristics of the people to whom the results apply.

- What kinds of external validation has undertaken to test and confirm your model’s ‘ground truth’.

- What the overall accuracy rate of the system was at testing stage.

- What is done to monitor this (e.g., measuring for concept drift over time).
 
For reliability:

- How it is measured and what the assurance process behind it is.

- Results of the formal verification of the system’s programming specifications, i.e., how encoded requirements have been mathematically verified.
 
For security: 
- How it is measured and what the assurance process behind it is, e.g., how limitation have been set on who is able to access the system, when, and how.

- How the security of confidential and private information that is processed in the model has been managed.
 
For robustness:

- How it is measured.

- Why the specific measures were chosen.

- What the assurance process behind it is, e.g., how the system has been stress-tested to understand how it responds to adversarial intervention, implementer error, or skewed goal-execution by an automated learner (in reinforcement learning applications).
 

Outcome-based explanations:

While one might not be able to guarantee accuracy at an individual level, one should be able to provide assurance that, at run-time, an AI system operated reliably, securely, and robustly for a specific decision.

- In the case of accuracy and the other performance metrics, however the resultsof cross-validation (training/ testing splits) and any external validation carried out, should be included in the model's delivery interface.


- Other relevant information that could be included is:  information related to the system’s confusion matrix (the table that provides the range of performance metrics) and ROC curve (receiver operating characteristics)/ AUC (area under the curve). Include guidance for users and affected individuals that makes the meaning of these measurement methods, and specifically the ones that have been chosen, easily accessible and understandable. This should also include a clear representation of the uncertainty of the results (e.g., confidence intervals and error bars).


### Impact explanation
 
What does this explanation help people understand?

An impact explanation helps people understand how the effects that an AI decision-support system may have on an individual, i.e., what the outcome of the decision means for them, have been considered. 

It is also about helping individuals to understand the broader societal effects that the use of this AI system may have. This can help reassure people that the use of AI will be of benefit. Impact explanations are therefore often well suited to delivery before an AI-assisted decision has been made. 
 
What does this type of explanation include?

Demonstrate that thought has been put into how an AI system will potentially affect individuals and wider society. It is important to clearly show affected individuals the process done to determine these possible impacts.

**What information goes into impact explanations**
 
Process-based explanations include:

- Showing the considerations givne to the AI system’s potential effects, how these considerations were undertaken, and the measures and steps taken to mitigate possible negative impacts on society, and to amplify the positive effects.

- Information on the plan in place to monitor and re-assess impacts while the system is deployed should also be included.
 
Outcome-based explanations:

Although impact explanations are mainly about demonstrating that appropriate forethought has been given into the potential ‘big picture’ effects, it is also important to consider how to help recipients understand the impact of the AI-assisted decisions that specifically affect them. For instance, one might explain the consequences for the individual of the different possible decision outcomes and how, in some cases, changes in their behaviour would have brought about a different outcome with more positive impacts. This use of counterfactual assessment would help decision recipients make changes that could lead to a different outcome in the future or allow them to challenge the decision.

## Putting the Principle of Transparency and Explainability into Practice

!!! success

    - Task 1 (Project Planning): Select priority explanations by considering the domain, use case and potential impacts
    - Task 2 (Data Extraction or Procurement, Data Analysis): Collect and pre-process data in an explanation-aware manner
    - Task 3 (Model Selection): Build a system that is able to extract relevant information for a range of explanation types
    - Task 4 (Model Reporting): Translate the rationale of the system’s results into useable and easily understandable reasons
    - Task 5: (User Training) Prepare implementers to deploy the AI system
    - Task 6 (Model Reporting): Consider how to build and present an explanation



There are a number of tasks both to help in the design and deployment of appropriately transparent and explainable AI systems and to assist in providing clarification of the results these systems produce to a range of impacted stakeholders (from operators, implementers, and auditors to decision recipients).
These tasks make up Transparency and Explainability Assurance Management for AI projects, offering a systematic approach to:

- Designing, developing, and deploying AI projects in a transparent and explanation-aware fashion; and selecting, extracting and delivering explanations that are differentiated according to the needs and skills of the different audiences they are directed at.

**Task 1 (Project Planning): Select priority explanations by considering the domain, use case and potential impacts**

- Understanding the different types of explanation will serve to identify the dimensions of an explanation that decision recipients will find useful. 
In most cases, explaining AI-assisted decisions involves identifying what is happening in the AI system and who is responsible. That means prioritising the rationale and responsibility explanation types.

- The setting and the sector are important in figuring out what kinds of explanation one should be able to provide. Therefore considering the domain context and use case is crucial to prioritise which explanations the team should be prepared to give.

- In addition, consider the potential impacts of the particular use of the AI system to determine which other types of explanation should be provided. This will also help in thinking about how much information is required, and how comprehensive it should be.

- Choosing what to prioritise is not an exact science. Hopefully the explanations prioritised will coincide with what the majority of the people impacted want to know, but it is unlikely that every individual will have all their questions answered. Having a clear and documented rationale for the explanations prioritised will probably also be useful for your own accountability or auditing purposes.

**Task 2 (Data Extraction or Procurement, Data Analysis): Collect and pre-process data in an explanation-aware manner**

The data collected and pre-processed before inputting it into the system has an important role to play in the ability to derive each explanation type. Careful labelling and selection of input data can help provide information for your rationale explanation.

Providing details about who is responsible at each stage of data collection and pre-processing is part of being more transparent. This is part of the responsibility explanation (information can be drawn from Workflow Governance Map, covered in the AI accountability section of this course).

Drawing from the dataset factsheet can aid in providing data explanations, including the following information:

- the source of the training data;
- how it was collected;
- assessments about its quality; and
- steps taken to address quality issues, such as completing or removing data

Check the data used within the model to ensure it is sufficiently representative of those it is making decisions about. Another issue to consider is whether pre-processing techniques, such as re-weighting, are required.  These decisions should be documented in the Bias Self-Assessments, and will help construct the fairness explanation.


**Task 3 (Model Selection): Build a system that is able to extract relevant information for a range of explanation types**

Deriving the rationale explanation is key to understanding an AI system (as well as complying with parts of the GDPR).
It requires looking ‘under the hood’ and helps in gathering the information needed for some of the other explanations, such as safety and fairness. 

However, this is a complex task that requires knowing when to use more and less interpretable models and how to understand their outputs.
To choose the right AI model for the particular explanation needs, one should think about the domain the system will be working in, and the potential impact of the system.

When selecting a model for an AI project, it is important to consider whether:

- there are costs and benefits of using a newer and potentially less explainable AI model;
- the data used requires a more or less explainable system;
- the use case and domain context encourage choosing an inherently interpretable system; 
- the processing needs lead to the selection of a ‘black box’ model; and
- the supplementary interpretability tools that help  explain a ‘black box’ model (if chosen) are appropriate given the context.

To extract explanations from inherently interpretable models, look at the logic of the model’s mapping function by exploring it and its results directly.
On the other hand, there are many techniques used to extract explanations from ‘black box’ systems. Make sure that they provide a reliable and accurate representation of the system’s behaviour.


**Task 4 (Model Reporting): Translate the rationale of the system’s results into useable and easily understandable reasons**
 
Once the rationale of the underlying logic of the AI model has been extracted, the statistical output needs to be incorporated into the wider decision-making process.

Implementers of the outputs from the AI system will need to recognise the factors that they see as legitimate determinants of the outcome they are considering.

Decision recipients should be able to easily understand how the statistical result has been applied to their particular case.
 
**Task 5: (User Training) Prepare implementers to deploy the AI system**

In cases where decisions are not fully automated, implementers need to be meaningfully involved.

This means that they need to be appropriately trained to use the model’s results responsibly and fairly.

Their training should cover:
- the basics of how machine learning works;
- the limitations of AI and automated decision-support technologies;
- the benefits and risks of deploying these systems to assist decision-making, particularly how they help humans come to judgements rather than replacing that judgement; and
- how to manage cognitive biases, including both decision-automation bias and automation-distrust bias.
 
**Task 6 (Model Reporting): Consider how to build and present an explanation**
Gathering together the information gained when implementing Tasks 1-4 is the first step towards building an explanation. This includes reviewing the information and determine how this provides an evidence base for the process-based or outcome-based explanations.

Additionally, it is important to revisit the contextual factors to establish which explanation types should be prioritised.

The way an explanation is presented depends on the way AI-assisted decisions are made, and on how people might expect those responsible for the AI system to deliver explanations without using AI.

Explanations can la 'layered' by proactively providing individuals with the prioritised explanations first and making additional explanations available in further layers. This helps to avoid information (or explanation) overload.

Delivering explanations should be thought of as a conversation, rather than a one-way process. People should be able to discuss a decision with a competent human being.

Providing an explanation at the right time is also important. Proactively engaging with customers by making information available on how the AI system is used and how it aids in making decisions, can increase the trust and awareness.


<!-- ****** Question, should we include the template on transparency and explainality assurance? -->