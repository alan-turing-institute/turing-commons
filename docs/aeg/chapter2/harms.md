# AI Harms

## 1. Loss of autonomy, interpersonal connection, and empathy

Automated AI systems with the power to make decisions for us can have potentially dehumanising consequences for people subject to them.  Obviously, not all automated decisions are created equal. It is one thing if an automated system decides whether an email should count as spam or not, and quite another if an AI is in charge of allocating scarse social services, or deciding who gets hired for a job. 

Individuals may feel disempowered in the face of unstoppable automation, especially when these decisions are relevant to their sense of personal autonomy. This feeling can be compounded as well if there are little or no avenues in place to dispute or contest the automated decision.

People may also feel like they are being merely "reduced to a statistic" by these systems, or that the use of their personal data violated their privacy.

Finally, but no less importantly, automation may also result in loss of empathy and crucial human connection. 

!!! example "1"
    Example 1

## 2. Poor qualities and dangerous outcomes

Inaccuracies, measurement errors, and sampling biases across data collection and recording can taint datasets. Using poor quality data could have grave consequences for individual wellbeing, and public welfare.

!!! example "2"
    Example 2

## 3. Bias, injustice, and discrimination

Supervised machine learning models draw insights (learn) from the existing data patterns on which they are trained. When they are working reliably, thet make accurate, out-of-sample predictions from what they inferred from the training data - regardless of whether these patterns are inequitable, biased, or discriminatory. 

However, this is very often not the case. Most (if not all) machine learning models are trained on historial data, and this means that as long as they do, they will be embedded with past and present injustices, forms of discrimination, and multiple biases which the data itself contains.
Not only that, the machine learning algorithms will reproduce, and even amplify said biases.

In day 4 we will look at the various different biases which can creep up in the ML/AI lifecycle. One crucial thing to keep in mind though, is that there is no fairness without awareness. When designing, implementing, and using these systems, conscious awareness of biases and explicit mitigation strategies must be discussed and implemented.

!!! example "3"
    - Healthcare models
    - Recidivism predictors
    - Hiring algorithms


## 4. Widening global digital divides
The use of AI systems is not distributed uniformally across different countries, or even within regions in the same country. The varying levels of access and use of these technologies can reinforce and amplify already existing digital divides and data inequities. It can also exacerbate exploitative data appropriation from less rich countries and institutions to more well-resourced researchers and companies in richer countries or in better-funded universities within one country. 

Long-standing dynamics of global inequality, for instance, may undermine reciprocal sharing between research collaborators from high-income countries (HICs) and those from low-/middle-income countries (LMICs).[@leslie2020] Given asymmetries in resources, infrastructure, and research capabilities, data sharing between LMICs and HICs, and transnational research collaboration, can lead to inequity and exploitation (Bezuidenhout et al., 2017; Leonelli, 2013; Shrum, 2005). That is, data originators from LMICs may put immense amounts of effort and time into developing useful datasets (and openly share them) only to have their countries excluded from the benefits derived by researchers from HICs who have capitalized on such data in virtue of greater access to digital resources and compute infrastructure (Goldacre et al., 2015). 

<!-- Moreover, data originators from LMICs may generate valuable datasets that they are then unable to independently and expeditiously utilize for needed research, because they lack the aptitudes possessed by researchers from HICs who are the beneficiaries of arbitrary asymmetries in education, training, and research capacitation (Bull et al., 2015; Merson et al., 2015). -->

This can create a two-fold architecture of research inequity wherein the benefits of data production and sharing do not accrue to originating researchers and research subjects, and the scientists from LMICs are put in a position of relative disadvantage vis-à-vis those from HICs whose research efficacy and ability to more rapidly convert data into insights function, in fact, to undermine the efforts of their disadvantaged research partners (Bezuidenhout et al., 2017; Crane, 2011). It is important to note, here, that such gaps in research resources and capabilities also exist within HICs where large research universities and technology corporations (as opposed to less well-resourced universities and companies) are well positioned to advance data research given their access to data and compute infrastructures (Ahmed & Wahed, 2020). 

<!-- In redressing these access barriers, emphasis must be placed on “the social and material conditions under which data can be made useable, and the multiplicity of conversion factors required for researchers to engage with data” (Bezuidenhout et al., 2017, p. 473). Equalizing know-how and capability is a vital counterpart to equalizing access to resources, and both together are necessary preconditions of just research environments. CSS scholars engaging in international research collaborations should focus on forming substantively reciprocal partnerships where capacity-building and asymmetry-aware practices of cooperative innovation enable participatory parity and thus greater research access and equity. -->


!!! example "4"
    Example 4

## 5. Data integrity, privacy, and security

The ways we measure, collect, use, and store data points can lead to a multplicity of harms to individuals but also in wider society. There can be issues with data points being appropriately and fairly measured as well as with acquiring data sets with informed consent from the data subjects. Once the data is collected, harms may arise in terms of how the data is used. In this sense the notion of contextual privacy (Nissembaum, XXXX) can be very enlighting. The idea is that a data point (or a piece of information more generally) is not public or private per se, but instead in depends on the context and for the purpose it is being used. For example, one may consent to a fitness tracker collecting one's data for personal purposes, but they have not necessarily have consented to the company using the data in other ways (for example, sell it to health insurance companies). Additionally, many potential harms can occur in the way information is stored in the medium and long run where security considerations are not always at the forefront of data managers.


!!! example "5"
    Data leaks
    Case where data is used for reasons different than those collected

## 6. Biospheric harms


The explosion of computing power (which has partly driven the “big data revolution”) has had significant environmental cost. As algorithmic models become more intesive in data and computation, they also require higher levels of energy consumption. 

Many of these models ingest abundant amounts of data for training. These increase in model size and complexity does not necessarily lead to an equally large increase in model accuracy; in many cases only the gains in accuracy are only modest. The amount of compute needed to train complex models has increased 300,000 times from 2013 to 2019, with training expenditures of energy doubling every six months. These means that a lot of costly resources are used, even when the benefits of improvements in the model are small at best. Additionally, the costs of these resources are burdened upon everyone on the planet (in the form of negative externalities), while the modest gain in model performace is most likely accrued to the propietary owner(s) of the model.

These models contribute to emissions which are partly responsible of biospheric harm and climate change. Additionally, the benefits and risks of the use of data-intensive models is not uniformly distributed among the population or among the world’s regions.
If anything, the allocations of benefit and risk have closely tracked the existing patterns of environmental racism, coloniality, and “slow violence” (Nixon, 2011 (CITE)) that have typified the disproportionate exposure of marginalised communities (especially those who inhabit what has conventionally been referred to as “the Global South”) to the pollution and destruction of local ecosystems and to involuntary displacement.

!!! example "6"
    -  Training Google’s large language model BERT produces emissions equivalent to around 1 transatlantic flight[@strubell2019]. 