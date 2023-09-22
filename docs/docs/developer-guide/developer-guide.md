# What to expect from this guide?
This guide shows you how to use and contribute to **Slodon** with its full potential, step by step.

Each section *gradually builds* on top of the previous ones, but you can jump to any section you're interested in.
We will first cover the essentials and [setting up your environment](#get-started-with-the-project), then we will clarify [how to contribute to the project](#how-to-help-with-ongoing-features) and get the moust out of your contribution. After that we will take a look at one of the most important topic which is the [merging process](#merging-process). Finally we will discuss how to [report issues](#reporting-issues) and [discuss new features](#propose-a-new-feature).

Let's dive in!

# Get Started with the project
Assuming that you have basic knowledge about git you need to do the followings:

-  **[create a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo)**
- **clone the fork by running:**
```bash
git clone <your-fork-url>
```
- **Create a new feature branch on your fork by doing:**
```bash
$ git checkout -b [name_of_your_new_branch]
```

<div class="warning" style='background-color: hsla(232,15%,21%,1); color: white; box-shadow: 0 0 5px #2977ff; border: 2px solid #2977ff; border-radius: 12px;'>
<div style='font-size:16px; font-weight:semi-bold; padding: 10px;  border-radius: 10px 10px 0px 0px; background-color: #303952;'>
  <span style="">Note<span> 
</div>
<span>
<div style='margin-left: 11px; padding: 2px; margin-top: 10px; text-align:left'>
<span class='font-style: bold; color: #cf1121'>
In order to contribute to the project you need to install the <a href="https://github.com/Hadhzy/slodon/blob/main/requirements-dev.txt">dev requirements</a>, make sure to do that before you start working on the project.
</div>
</p></span>
</div>


- **Create a [virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) by running:**
```bash
python -m venv env
```
This will create a virtual environment in the current directory naming it env.
- **[Active virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments)**
- **Install requirements**:
```bash
pip install -r requirements-dev.txt
```
This will go ahead and install all of the dependencies that are listed in the [requirements-dev.txt](https://github.com/Hadhzy/slodon/blob/main/requirements-dev.txt) file.

# Todos and Tasks
Official todos and tasks can be found at the [proejcts board](https://github.com/Hadhzy/slodon/projects?query=is%3Aopen):

We are using multiple boards for different projects:

[slodon-general-todo](https://github.com/orgs/Hadhzy/projects/4):
This board is for general todos and tasks, it is not specific to any package. This includes general tasks that are not related to any subpackage but more to the whole project in general. This should be prevent from users and only core developers should be able to access it. 

[Slodonix](https://github.com/orgs/Hadhzy/projects/13):
This board includes the tasks and todos specifically realted to the [Slodonix]() package. Furthermore the board includes issues that were opened for this subpackage, meaning that when the issue was created, the `Slodonix` label was included, this makes the issue show up here, so make sure to be aware of this. The issues are being organised to three columns depending on the status of the issue. 

[SloSynth](https://github.com/orgs/Hadhzy/projects/15):
This board includes the tasks and todos specifically realted to the [SloSynth]() package. Furthermore the board includes issues that were opened for this subpackage. meaning that when the issue was created, the `SloSynth` label was included, this makes the issue show up here, so make sure to be aware of this. The issues are being organised to three columns depending on the status of the issue.

[SloScrap](https://github.com/orgs/Hadhzy/projects/8):
This board includes the tasks and todos specifically realted to the [SloScrap]() package. Furthermore the board includes issues that were opened for this subpackage, meaning that when the issue was created, the `SloScrap` label was included, this makes the issue show up here, so make sure to be aware of this. The issues are being organised to three columns depending on the status of the issue.

# Requirements

*[Main requirements are](https://github.com/Hadhzy/slodon/blob/main/pyproject.toml#L3-L10)*:

- `setuptools` -> Basic python dependency comes with every package.
- `wheel` -> Basic python dependency comes with every package.
- `websockets` -> This probably going to be removed in the future. (Right now it represent a unique websocket server from scratch for the model.)
- `typer` This probably going to be removed in the future. (Empowers CLI)
- `textual` -> This probably going to be removed in the future. (Colourized CLI)
- [hadhzy-python-xlib](https://pypi.org/project/hadhzy-python-xlib/)` -> Our fork of the python-xlib project, empowers the x display server.

*[Dev requirements are](https://github.com/Hadhzy/slodon/blob/main/requirements-dev.txt)*:

*These requirements are essential for contributing to the project(not part of the basic package)*

- [`pylint`](https://pypi.org/project/pylint/) -> Empowers the linter
- [`black`](https://pypi.org/project/black/) -> Empowers the formatter
- [`mypy`](https://mypy.readthedocs.io/en/stable/) -> Used for static type checking.
- [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) -> Empowers the documentation

# How to help with ongoing features
If you consider helping with ongoing tasks, and not neccessarily interested in proposing a [new feature](#propose-a-new-feature) the following might be useful.

- Checking out our [project's board](https://github.com/orgs/Hadhzy/projects) should be the first thing, this is very essential and it will give an idea of what we are dong daily. 

- If you have not already joined to our [discord server](https://discord.gg/gaRuN8jC) than this is the time to do so, this might be the best place to get started. This is where new ideas are forming and majority of the fun is going on. Also if you need any help or having any concerns about our project then this is the place to do it. You definitely don't want to miss out on that. 

- Checking out the [issue page](https://github.com/Hadhzy/slodon/issues): This is where bug reporting is happening, and accepted proposals occur. Having a look at the issue page might be a good idea to get started.
    
# Propose a new feature:
In order to propose a new feature you have to follow a few rules:

- Firstly, if you want to propose a new feature you have to make sure that you are following up with our todos and current tasks, this is essential and will give you an idea that what are we currently working on and what are we planning to do next. Also this is where we are handling issues and discussing new features. That means that you have to be familiar with the [project's board](https://github.com/orgs/Hadhzy/projects), our [github discussions](https://github.com/orgs/Hadhzy/discussions) and our [discord server](https://discord.gg/gaRuN8jC).

**To Propose a new feature to the project properly**:
    - Check out the [project's board](https://github.com/Hadhzy/slodon/projects?query=is%3Aopen) -> where you can see the outgoing tasks
    - Propose it in the [discord server](https://discord.gg/gaRuN8jC) -> At the moment, our community is based on the discord server, having a conversation about a proposal might be a the best idea before getting started. 
    - Open a [new issue](https://github.com/Hadhzy/slodon/issues) -> According to famous and respected open source projects, the issue page is one of the best places to tell us your proposal idea.
    **The proposal must happen on the [issue](https://github.com/Hadhzy/slodon/issues) page.**

    Our Official Template for proposing a new feature:
    ```
    Title: New feature proposal: Implementing ... (name of the new feature)
    Description: A long description about the feature that you wish to propose.
    History: It is also necessary to include old issues or feature proposals which are similiar or have any level of correlation with your proposal.
    Thread: If there is a thread already discussing your idea please make sure to link that here.
    Examples: Add examples to help us understand what you want to achieve, the more specific the better(code snippets, showing the proposed feature).
    Technical Implementation: This is where you describe how you are planning to implement this technically(make sure to link the relevant source code), this section also should contain some code snippets, or a pr.
    ```



# Merging process
Now you've got to the point where you have finished your work and you are ready to merge your work to the main branch. This is the most important part of the process, and it is very important to do it properly. We have certain requirements that you have to follow in order to merge your work to the main branch. These are the following:

- Assuming that you have created a feature branch, you need to update your main branch first(on your fork). Make sure to do that first before moving on.
- Secondly, Open a PR from your fork.
- Once your PR has been opened, we require every one of our PRs to meet with the following requirements: 
    - The code needs to be formatted by [black](https://github.com/orgs/Hadhzy/projects/8), If not then the checking will fail, also make sure to format every single file because you may get errors related to this issue. 
    - The code quality have to be above 9 out of ten. You may [check out](https://docs.pylint.org/run.html#invoking-pylint) the code quality and improve it before opening the PR.
    - Additionally we are also using static type checking, so it's essential to provide the right types.[Invoke mypy locally](https://mypy.readthedocs.io/en/stable/getting_started.html#installing-and-running-mypy).

# Reporting issues
To report a new issue/bug you can check whether it was reported before or not, don't miss out on this as it can cause inconvenience. 
If you think you have discovered a new issue/bug please open a github issue under the correct lable.
You may also want to open a new bug thread on the [discord-server](https://discord.gg/gaRuN8jC) as well.


# Contribute to docs
If you are interested in contributing to the docs, this chapter is for you.

Assuming you have installed [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) already, you need to do the followings:

- navigate to the docs folder -> [`slodon/docs`](https://github.com/Hadhzy/slodon/tree/main/docs) (NOTE: you need to be in the folder where the [`mkdocs.yml`](https://github.com/Hadhzy/slodon/blob/main/docs/mkdocs.yml) lives, otherwise its not going to be recognised)
- Execute the command: `mkdocs serve` -> which should start the website locally.

Now, you have a working system, we can look at the structure of the documentation.

Every single endpoint needs to be [registered](https://github.com/Hadhzy/slodon/blob/main/docs/mkdocs.yml#L56) in the [`mkdocs.yml`](https://github.com/Hadhzy/slodon/blob/main/docs/mkdocs.yml) file.
Corresponding folders for endpoints exist under [`slodon/docs/docs`](https://github.com/Hadhzy/slodon/blob/main/docs/mkdocs.yml), where inside every folder a markdown file is defined.
You might need to create a new folder if you are considering adding a new endpoint by following the same arhitecture.
