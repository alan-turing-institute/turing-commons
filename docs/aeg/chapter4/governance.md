# Governance and Accountability

## Introduction to accountability

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
    
 
## Types of accountability 

Accountability deserves consideration across the entire design and implementation workflow. As a best practice, the team should actively consider the different demands that accountability-by-design requires before and after the roll out of the AI project. We will refer to the process of ensuring accountability during the design and development stages of the AI project as ‘anticipatory accountability’. This is because the team is anticipating the project’s accountability needs prior to it being completed.

Following a similar logic, we will refer to the process of addressing accountability after the start of the deployment of your AI project as ‘remedial accountability’. This is because after the initial implementation of a system, the team is remedying any of the issues that may be raised by its effects and potential externalities. These two subtypes of accountability are sometimes referred to as ex-ante (or before-the-event) accountability and ex-post (after-the-event) accountability respectively.

### Anticipatory accountability
Treating accountability as an anticipatory principle entails that the project team takes as of primary importance the decisions made and actions taken by them prior to the outcome of an algorithmically supported decision process. This kind of ex ante accountability should be prioritised over remedial accountability, which focuses instead on the corrective or justificatory measures that can be taken after that automation supported process had been completed.

Ensuring that the AI project delivery processes are accountable prior to the actual application of the system in the world will bolster the soundness of design and implementation processes and thereby more effectively pre-empt possible harms to individual wellbeing and public welfare or other adverse impacts.

Likewise, by establishing strong regimes of anticipatory accountability and by making the design and delivery process as open and publicly accessible as possible, the project team will put affected stakeholders in a position to make better informed and more knowledgeable decisions about their involvement with these systems in advance of potentially harmful impacts. Doing so will also strengthen the public narrative and help to safeguard
the project from reputational harm.

!!! example
    
    During the preprocessing phase of an AI production lifecycle, technical members of a project team are deciding which features to include, and which to leave out. To safeguard sufficient anticipatory accountability, they make sure to log which team members are involved in making these decisions and record the rationale behind the choices made.

### Remedial Accountability

While remedial accountability should be seen, along these lines, as a necessary fallback rather than as a first resort for imputing responsibility in the design, development and deployment of AI systems, strong regimes of remedial accountability are no less important in providing necessary justifications for the bearing these systems have on the lives of affected stakeholders.

Putting in place comprehensive auditability regimes as part of your accountability framework and establishing transparent design and use practices, which are methodically logged throughout the AI project delivery lifecycle, are essential components for this sort of remedial accountability.

One aspect of remedial accountability that you must pay close attention to is the need to provide explanations to affected stakeholders for algorithmically supported decisions.

Offering explanations for the results of algorithmically supported decision-making involves furnishing decision subjects and other interested parties with an understandable account of the rationale behind the specific outcome of interest. It also involves furnishing the decision subject and other interested parties with an explanation of the ethical permissibility, the fairness, and the safety of the use of the AI system.

!!! example

    After receiving an unfavourable decision in their recruitment process, a job applicant seeks assurance and justification that the resume filtering AI system used in their process was not biased or discriminatory. To safeguard sufficient remedial accountability, the implementers of the system draw on the logged records of bias-mitigation measures and fairness-aware design practices to demonstrate the fair and non-discriminatory practices behind the production of the system. They also provide an explanation of the rationale behind the applicant’s negative result, showing that the determinative factors behind the system’s output were fair and reasonable.
    
    
## Putting accountability into practice

Now that we have explored some of the main aspects of the concept of accountability, we are ready to examine–in greater detail–how elements of answerability and auditability can be put into practice.

The central importance of the end-to-end operability of good governance practices should guide your strategy to embed accountability across the project workflow. Three components are essential to creating a such a workflow:

1. Maintaining strong regimes of professional and institutional transparency.

2. Establishing and maintaining a clear and accessible Process-Based Governance Framework (PBG Framework).

3. Establishing a well-defined auditability trail for your PBG Framework through robust activity logging protocols that are consolidated digitally in a Process Log.

### Maintaining professional and institutional transparency

At every stage of the design and implementation of your AI project, team members should be held to rigorous standards of conduct that secure and maintain professionalism and institutional transparency. These standards should include the core values of selflessness, integrity, honesty, accountability, openness, sincerity, neutrality, objectivity, impartiality, and leadership. All professionals involved in the research, development, production, and implementation of AI technologies are, first and foremost, acting as fiduciaries of the public interest and must, in keeping with these core values of the Civil Service, put the obligations to serve that interest above any other concerns. For helpful guidance on professionalism and good conduct for public office holders, see the Seven Principles of Public Life (also known as the Nolan Principles).

Furthermore, from start to finish of the AI project lifecycle, the design, development, and deployment process should be as transparent and as open to public scrutiny as possible with restrictions on accessibility to relevant information limited to the reasonable protection of justified public sector confidentiality and of analytics that may tip off bad actors to methods of gaming the system of service provision.

### Process-based governance framework

So far, this workbook series has presented some of the main values principles necessary for establishing responsible innovation practices in your AI project. Perhaps the most vital of these measures is the effective operationalisation of these practices.The recently-adopted standard, ISO 37000, defines governance as ‘the system by which the whole organisation is directed, controlled, and held accountable to achieve its core purpose in the long run’. 
Establishing a diligent and well-conceived governance framework that covers the entire design, development, and deployment process will provide the foundation for your team to effectively establish needed practical actions and controls, exhaustively distribute roles and responsibilities, and operationalise answerability and auditability throughout the AI lifecycle. By organising all of your governance actions into a PBG Framework, you will be better able to accomplish this task.

The purpose of a PBG Framework is to provide a template for the integrations of the norms, values, and principles, which motivate and steer responsible innovation, with the actual processes that characterise the AI design and development pipeline. Establishing a PBG framework creates the baseline conditions for ensuring that the goal of instituting an AI innovation process that is accountable-by-design is achieved.

A PBG Framework should give the team a landscape view of the governance actions that are organising the control structures of the project workflow. Constructing a good PBG Framework will provide the team with a big picture of:

• The relevant stages of the workflow in which actions are necessary to meet governance goals
• The relevant team members and roles involved in each governance action
• Explicit timeframes for any necessary follow-up actions, re-assessments, and continual monitoring
• Clear and well-defined protocols for logging activity and for instituting mechanisms to assure end-to-end auditability and appropriate documentation

The PBG framework asks that teams not only outline the governance actions established for individual projects, but also roles involved in each action, timeframes for follow-up actions, and logging protocols.

ADD TEMPLATE

### Establishing proportional governance actions

Just as with the determination of proportionate stakeholder involvement, the establishment of proportionate governance protocols should involve a preliminary assessment of the potential risks and hazards of the model or tool under consideration. Low-stakes AI applications that are not safety critical, do not directly impact the lives of people, and do not process potentially sensitive social and demographic data may need less proactive governance controls and processes than high-stakes projects. By completing the Project Summary Report and Stakeholder Impact Assessments, you and your project team will need to carry out evaluations of the scope of the possible risks that could arise from your project and of the potential hazards it poses to affected individuals and groups. These assessments of the dangers posed to individual wellbeing and public welfare will help you formulate proportionate governance actions to be outlined in your PBG framework.

Notwithstanding the importance of the need for this reasonable application of proportionate governance actions, you should take care to establish a strong regime of accountability-by-design across your project lifecycle. It may be the case that your assessment of potential risks and adverse impacts do not sufficiently anticipate the full range of possible harms. In instances where such unforeseen harms do arise, you will want to have in place proper mechanisms of anticipatory accountability and corresponding documentation protocols, so that the best practices of your project team are demonstrable.

ADD IMAGES

### Accountability across the workflow
The task of establishing a PBG framework for your project should be initially undertaken in the project planning step of your project alongside your Project Summary Report (Please refer to the AI Sustainability in Practice Part I Workbook for details on the full process of creating your PS Report.) The results of your Stakeholder Analysis (particularly, the scoping of potential stakeholder impacts) should inform a proportional selection of governance actions within your PBG framework. At this stage, your PBG framework will provide a prospective and provisional plotting of governance actions, roles, and responsibilities for your project. This preliminary outline of governance structures will provide the necessary information for answering the Governance Framework Reflection questions within the PS Report.

In the PS Report, the task of reflecting on your governance framework on your involves answering the following questions:

ADD IMAGES

These questions (alongside the rest of the PS Report) are to be revisited and updated as part of completing each iteration of the Stakeholder Impact Assessment, at each point informing any necessary updates to your project’s governance structure (and PBG framework). Your PBG Framework is therefore a live document reflecting a governance structure that responds to the emerging needs across the design, development, and deployment lifecycle. It is to be updated after each revisitation of the PS report to reflect the project’s current governance structure.

The process by which you answer these questions should be as collaborative and inclusive as possible. You should aim to involve all relevant members of your project team (and any other relevant managers, operators, or vendors), so that all people involved in the workflow can share input and come to understand expectations about their roles and responsibilities. Any future revisions or updates of this part of the PS Report should likewise include all affected parties.
