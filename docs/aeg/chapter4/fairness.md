# AI Fairness 

## Introduction
What does it mean for an AI system to be fair? 

When thinking about fairness in the design, deployment, and deployment of AI systems, it is important to always keep in mind that these technologies, no matter how neutral they may seem, are designed and produced by human beings, who are bound by the limitations of their contexts and biases.

Human error, prejudice, and misjudgement can enter into the innovation lifecycle and create unfair biases at any point in the project delivery process from the preliminary stages of project planning, problem formulation, and data extraction to the phases of model development and system deployment.

Additionally, data-driven technologies achieve accuracy and efficacy by building inferences from datasets that record complex social and historical patterns, which themselves may contain culturally crystallised forms of bias and discrimination. 

There is no silver bullet when it comes to remediating the dangers of bias, discrimination, and unfairness in AI systems. The problem of fairness and bias mitigation in algorithmic design and use therefore has no simple or strictly technical solution.

When thinking about AI fairness, a lot of emphasis is placed on the specific inner-workings of an algorithmic system and its outputs (what we will call metric-based fairness). While this is by all means a crucial element of AI fairness which we will focus on in the course, it is important to emphasise that it is still only one of five different elements of AI fairness, all of which should be in place for an AI system to be deemed fair.

## Principle of disciminatory Non-Harm

While there are different ways to characterise or define fairness in the design and use of AI systems, we can consider the principle of discriminatory non-harm as a minimum required threshold of fairness. This principle directs us to do no harm to others through the biased or discriminatory outcomes that may result from practices of AI innovation.


::: info
**Key Concept: Principle of Discriminatory Non-Harm**
The producers and users of AI systems should prioritise the identification and mitigation of biases and discriminatory influences, which arise in the processes behind the design, development, and deployment of these systems. 
    
Developers and users of AI systems should likewise acknowledge and address discriminatory patterns that may originate (1) in the data used to train, test, and     validate the system and (2) in the model architectures (i.e., the variables, parameters, inferences, etc.) that generate system outputs.
    
The principle of discriminatory non-harm applies to any AI system that processes social or demographic data (i.e., data pertaining to features of human             subjects, population- and group-level traits and characteristics, or patterns of human activity and behaviour). However, the principle applies equally to AI    systems that process bio-physical or biomedical data. In this case, imbalanced datasets, selection biases, or measurement errors could have discriminatory effects on impacted individuals and communities—for instance, where a demographic group’s lack of representation in a biomedical dataset (e.g., one used to train a diagnostic prediction model) means that the trained system performs poorly for that group relative to others that are better represented in the data.
    
Prioritising discriminatory non-harm implies that the producers and users of AI systems ensure that the decisions and behaviours of their models do not generate discriminatory or inequitable impacts on affected individuals and communities. It can also be seen as a proportional approach to bias mitigation because it sets a baseline for fair AI systems, while, nevertheless, creating conditions for developers and users to strive towards an ideal for fair and equitable impact.
    
Finally, the scope of the principle means that, beyond designers and users,  any individuals, organisations, or departments who are procuring AI systems must ensure that the vendors of such systems can demonstrate the mitigation of potential   biases and discriminatory influences in the processes behind their production and in their outputs.
:::

How can this principle be operationalised? To make sure it is being upheld, the team designing and developing the AI system must make sure that they are following the different elements of fairness. Let's look at each in turn.

## Elements of Fairness

::: info 
**Elements of AI Fairness:**

**1. Application fairness:** The policy objectives of an AI project are acceptable to and line up with the aims, expectations, and sense of justice possessed by impacted people.

**2. Data fairness:** The AI system is trained and tested on properly representative, relevant, accurate, and generalisable datasets.

**3. Design fairness:** The AI system has a model architecture that does not include target variables, features, processes, or analytical structures (correlations, interactions, and inferences) which are unreasonable, morally objectionable, or unjustifiable.

**4. Metric-based fairness:** Clearly defined, transparent, and justifiable formal metrics of fairness have been operationalised into the AI system.

**5. Implementation fairness:** The AI system is deployed by users sufficiently trained to implement them responsibly and in a bias-aware manner.
:::

### **1. Application Fairness**

Fairness considerations should enter an AI project at the earliest possible stage of horizon scanning and project planning. The overall fairness and equity of an AI application is significantly determined by the objectives, goals, and policy choices that lie behind initial decisions to dedicate time and resources to its design, development, and deployment. 

For example, the choice made to build a biometric identification system,
which uses live facial recognition technology to identify criminal suspects at public events, may be motivated by the objective to increase public safety and security. However, many members of the public may find this use of AI technology unreasonable, disproportionate, and potentially discriminatory. In particular, members of communities historically targeted by disproportionate levels of surveillance in law enforcement contexts may be especially concerned about the potential for abuse and harm. Appropriate fairness and equity considerations should, in this case, occur at the horizon scanning and project planning stage (e.g.,as part of a stakeholder impact assessment process that includes engagement with potentially affected individuals and communities). Aligning the policy goals of a project team with the reasonable expectations and potential equity concerns of those affected is a key component of the fairness of the application. Note that in this example, we are note concerned yet with the actual otucomes of the facial recognition technology (i.e. whether it accurately recognises people from different races or ethnicities in the same proportion) but it is an even earlier question: does the impacted community think this is a fair use of this technology?
<!-- question: why do we call it fairness then? -->

Application fairness, therefore, entails that the policy objectives of an AI project are acceptable to and line up with the aims, expectations, and sense of justice possessed by those affected. As such, whether the decision to engage in the production and use of an AI technology can be described as “fairness-aware” depends upon ethical and policy considerations that are external and prior to considerations of the technical feasibility of  building an accurate and optimally performing system or the practical feasibility of accessing, collecting, or acquiring enough and the right kind of data.

Beyond this priority of assuring the equity and ethical permissibility of policy goals, application fairness requires additional considerations in framing decisions made at the horizon scanning and project scoping or planning stage.

**Equity considerations surrounding real-world context of the policy issue to be solved**
    When assessing the fairness of using an AI solution to address a particular policy issue, it is important to consider how equity considerations extend beyond the statistical and sociotechnical contexts of designing, developing, and deploying the system. Applied concepts of AI fairness and equity should not be treated, in a technology-centred way, as originating exclusively from the design and use of any particular AI system.

Nor should they exclusively be treated as abstractions that can be engineered into an AI application through technical or mathematical retooling (e.g., by operationalising formal fairness criteria). Limiting your understanding of the scope of ‘fairness’ or ‘equity’ to these two dimensions will result in an artificially constrained perspective whereby only the patterns of bias and discrimination that arise in AI innovation practices or that can be measured, formalised, or statistically digested are treated as actionable indicators of inequity.
    
Rather, equity considerations should be grounded in a human-centred  approach, which includes reflection on and critical examination of the wider social and economic patterns of disadvantage, injustice, and discrimination that arise in the real-world contexts surrounding the policy issue in question. Such considerations should include an exploration of how such patterns of inequity may lead, on the one hand, to the disparate distribution of the risks and adverse impacts of the AI system or, on the other, to a lack of equitable access to its potential benefits. For instance, while the development of an AI chatbot to replace a human serviced medical helpline may provide effective healthcare guidance for some, it could have disparate adverse impacts on others, such as vulnerable elderly populations or socioeconomically deprived groups who may face barriers to accessing and using the app. Here, reflection on the real-world contexts surrounding the provision of this type of healthcare support yields a more informed and compassionate awareness of social and economic conditions that could impair the fairness of the application.



**Equity considerations surrounding the group targeted by the AI innovation intervention**
Each AI application that makes predictions about or classifies people targets a specific subset of the wider population to which they belong. For instance, a résumé filtering system that is used to select desirable candidates in a recruitment process will draw from a pool of job applicants that constitute a subgroup within the broader population. Potential equity issues may arise here because the selection of subpopulations sampled by AI applications is non-random. Instead, the sample selection may reflect particular social patterns, structures, and path dependencies that are unfair or discriminatory. In the case of the résumé filtering system, the sample may reflect long-term hiring patterns where a disproportionate number of male job candidates from elite universities (or those with similarly privileged educational backgrounds) have been actively recruited. Such practices have historically excluded people from other gender identities and socioeconomic and educational backgrounds. As a result, the pattern of inequity surfaces, in this instance, not within the sampled subset of the population but rather in the way that discriminatory social structures have led to the selection of a certain group of individuals into that subset.

**Equity considerations surrounding the way that the model’s output shapes the range of possible decision-outcomes** 
    AI applications that assist human decision-making shape and delimit the  range of possible outcomes for the problem areas they address. For example, a predictive risk model used in children’s social care may generate an output that directly influences the space of choices available to a social worker. Because the model’s target is the identification of at risk children, it may lead to social care decisions that focus narrowly on whether a child needs to be taken into care. This centring of negative outcomes could restrict the range of viable choices open to the social worker insofar as it de-emphasises the potential availability of other strengths-based approaches (e.g., stewarding positive family functioning through social supports and identifying and promoting protective factors). These alternative decision-making paths could be closed off in the social care environment given how the predictive risk model’s outputs restrictively shape the range of actions that can be taken to address the problem it is being used to inform.



### **2. Data fairness**

Responsible data acquisition, handling, and management is a necessary component of algorithmic fairness. If the outcomes and AI project are generated by biased, compromised, or skewed datasets, affected stakeholders will not be adequately protected from discriminatory harm. Your project team should keep in mind the following key elements of data fairness.

**1. Representativeness:** 
Depending on the context, either underrepresentation or overrepresentation of disadvantaged or legally protected groups in the data sample may lead to the systematic disadvantaging of vulnerable or marginalised stakeholders in the outcomes of the trained model. To avoid such kinds of sampling bias, domain expertise will be crucial to assess the fit between the data collected or procured and the underlying population to be modelled. Technical team members should, if possible, offer means of remediation to correct for representational flaws in the sampling.

**2. Sufficiency:**
An important question to consider in the data collection and procurement process is: Will the amount of data collected be sufficient for the intended purpose of the project? The quantity of data collected or procured has a significant impact on the accuracy and reasonableness of the outputs of a trained model. A data sample not large enough to represent with sufficient richness the significant or qualifying attributes of the members of a population to be classified may lead to unfair outcomes. Insufficient datasets may not equitably reflect the qualities that should rationally be weighed in producing a justified outcome that is consistent with the desired purpose of the AI system. 

**3. Source integrity and measurement accuracy:**
Effective bias mitigation begins at the very commencement of data extraction and collection processes. Both the sources and instruments of measurement may introduce discriminatory factors into a dataset. When incorporated as inputs in the training data, biased prior human decisions and judgments—such as prejudiced scoring, ranking, interview-data or evaluation—will become the ‘ground truth’ of the model and replicate the bias in the outputs of the system. In order to secure discriminatory non-harm, you must do your best to make sure your data sample has optimal source integrity. This involves securing or confirming that the data gathering processes involved suitable, reliable, and impartial sources of measurement and sound methods of collection.

**4. Timeliness and recency:**
If your datasets include outdated data then changes in the underlying data distribution may adversely affect the generalisability of your trained model. Provided these distributional drifts reflect changing social relationship or group dynamics, this loss of accuracy with regard to the actual characteristics of the underlying population may introduce bias into your AI system. In preventing discriminatory outcomes, you should scrutinise the timeliness and recency of all elements of the data that constitute your datasets.

**5. Relevance, appropriateness, and domain:**
The understanding and utilisation of the most appropriate sources and types of data are crucial for building a robust and bias-mitigating AI system. Solid domain knowledge of the underlying population distribution and of the predictive or classificatory goal of the project is instrumental for choosing optimally relevant measurement inputs that contribute to the reasonable determination of the defined solution. You should make sure that domain experts collaborate closely with your technical team to assist in the determination of the optimally appropriate categories and sources of measurement.

### **3. Design fairness**
#### Design phase
#### Development phase
#### Deployment phase

### **4. Metric-based fairness**
As part of the safeguarding of discriminatory non-harm and diligent fairness and equity considerations, well-informed consideration must be put into how you are going to define and measure the formal metrics of fairness that can be operationalised into the AI system you are developing. 

Metric-based fairness involves the mathematical mechanisms that can be incorporated into an AI model to allocate the distribution of outcomes and error rates for relevant subpopulations (e.g., groups with protected or sensitive characteristics). In formulating your approach to metric-based fairness, your project team will be confronting challenging issues like the justifiability of differential treatment based on sensitive or protected attributes, where differential treatment can indicate differences in the distribution of model outputs or the distribution of error rates and performance indicators like precision or sensitivity.

There is a great diversity of beliefs in this area as to what makes the consequences of an  algorithmically supported decision allocatively equitable, fair, and just. Different approaches to metric-based fairness—detailed below—stress different principles: some focus on demographic parity, some on individual fairness, others on error rates equitably distributed across subpopulations.


Your determination of metric-based fairness should heavily depend both on the specific use case being considered and the technical feasibility of incorporating your chosen criteria into the construction of the AI system. (Note that different fairness-aware methods involve different types of technical interventions at the pre-processing, modelling, or post-processing stages of production). Again, this means that determining your fairness definition should be a cooperative and multidisciplinary effort across the project team.


Fairness types can fall under two big categories: individual and group fairness metrics. The former focuses on cases where context-specific issues of effective bias are considered and assessed at the level of the individual agent, while the latter refer to metrics which define fairness in terms of some form of equal treatments of different groups.


However one defines fairness though, we must remember that these technical approaches have limited scope in terms of the bigger picture issues of application and design fairness that we have already stressed. Moreover, metric-based approaches face other practical and technical barriers. For instance, to carry out group comparisons, formal approaches to fairness require access to data about sensitive/protected attributes as well as accurate demographic information about the underlying population distribution (both of which may often be unavailable or unreliable, and furthermore, the work of identifying sensitive/protected attributes may pose additional risks of bias). Metric-based approaches also face challenges in the way they handle combinations of protected or sensitive characteristics that may amplify discriminatory treatment. These have been referred to as intersectional attributes (e.g. the combination gender and race characteristics), and they must also be integrated into fairness and equity considerations. Lastly, there are unavoidable trade-offs and inconsistencies between mathematical definitions of metric-based fairness that must be weighed in determining which of them are best fit for your use case.

### **5. Implementation fairness:**

When your project team is approaching the beta stage, you should begin to build out your plan for implementation training and support. This plan should include adequate preparation for the responsible and unbiased deployment of the AI system by its on-the-ground users. Automated decision-support systems present novel risks of bias and misapplication at the point of delivery, so special attention should be paid to preventing harmful or discriminatory outcomes at this critical juncture of the AI project lifecycle. In order to design an optimal regime of implementer training and support, you should pay special attention to the unique pitfalls of bias-in-use to which the deployment of AI technologies give rise. These can be loosely classified as decision-automation bias (more commonly just ‘automation bias’) and automation-distrust bias:

**Decision-automation bias (over-reliance):**
Users of automated decision-support systems may tend to become hampered in their critical judgment, rational agency, and situational awareness as a result of their faith in the perceived objectivity,  neutrality, certainty, or superiority of the AI system. This may lead to over-reliance or errors of omission, where implementers lose the capacity to identify and respond to the faults, errors, or deficiencies, which might arise over the course of the use of an automated system, because they become complacent and overly deferent to its directions and cues.

**Decision-automation bias (over-compliance):**
Decision-automation bias may also lead to over-compliance or errors of commission where implementers defer to the perceived infallibility of the system and thereby become unable to detect problems emerging from its use for reason of a failure to hold the results against available information. Both over-reliance and over-compliance may lead to what is known as out-of-loop syndrome where the degradation of the role of human reason and the de-skilling of critical thinking hampers the user’s ability to complete the tasks that have been automated. This condition may bring about a loss of the ability to respond to system failure and may lead both to safety hazards and to dangers of discriminatory harm. To combat risks of decision-automation bias, you should operationalise strong regimes of accountability at the site of user deployment to steer human decision-agents to act on the basis of good reasons, solid inferences, and critical judgment.

**Automation-distrust bias:**
At the other extreme, users of an automated decision-support system may tend to disregard its salient contributions to evidence-based reasoning either as a result of their distrust or scepticism about AI technologies in general or as a result of their overprioritisation of the importance of prudence, common sense, and human expertise. An aversion to the non-human and amoral character of automated systems may also influence decision subjects’ hesitation to consult these technologies in high impact contexts such as healthcare, transportation, and law.

### Putting implementation fairness intro practice

To secure and safeguard fair implementation of AI systems by users well-trained to utilise the algorithmic outputs as tools for making evidence-based judgements, you should consider the following measures:

1. Training of implementers should include  the conveyance of basic knowledge about the statistical and probabilistic character of machine learning and about the limitations of AI and automated decision-support technologies. This training should avoid any anthropomorphic (or human-like) portrayals of AI systems and should encourage users to view the benefits and risks of deploying these systems in terms of their role in assisting human judgment rather than replacing it.

2. Forethought should be given in the design of the user-system interface about human factors and about possibilities for implementation biases. The systems should be designed into processes that encourage active user judgment and situational awareness. The interface between the user and the system should be designed to make clear and accessible to the user the system’s rationale, in a ‘runtime’ manner. compliance to fairness standards, and confidence level in a ‘runtime’ manner.

3. Training of implementers should include a pre-emptive exploration of the cognitive and judgmental biases that may occur across deployment contexts. This should be done in a use case-based manner that highlights the particular misjudgements that may occur when people weigh statistical evidence. Examples of the latter may include overconfidence in prediction based on the historical consistency of data, illusions that any clustering of data points necessarily indicates significant insights, and discounting of societal patterns that exist beyond the statistical results.
