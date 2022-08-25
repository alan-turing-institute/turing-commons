# Governance and Accountability

## Introduction to Accountability

The principle of accountability is an end-to-end governing principle. 

What does accountability mean? It means that **humans are answerable** for the parts they play across the entire AI design, development, and deployment. It
also demands that the results of this work are **traceable** from start to finish.

According to the principle of fairness, designers and implementers are held accountable for being equitable and for not harming anyone through bias or discrimination. According to the principle of sustainability, designers and implementers are held accountable for producing AI innovation that is safe and ethical in its outcomes and wider impacts. And according to the principle of explainability, designers and implementers are held accountable for making sure that any decision the AI system makes, or provides support for humans to make, can be adequately explained to relevant stakeholders.

When considering the role of accountability in the AI project delivery lifecycle, it is important first to make sure that you are taking a ‘best practices’ approach to data processing that is aligned with the Data Ethics Framework. 

However, responsible AI project delivery requires confronting two relevant challenges to accountability.

!!!! danger "Accountability gap"

    Automated decisions are not self-justifiable. Whereas human agents can be called to account for their judgements and decisions in instances where those judgments and decisions affect the interests of others, the statistical models and underlying hardware that compose AI systems are not responsible in the same morally relevant sense. This creates an accountability gap that must be addressed so that clear and imputable sources of human answerability can be attached to decisions assisted or produced by an AI system.
    
!!! danger "Complexity of AI production processes"

    Establishing human answerability is not a simple matter when it comes to the design, development, and deployment of AI systems. This is due to the complexity and multi-agent character of the production and use of these systems. Typically, AI project delivery workflows include department and delivery leads, technical experts, data procurement and preparation personnel, policy and domain experts, implementers, and others. Due to this production complexity, it may become difficult to answer the question of who among these parties involved in the production of AI systems should bear responsibility if these systems’ uses have negative consequences and impacts.
    
Meeting the special requirements of accountability, which are born out of these two challenges, calls for a sufficiently fine-grained concept of what would make an AI project properly accountable. This concept can be broken down into two subcomponents of accountability, answerability and auditability:

!!! success "Answerability"

    The principle of accountability demands that the onus of justifying algorithmically supported decisions be placed on the shoulders of the human creators and users of those AI systems. This means that it is essential to establish a continuous chain of human responsibility across the whole AI project delivery workflow. Making sure that accountability is effective from end to end necessitates that no gaps be permitted in the answerability of responsible human authorities from first steps of the design of an AI system to its algorithmically steered outcomes.
    
    Answerability also demands that explanations and justifications of both the rationale underlying the results of an AI system and the processes behind their production and use be offered by competent human authorities in plain, understandable, and coherent language. These explanations and justifications should be based upon sincere, consistent, sound, and impartial reasons that are accessible to non-technical hearers.

!!! success "Auditability"
    
    Whereas the notion of answerability responds to the question of who is accountable for an automation supported outcome, the notion of auditability answers the question of how the designers and implementers of AI systems are to be held accountable. This aspect of accountability has to do with demonstrating both the responsibility of design, development, and deployment practices and the justifiability of outcomes.
    
    Auditability also has to do with traceability; It refers to the process by which all stages of the AI innovation lifecycle from data collection and model selection to system deployment, updating, and deprovisioning are documented in a way that is accessible and easily understood.
    
    The project team must ensure that every step of the process of designing and implementing an AI project is accessible for audit, oversight, and review by appropriate parties. Successful auditability requires builders and implementers of algorithmic systems
to:
    • keep records and to make available information that enables monitoring of the soundness and diligence of the innovation processes that produced these systems
    • keep track of the accountable parties within an organisation’s project team and others involved in the supply chain (where system components are procured)
    • keep track of the governance actions taken across the entire AI innovation workflow
    • keep records and make accessible information that enables monitoring of data provenance and analysis from the stages of collection, pre-processing, and modelling to training, testing, and deploying. This is the purpose of the Dataset Factsheet.


Moreover, auditability requires the team to enable peers and overseers to probe and to critically review the dynamic operation of the system in order to ensure that the procedures and operations which are producing the model’s behaviour are safe, ethical, and fair. Practically transparent algorithmic models must be built for auditability, reproducible, and equipped for end-to-end recording and monitoring of their data processing.The deliberate incorporation of both of these elements of accountability (answerability and auditability) into the AI project lifecycle may be called accountability-by-design.

!!! success "Key Concept: Accountability-by-design"

    AI systems must be designed to facilitate end-to-end answerability and auditability. This requires both responsible humans-in-the-loop across the entire design and implementation chain as well as activity monitoring protocols that enable end-to-end oversight and review.
    
 
## Types of Accountability 

Accountability deserves consideration across the entire design and implementation workflow. As a best practice, the team should actively consider the different demands that accountability-by-design requires before and after the roll out of the AI project. We will refer to the process of ensuring accountability during the design and development stages of the AI project as ‘anticipatory accountability’. This is because the team is anticipating the project’s accountability needs prior to it being completed.

Following a similar logic, we will refer to the process of addressing accountability after the start of the deployment of your AI project as ‘remedial accountability’. This is because after the initial implementation of a system, the team is remedying any of the issues that may be raised by its effects and potential externalities. These two subtypes of accountability are sometimes referred to as ex-ante (or before-the-event) accountability and ex-post (after-the-event) accountability respectively.

### Anticipatory Accountability
Treating accountability as an anticipatory principle entails that the project team takes as of primary importance the decisions made and actions taken by them prior to the outcome of an algorithmically supported decision process. This kind of ex ante accountability should be prioritised over remedial accountability, which focuses instead on the corrective or justificatory measures that can be taken after that automation supported process had been completed.

Ensuring that the AI project delivery processes are accountable prior to the actual application of the system in the world will bolster the soundness of design and implementation processes and thereby more effectively pre-empt possible harms to individual wellbeing and public welfare or other adverse impacts.

Likewise, by establishing strong regimes of anticipatory accountability and by making the design and delivery process as open and publicly accessible as possible, the project team will put affected stakeholders in a position to make better informed and more knowledgeable decisions about their involvement with these systems in advance of potentially harmful impacts. Doing so will also strengthen the public narrative and help to safeguard
the project from reputational harm.

!!! example
    
    During the preprocessing phase of an AI production lifecycle, technical members of a project team are deciding which features to include, and which to leave out. To safeguard sufficient anticipatory accountability, they make sure to log which team members are involved in making these decisions and record the rationale behind the choices made.

### Remedial Accountability
