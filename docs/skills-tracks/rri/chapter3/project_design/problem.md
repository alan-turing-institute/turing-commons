# Problem Formulation

In the previous section we acknowledge that it is important to clearly define and delineate the problem that your project is intended to address.
Here, ‘problem’ is used in two interrelated ways:

1. To refer to a *well-defined computational process* (or a higher-level abstraction of the process) that is carried out by the algorithm to map inputs to outputs.
2. To refer to the wider practical, social, or policy issue that will be addressed through the translation of that issue into the aforementioned mathematical or computational framing.

On the computational side, we can think of how a convolutional neural network carries out a series of successive transformations by taking (as input) an image, encoded as an array, in order to produce (as output) a decision about whether some object is present in the image.
On the practical, social, and policy side, there will be a need to define the computational ''problem'' being solved in terms of the algorithmic system’s embeddedness in the social environment and to explain how it contributes to (or affects) the wider sociotechnical issue being considered. In the convolutional neural network example, the system being produced may be a facial recognition technology that responds to a perceived need for the biometric identification of criminal suspects by matching facial images in a police database. The social issue of wanting to identify suspects is, in this case, translated into the computational mechanism of the computer vision system. But, beyond this, diligent consideration of the practical, social, or policy issue being addressed by the system will also trigger, *inter alia*, reflection on the complex intersection of potential algorithmic bias, the cascading effects of socio-historical patterns of racism and discrimination, wider societal and community impacts, and the potential effects of the use of the model on the actors in the criminal justice systems who will become implementers and subjects of the technology.

Sociotechnical considerations are also important for determining and evaluating the choice of target variables used by the algorithm, which may ultimately be implemented within a larger automated decision-making system (e.g. in a risk prediction system).
The task of formulating the problem allows the project team to get clear on what input data will be needed, for what purpose, and whether there exists any representational issues in, for example, how the target variables are defined.
It also allows for a project team (and impacted stakeholders) to reflect on the reasonableness of the measurable proxy that is used as a mathematical expression of the target variable, for instance, whether moving a patient into an intensive care unit (ICU) is a reasonable action to take after being classified as ''at risk'' by a model that uses a set of demographic and physiological input variables.

The fact that formulating problems and defining target variables in ML/AI innovation lifecycles can often be a biased and contested process is why stakeholder engagement, which helps bring a diversity of perspectives to project design, is so vital.
It is also why this stage is so closely connected with the interpretive burdens of the project planning activities seen in the previous section (e.g. discussion about legal and ethical concerns regarding permissible uses of personal or sensitive information).