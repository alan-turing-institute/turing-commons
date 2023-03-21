# User Training

Consider the following scenario:

!!! example "Security System"

    You are in charge of deploying an automated facial recognition system that is used to verify that people who are attempting to enter a secure building are using the appropriate identity card.
    Upon swiping their identity card, the system scans the face of the user and matches it to the expected image from a database of authorised people.
    If the person matches their card and is also allowed access to the building, they are automatically granted access.
    
    After a week or so of deploying the system, you find out that the security guard in charge of the building has been overriding the system.
    You go to speak with the security guard, and he claims that the system has been refusing entry to people who clearly match their identity badge.
    
    When you investigate the issue, you find out that the system is functioning as expected and that no errors with the automated facial recognition system have been logged.
    However, every one of the attempts that the security guard has overridden are for people with expired identity cards.
    Although they match their cards, they should not have access to the building.

This scenario highlights an important, but sometimes overlooked part of system deployment and evaluation: **human factors**.

> Human factors is a field in which researchers and practitioners are interested in both understanding the interaction of people and technology and in making that interaction more efficient, safer, and pleasant.[@durso2014]

Research into human factors considers both perceptual, cognitive, social, and physical characteristics of the human operator, as well as how a technological system has been designed. This is important, because if there is an issue, such as the one in our above scenario, the *sociotechnical system* can be improved by changing either a) the human or b) the technology.

For instance, in our scenario, you could provide training for the security guard that shows him how to identify the cause of an automated rejection. Or, you could design a simple prompt or notification that explains why an individual is being denied entry to avoid the possibility of the security guard overriding the system unless there is a legitimate false negative (i.e. an error with the facial recognition system for a valid identity card and matched person).

There is a huge amount of quantitative and qualitative research related to human factors in general (see Durso, 2014[@durso2014]), and a growing source of research for human interaction with algorithmic systems more specifically.

For present purposes, it is sufficient to note that although the performance of a model is evaluated in earlier stages, the model's **impact** cannot be fully evaluated without consideration of the human factors that affect its performance in real-world settings.
For instance, the impact of human cognitive biases, such as *algorithmic aversion* must also be considered, as these biases can lead to over- and under-reliance on the model (or system), in turn negating any potential benefits that may arise from its use.
Understanding the social and environmental context is also vital, as sociocultural norms may contribute to how training is received, and how the system itself is evaluated (see {Burton, 2020[@burton2020]).

In the context of RRI, user training related to how an algorithmic system should be operated may include: a) conveying basic knowledge about the nature of machine learning (e.g. probabilistic results or outcomes), b) explaining the limitations of the system, c) educating users about the risks of AI-related biases, such as decision-automation bias or automation-distrust bias, and d) encouraging users to view the benefits and risks of deploying these systems in terms of their role in helping humans to come to judgements, rather than replacing that judgement.
