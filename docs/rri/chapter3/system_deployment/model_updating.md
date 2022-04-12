# Model Updating or Deprovisioning

We come now to the end of the project lifecycle!

In the previous section we saw that model drift can affect the accuracy and overall performance of a model.
One way to address this is to update the model by retraining on more timely and up-to-date data.

Model updating can occur **continuously** if the architecture of the system and context of its use allows for it.
This can help prevent model drift from occurring in the first place.
However, this type of *online learning* is a challenging task, and is not without its limitations.
For instance, it introduces a further source of uncertainty into how the model and system will perform, given their close coupling with the environment.

Alternatively, model updating can occur **periodically**.
Perhaps, there is known seasonal variation in the performance of a system (e.g. a recommender system for an e-commerce site that has to adjust for varied shopping patterns).
As such, the re-training of the model may be planned around these times to help maintain a high-level of performance.

These types of updating can use the original model as a starting point, in order to just retune the model's parameters or maybe drop certain features that are no longer predictive.
However, there is also the option of entirely *de-provisioning* (i.e., stopping use) the model and system if performance simply drops too low to be addressed by mere re-training.

## Full Circle

As you may recall, the project lifecycle image showed this final stage connected to the first stage of '[Project Planning](../project_design/planning.md)' in a circular manner.

```{figure} /images/graphics/project-lifecycle.png
---
align: center
name: project-lifecycle-2
alt: The Project Lifecycle. 
---
The Project Lifecycle. 
```

The reason for this should now be clearer.
Depending on the choices made at this stage, it may be necessary to start planning for a new project.
For instance, a project team may not be able to simply *remove* a system that serves a business critical function.
Instead, an existing project may serve as a foundational input or constraint into the planning stages of a new project—starting the cycle once more.
