# Notes on Data Analysis Activity

<!-- I've added a set of slides from a DECOVID project presentation with some information on NEWS2, which is a real-world early warning system used to triage patients and predict risk of deterioration. The goal is not to mimic this model, but just to take some inspiration. Slides are here: https://github.com/chrisdburr/turing-commons/blob/master/guidebooks/rri/chapter4/ews_presentation.pdf -->

## Goals/Objectives

- To introduce participants, many of whom will not be data scientists, to some of the issues that arise during the exploratory data analysis (EDA) stage
- To discuss how a range of biases can affect the process of EDA
- To visualise the effects of bias on data analysis

## Case Study

A research team are exploring whether risk of deterioration from COVID-19 can be predicted during admission and triaging of patients. They have a dataset collected over the course of a couple of months from a single hospital. The dataset includes a variety of demographic and physiological parameters for each patient and indicates whether/when they deteriorated and if they required emergency invasive ventilation.

### Features

<!-- See slides for information about permissible ranges for physiological parameters: https://github.com/chrisdburr/turing-commons/blob/master/guidebooks/rri/chapter4/ews_presentation.pdf -->

- (Pseudonymous) NHS number
  - This can just be a random string of digits (e.g. #186357)
- Age (range, not lower than 80)
  - 18–30
  - 31-40
  - 41–50
  - 51–60
  - 61–70
  - 71-80
  - 80+
- Gender
  - Male
  - Female
  - null
- Ethnicity (official distributions: https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/population-of-england-and-wales/latest / COVID deaths by ethnicity: https://www.gov.uk/government/publications/covid-19-reported-sars-cov-2-deaths-in-england/covid-19-confirmed-deaths-in-england-report)
  - White 
    - English, Welsh, Scottish, Northern Irish or British
    - Irish
    - Gypsy or Irish Traveller
    - Any other White background
  - Mixed or Multiple ethnic groups
    - White and Black Caribbean
    - White and Black African
    - White and Asian
    - Any other Mixed or Multiple ethnic background
  - Asian or Asian British
    - Indian
    - Pakistani
    - Bangladeshi
    - Chinese
    - Any other Asian background
  - Black, African, Caribbean or Black British
    - African
    - Caribbean
    - Any other Black, African or Caribbean background
  - Other ethnic group
    - Arab
    - Any other ethnic group
- BMI*
- Received Respiratory Support (e.g. CPAP)*
- Date of admission (spanning 3 months)
- Outcomes
  - Received invasive ventilation (yes/no) (w/ date of treatment)
    - Have rate of invasive ventilation drop from 50% to 10% after two months, to signify changing clinical practices, but don't have effect on clinical outcome
  - Clinical Outcome (survived/died)

### Biases to show

These are the biases that we will probably explore in the guidebook and activity

- Label bias
  - The use of binary gender options may complicate data collection, as some individuals may have refused to disclose (i.e. 'null')
- Missing data bias
  - One group should be missing from the data (probably elderly people who would not have made it to hospital and, therefore, not been triaged or seen healthcare professional)
- Chronological bias
  - There could be a marked difference between patients who were admitted in first few weeks, versus those who were admitted towards end of dataset due to improved practices in the hospital
- Confounding
  - Dataset may not be sufficient to rule out confounders
- Cognitive bias
  - Did the participant have a prior belief about what to expect that influenced the judgement of the analysis?