# Responsible Data Science and AI

!!! quote

    What separates responsible data science and AI from responsible research and innovation more generally?

We saw in the [previous chapter](../chapter1/index.md) how RRI can be defined with reference to concepts that emphasise the need for ethical reflection on possible social harms and benefits, supported by inclusive participation of affected stakeholders.
Responsible data science and AI shares this emphasis, but can be further refined by considering more specific principles that are geared towards the particular harms and benefits associated with data science and AI.
These principles can help us identify what is unique to responsible data science and AI.

## SAFE-D Principles

According to Mittelstadt[@mittelstadt2019], in 2019 there were at least 84 statements that provided ''high-level principles, values and other tenets to guide the ethical development, deployment and governance of AI''.
By now there are surely many, many more!

In response to this proliferation of principles, some have attempted to distil and condense the myriad documents, in order to identify commonalities and extract a unified list of shared principles.[@jobin2019]<sup>-</sup>[@floridi2019]
However, regardless of which set of principles we start with, one thing remains the same: good principles should support ongoing reflection and deliberation; they are not decision procedures in their own right.

![An illustration of a man standing in front of a branching pathway of moral decisions and considerations](https://raw.githubusercontent.com/alan-turing-institute/turing-commons/main/docs/assets/images/illustrations/deliberation.png){ align="center" }

This point is sometimes lost in the ensuing debate about *which set* of principles should be used or adhered to, or which set is best.
However, what matters is that the set of principles should a) be responsive to the actual harms and benefits that matter to the communities of affected individuals, b) be underwritten by a set of shared values, which support and motivate dialogue between stakeholders[^values], and c) serve as *starting points* in a wider process of reflection and deliberation.

[^values]: We won't say much about ethical values in this course. However, the course on [AI Ethics & Governance](../../aeg/index.md) focuses on them directly.

With these points in mind, we will make use of the following set of principles known as the 'SAFE-D principles':

- Sustainability
- Accountability
- Fairness
- Explainability
- Data Quality, Integrity, Protection and Privacy

These principles are grounded in comprehensive research and understanding of human rights and data protection law, as well as applied ethics of data and AI.[@leslie2021a]

You can click through the following illustrative examples to get an idea of some of the social harms associated with data-driven technologies:

=== "Predicting Risk"

    Avon and Somerset Police and Bristol City Council developed a sophisticated predictive risk tool that was used, among other things, to predict the risk of children suffering sexual abuse. But, the Bristol Cable reported that many children were falsely flagged as being at risk, and that the tool was developed using dozens of public sector databases, including schools, housing, NHS records, and even credit scores from Experian.
    
    [The Bristol Cable, 'How a police and council database is predicting if your child is at risk of harm'](https://thebristolcable.org/2021/07/how-a-police-and-council-database-is-predicting-if-your-child-is-at-risk-of-harm/)

=== "Facebook Discriminatory Job Adverts"

    The algorithmic system used by Facebook to automatically show job adverts to users it believes are most likely to engage with them was reported to perpetuate discriminatory gender norms. Thee BBC reported that
    
    !!! quote 
    
        almost all Facebook users shown adverts for mechanics were men, while ads for nursery nurses were seen almost exclusively by women.
        
    [BBC News, 'Facebook accused of allowing sexist job advertising'](https://www.bbc.co.uk/news/technology-58487026)

=== "Racist Photo Cropping Tool"

    Twitter was forced to apologise after many users reported that the automated tool for cropping images on the social media platform showed a racial bias towards faces of white people over faces of black people. According to [Twitter](https://blog.twitter.com/engineering/en_us/topics/insights/2021/sharing-learnings-about-our-image-cropping-algorithm), one source of the issue was the use of a ''saliency algorithm'' that was trained on human eye-tracking data.
    
    [The Guardian, 'Twitter apologises for 'racist' image-cropping algorithm'](https://www.theguardian.com/technology/2020/sep/21/twitter-apologises-for-racist-image-cropping-algorithm)

=== "Lethal Autonomous Weapons"

    Turkish company STM manufactures the [Kargu-2](https://www.stm.com.tr/uploads/docs/1628858259_tacticalminiuavsystems.pdf?)—an attack drone that can operate autonomously by using machine learning and real-time image processing to identify targets. According to a UN security council report this drone was reported to have been used to "remotely engage" and "hunt down" logistics convoys and retreating forces in the Libyan civil war during 2019.
    
    [NPR, 'A Military Drone With A Mind Of Its Own Was Used In Combat, U.N. Says'](https://www.npr.org/2021/06/01/1002196245/a-u-n-report-suggests-libya-saw-the-first-battlefield-killing-by-an-autonomous-d)

=== "#TravelingWhileTrans"

    In their book, Design Justice, Sasha Costanza-Chock highlights how the design of sociotechnical systems reinforce and embed a variety of social norms and expectations that can be harmful to vulnerable or marginalised communities. For example, the impact of full-body scanners at airport security that require operators to select either 'male' or 'female', even when presented with non-binary or trans individuals whose bodies may not conform to the models embedded within the machine.
    
    [Design Justice, 'Introduction: #TravelingWhileTrans, Design Justice, and Escape from the Matrix of Domination'](https://design-justice.pubpub.org/pub/ap8rgw5e/release/1)

=== "Any Others?"

    Do you know any other examples of social harms associated with data-driven technologies?

Each of the SAFE-D principles is either motivated by and captures a specific set of harms that have been uncovered and exposed, responds to a set or well-documented risks that arise in the context of data science and AI, or is oriented towards the sustainable, ethical, and responsible use of data-driven technologies.
Let's look at each principle in turn.

### Sustainability

Sustainability can mean a couple of things.
From a technical perspective, sustainability requires the outputs of a project to be safe, secure, robust, and reliable.
For example, if an organisation is developing an autonomous vehicle, it should operate safely in the intended context of use.
However, in the context of responsible data science and AI, there is also a social sustainability component.
This aspect of sustainability requires a project's practices to be informed by ongoing consideration of the risk of exposing individuals to harms even after the system has been deployed and the project completed—a long-term (or sustainable) safety.

### Accountability

Accountability can refer to transparency of processes and associated outcomes that enable people to understand how a project was conducted (e.g., project documentation), or why a specific decision was reached.
But it can also refer to broader processes of responsible project governance that seek to establish clear roles of responsibility where full transparency may be inappropriate (e.g., confidential projects).

### Fairness

Fairness is inseparably connected with legal conceptions of equality and justice, which may emphasize a variety of features such as non-discrimination, equitable outcomes, or procedural fairness through bias mitigation.
However, these notions serve as a subset of broader normative considerations pertaining to social justice, socioeconomic capabilities, diversity and inclusivity.
For this reason, the term 'fairness' can be confusing due to the wide variety of ways it is employed, and the large number of more specific concepts that fall within its scope.

### Explainability

Explainability is a key condition for autonomous and informed decision-making in situations where data-driven systems interact with or influence human judgement and choice behaviour.
Explainability goes beyond the ability to merely interpret specific aspects of a project (e.g., interpreting the parameters of a model); it also depends on the ability to provide an accessible and relevant information base about the processes behind the outcome.

### Data Quality, Integrity, Protection and Privacy

Data quality, integrity, protection and privacy must all be established to be confident that a research or innovation project has been designed, developed, and deployed in a responsible manner.

- 'Data Quality' captures the static properties of data, such as whether they are a) *relevant* to and *representative* of the domain and use context, b) *balanced* and *complete* in terms of how well the dataset represents the underlying data generating process, and c) *up-to-date* and *accurate* as required by the project.
- ‘Data Integrity' refers to more dynamic properties of data stewardship, such as how a dataset evolves over the course of a project lifecycle. In this manner, data integrity requires a) *contemporaneous* and *attributable* records from the start of a project (e.g., process logs; research statements), b) ensuring *consistent* and *verifiable* means of data analysis or processing during development, and c) taking steps to establish *findable*, *accessible*, *interoperable*, and *reusable* records towards the end of a project’s lifecycle.[^FAIR]
- ‘Data protection and privacy' reflect ongoing developments and priorities as set out in relevant legislation and regulation of data practices as they pertain to fundamental rights and freedoms, democracy, and the rule of law. For example, the right for data subjects to have inaccurate personal data rectified or erased.[@ico2021]

[^FAIR]: These are known as the FAIR principles ([read more here](https://www.go-fair.org/fair-principles/)).

Each of these principles can be treated as a goal to which responsible data science and AI ought to be directed.[^ped]
But, on their own they are insufficient for establishing what specific actions or decisions should be taken in any given project.
For instance, what does it mean to develop a *fair* diagnostic model in healthcare?

Does it mean ensuring that all patients are exposed to the same level of risk with respect to the distribution of possible false negatives?

What about false positives instead?

What about the use of the decision support system in which thee model is implemented?

Will it be used in all hospitals on all patients?

Or, will only those wealthy enough to afford private healthcare receive this service?

Should it instead be used for the most vulnerable and worse off in society?

[^ped]: In our guidebook on [public engagement of data science and AI](../../ped/index.md) we formalise this notion of an ethical goal in relation to a method known as argument-based assurance. Here, the goals are supported by specific properties that must be established in a project, in order to provide justifiable assurance to stakeholders that the respective goal has been realised.

Questions such as these have no straightforward answer and are heavily context-dependant.
Even if consensus were to be reached for a specific model used, say, in the diagnosis of lung cancer,[@svoboda2020] this would be no guarantee of a similar answer in a different area of healthcare (e.g., paediatrics, mental healthcare), or even for another diagnostic model in radiology (e.g., MRI instead of CT scans).
Therefore, starting in the next section we will look at a model for helping us get a clear grasp of the situated and sociotechnical context under consideration in research and innovation projects.
