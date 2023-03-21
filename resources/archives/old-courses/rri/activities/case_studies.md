# Case Studies

The following case studies have been designed to work alongside a series of practical activities that cover the various stages of the project lifecycle.
They offer only *basic* information to guide reflective and deliberative activities.
If you find that you do not have sufficient information to address an issue that arises during deliberation, you should try to come up with something reasonable that fits the context of your chosen case study and then reflect on what this would mean for the project.

For example, when you reach the model selection section, you will have to consider what the benefits and risks could be for choosing a particular model over another, given the type of technology being developed.
Because the focus of this course is on normative issues associated with data science and AI, we will not be training any models, so the actual outcome of choosing one model over another will require some informed speculation and reflection.

## 1) Predicting Risk of Reoffending

!!! info "Summary"

    You are a project team responsible for developing a predictive risk assessment tool that can support sentencing decisions by judges in criminal courts. The tool will take data about a defendant and feed this into an algorithm that predicts a *risk score*, between 1 and 5 that is presented to the judge alongside additional case evidence (e.g., witness testimony). This score will represent the likelihood of reoffending, and, therefore, inform the sentencing decision made by the judge. For those that are discharged, the system will also receive feedback about whether the defendant goes on to reoffend. 

### Details

| Category | Details |
| --- | --- |
|*Type of technology:*| Decision Support Tool|
|*Context of Use:*| Sentencing Decisions in Criminal Courts|
|*Outcome:*| A Risk Score |
|*Project Team:*| Data scientists working for the courts|
|*Data Types:*| `Age`, `Gender`, `Crime Committed`, `Postcode`, `Housing Status`, `Level of education`, `Occupation`, `Past offences`, `Feedback from police and parole officers` (i.e., whether the defendant goes on to reoffend)|
|*Data Source(s):*| Criminal Court Data |

## 2) Recommending Courses

!!! info "Summary"

    You work for an EdTech company and need to develop a recommender system that will be sold to schools to augment careers advice for students considering university courses. The system will ask each student to answer a series of questions, and will then provide an ordered list of recommended courses (linked to the respective university) that it "believes" are good options for the student. The system will also use satisfaction survey results and obtained degree results from those students who used the system previously as a way of calibrating and adjusting its recommendations (i.e., learning).

| Category | Details |
| --- | --- |
|*Type of technology:*| Recommendation System|
|*Context of Use:*| Secondary Schools or Colleges|
|*Outcome:*| A ranking of possible degrees and career paths |
|*Project Team:*| Private EdTech Organisation|
|*Data Types:*| `Courses currently being studied at school`, `Current grades`, `Gender`, `Age`, `Postcode`, `Extracurricular activities`, `Interests/Hobbies` (from list of pre-selected options), `Satisfaction survey results from previous users of system`, `University grades of previous users of system`|
|*Data Source(s):*| Input by Student, Gathered from Partner Universities |

## 3) Classifying Hate Speech

!!! info "Summary"

    You are a team of social data scientists employed as consultants for a social media company. You have been tasked with reducing the levels of hate speech on the company's platform by developing a classifier that can flag potential instances of hate speech for review by human moderators. The tool will automatically review every post submitted to the platform, but will only flag those that are likely to represent an instance of hate speech, based on whether they exceed some likelihood threshold. In addition to the textual content contained within the post, your tool can also use a variety of other input sources to improve its decision-making, including feedback from the human moderators that help improve the accuracy of the model over time. 

| Category | Details |
| --- | --- |
|*Type of technology:*| Hate Speech Classifier|
|*Context of Use:*| Social Media Platform|
|*Outcome:*| Binary variable ('hate speech' or 'not hate speech') with confidence rating |
|*Project Team:*| Social Media Consultants and Platform|
|*Data Types:*| `Text content of post`, `Links or URLs`, `Network or connections of user`, `Tags`, `Images`, `Use of emojis`, `Liked communities`, `Stored cookies`, `Moderator feedback`|
|*Data Source(s):*| Social Media Company Data |
