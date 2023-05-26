---
hide:
  - navigation
  - toc
---

# About this Module - Fairness

!!! info  "**Important**"

    This module is not a technical introduction to Fair ML methods, nor does it attempt to provide an up-to-date overview of the current methods in the field.
    New methods are currently being developed at a rapid pace, and many of these methods are designed to solve problems with specific techniques (e.g. privacy-preserving federated learning to protect interest of vulnerable groups).
    It is not possible, nor desirable, to keep these resources up-to-date with these sorts of developments.
    Rather, we aim to provide clarity on the practical and ethical consequences of fairness in data-driven technologies.
    As such, we discuss those methods (or classes of methods) that are well established and have wide applicability across domains and use cases.

This module is about the importance of fairness in data-driven and AI systems. It approaches fairness as a multi-faceted concept comprising different, equally relevant, aspects. 
The module is divided into four sections: first, a broad look into what fairness is and the difficulties associated with defining the concept. 
It then introduces two relevant aspects of fairness in the context of AI and data-driven systems: sociocultural fairness and statistical fairness. 
The last section focuses on the role bias identification and mitigation play in the project lifecycle and how it intersects with questions of fairness.

## Learning Objectives

This module has the following learning objectives:

- Explore the concept of fairness in general, understanding the difference between utilitarian, economic egalitarian, and libertarian theories of fairness.
- Understand what is meant by fair procedures in allocating a good or service, as well as what is meant by outcome fairness and how we can make comparisons between different outcomes.
- Analyse the concept of sociocultural fairness and how it relates to sociotechnical systems (such as AI and data-driven ones). 
- Learn how to identify fairness factors and the difference between impermissible factors and potentially permissible factors.
- Reflect upon aspects of sociocultural fairness such as: whether there are divides or barriers that obstruct people from accessing technology, whether there are differences in how different groups are represented by these technologies, and consider the invisible or ghost labour that goes into creating most sociotechnical system.
- Understand what is meant by statistical fairness, why it is relevant and what its limitations as a concept are.
- Identify different issues arising within statistical fairness (imbalanced classes, the precision-recall trade-off, variation in base rates, and establishing ground truth).
- Understand the three main criteria for non-discrimination for group fairness (independence, separation, and sufficiency).
- Identify the three different kinds of bias (social, statistical, and cognitive) and how these can arise within and AI or data-driven system.
- Explore different avenues for mitigating biases.

## Table of Contents

<div class="grid cards" markdown>

-   :octicons-beaker-16:{ .lg .middle } __What is Fairness?__

    ---

    This section is the introduction for the module and it is a broad-stroke look into what the concept of fairness means. 
    As we will see, there is no easy answer to this as it will depend on underlying values which might be different for different people.
    It also focuses on questions around procedures for adjudicating goods or services (who should get what and how we decide on this), as well as questions around fairness in outcomes.

    [:octicons-arrow-right-24: Go to module](rri-203-1.md)

-   :fontawesome-solid-arrows-spin:{ .lg .middle } __Sociocultural Fairness__

    ---

    This section introduces the concept of sociocultural fairness and its relevance to design, development, and deployment of AI and data-driven systems.
    We look at the pre-conditions required to make a system fair, which we call *fairness factors* and when and why they may or may not be in place. 
    This section also explores issues around the digital divide between different sectors in society and the ghost labour implicit in the creation of many of these systems.  

    [:octicons-arrow-right-24: Go to module](rri-203-2.md)

-   :material-thought-bubble:{ .lg .middle } __Statistical Fairness__

    ---

    This section focuses on statistical notions of fairness. It uses a binary classification task as a running example to help illustrate different group fairness considerations that arise when working with data. It looks at problems with imbalanced classes and accuracy, the prediction-recall trade-off, variations in base rates, and the problems with establishing ground truth. It also provides a broad overview of the most important statistical fairness or non-discrimination criteria for group fairness (independence, separation, and sufficiency). 

    [:octicons-arrow-right-24: Go to module](rri-203-3.md)

-   :material-chat-processing:{ .lg .middle } __Practical Fairness__

    ---

    In the module's final section we turn our attention to the concept of biases: what they are, how they can arise in a machine learning or AI project, and what can be done to appropriately mitigate them. We divide biases into three broad categories; social, statistical, and cognitive, and then look at each category in detail. Finally, we give an overview of different strategies teams and researchers can employ to mitigate biases once they have been identified.

    [:octicons-arrow-right-24: Go to module](rri-203-4.md)

</div>
