# Activty 4: Contributing to Collaborative Projects

In a [later section](../chapter3/model_development/model_reporting.md), we will look at why active contribution to clear and accessible documentation is an important means for ensuring responsibility in collaborative projects.
However, the need to support asynchronous collaboration poses challenges when working in large teams.
I'm sure we have all experienced the feeling of despair that arises when trying to find the most recent version of a draft article in your inbox, and finding multiple instances of files named, `document_v1.docx`, `document_v1.1.docx`, `document_final.docx`, `document_final_v2.doc`... and so on!

```{image} /images/graphics/versions.jpeg
:alt: A person drowning in a sea of paper
:align: center
```

![A person drowning in a sea of paper](../assets/images/graphics/versions.jpeg){ align="center" }

## Enter GitHub

GitHub has become an increasingly popular solution to address this challenge of document version control.
While originally used by software developers wishing to share and contribute to code, the platform also has a range of features that make it ideal for managing scientific research projects.
As such, it is frequently recommended by those in the [Open Science](https://openlifesci.org) community.
If you are completely new to GitHub, the following video offers a useful introduction.
Be sure to pay attention to the discussion of branches, issues, and pull requests specifically—we will be using these features in the current activity.

<iframe width="560" height="315" src="https://www.youtube.com/embed/w3jLJU7DT5E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Familiarising Yourself with GitHub

!!! warning "Activity"

    Unfortunately, this activity can only be done when using this guide as part of an instructor-led training course.
    However, there are other ways to use GitHub to contribute to this project ([click here](https://github.com/alan-turing-institute/turing-commons/blob/master/CONTRIBUTING.md)).

This activity is a relatively easy one, but it's also very important for some of the later activities.
You will be guided through the following steps, which you will then perform yourself:

1. Create a GitHub account (if you don't have one already)
2. Explore the Turing Commons Repository
3. Make a contribution
   - Fork the repository to your own account
   - Make a change to the [Participants](../resources/participants.md) file
   - Submit a "pull request"
4. Add to an issue and list yourself as a contributor

### Create a GitHub account

This is the easiest of the steps.
Head on over to [GitHub](https://github.com/join) and sign-up for a free account.

### Explore the Turing Commons Repository

Perhaps you have already visited this using the link at the top of this page.
If not, head on over to this [book's repository](https://github.com/alan-turing-institute/turing-commons).

You will be greeted with a page that has a list of tabs along the top, a series of files and directories, and a section title README.md.
This is the homepage for the Turing Commons repository (or, 'repo' for short).
This is where all the files that are used to compile the website that you're currently reading this text from is stored. 
Feel free to click through the directories and open up the files.
The `guidebooks` directory is probably the most interesting place to browse.

### Fork the Repository

The next step is to "fork" the repo to your own account.
In short, this is creating a personal copy of the repository to your own account, which you can then freely edit.

Now, in your own copy of the repository, head on over to the following file:

`/rri/resources/participants.md`

Here, you can add your own GitHub username and leave a comment about your feelings for the course so far.

Click on the edit button and then type your username and add a comment 

![Screenshot of GitHub](../../assets/images/graphics/github.png)

!!! warning "Warning"

    Be careful to pay attention to the formatting!

Once you've done this, you will need to commit the changes directly to the `master` branch and add a message for your commit. This should be informative of the change you have made (e.g. "Added new line to table").

Now, go back to the main page of your forked repo and click on the button that says 'Contribute', and then 'Open pull request'.

This next screen will allow you to submit a *request* to the original owner of the repository to *pull* your changes into the main repository.
They will have to approve the changes you've made, but if all is okay then you will have just made a contribution to a collaborative project!

A lot of public repositories have codes of conducts or contributing guidelines, so it's good practice to read these before you try to submit a pull request.

### Add to an Issue

One reason for contributing to projects is when there are open issues and you can help resolve them.
A repository will have a list of open and closed issues that you can access from the main page by clicking on the 'Issues' button.
Individual issues are like threads or conversations.
There can be a lot of information to read through, especially if the issues is complex.

For this activity, we're going to use issues for something a little bit different—to automatically add you as a contributor.
After all, your contributing to this project by taking part 🥳

Go to the following issue and read the instructions: https://github.com/alan-turing-institute/turing-commons/issues/10 

### Congratulations 🎉

That's it, you've finished this activity!
There is, obviously, a lot **lot** more to GitHub than we have covered.
If you're interested in learning more, freecodecamp.org have a good [YouTube video](https://www.youtube.com/watch?v=RGOj5yH7evk) that manages to cram a lot into just over one hour.
I hope you come back here and contribute more to the Turing Commons afterwards 😄

<!---
Activity 3: Contributing to Collaborative Projects

If you are following this guide as part of an online course, there is an associated activity that is designed to help you collaborate with your team.
Please visit https://bit.ly/3lL2KTc to view the associated activity.

If you are reading this as a self-directed exercise, you can instead visit https://the-turing-way.netlify.app/collaboration/ to read more about collaborative research.
--->
