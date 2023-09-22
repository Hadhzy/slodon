# What to except from this chapter?

By the end of this chapter you will have a basic understanding of the project's structure including the [folder-system](#folder-system) , [workflows](#workflows), and [task-management](#task).

---
<div class="warning" style='background-color: hsla(232,15%,21%,1); box-shadow: 0 0 5px #d90429; color: white; border: 2px solid #d90429; border-radius: 12px;'>
<div style='font-size:16px; font-weight:semi-bold; padding: 10px; border-radius: 10px 10px 0px 0px; background-color: #ef233c;'>
  <span style="">Warning<span> 
</div>
<span>
<div style='margin-left: 11px; padding: 2px; margin-top: 10px; text-align:left'>
<span class='font-style: bold; color: #cf1121'>The folder structure may change in the future, therefore the information in here may be irrelevant at the time you are reading it, however we are doing our very best to keep our docs updated, if you encounter such issues then feel free to message to our discord server.</p>
</div>
</p></span>
</div>

---

# Folder System

```bash
├───.github
│   └───workflows
├───docs
│   └───docs
│       ├───API
│       ├───developer-guide
│       ├───fundementals
│       ├───hadhzy-python-xlib
│       ├───hzy
│       ├───model
│       ├───paper
│       └───slodonix
├───etc
│   └───images
├───paper
├───slodon
│   ├───api
│   │   ├───test
│   │   └───utils
│   │       └───locales
│   │           ├───de
│   │           └───en
│   ├───cli
│   ├───slodonix
│   │   ├───examples
│   │   │   ├───windows
│   │   │   └───xlib
│   │   ├───slodonix
│   │   │   └───exceptions
│   │   └───systems
│   │       ├───wayland
│   │      
│   │       ├───windows
│   │       └───x
│   ├───SLoScrap
│   └───SloSynth
└───_static
    └───images
```

- [`docs`](https://github.com/Hadhzy/slodon/tree/main/docs): This folder contains the content of this website, for more information about the docs check out the [developer guide](https://slodon.io/developer-guide/developer-guide/). 
- [`etc`](https://github.com/Hadhzy/slodon/tree/main/etc): etc contains essential markdown files such as *developing.md* *core_developer.md*
- [`paper`](https://github.com/Hadhzy/slodon/tree/main/paper): More about the paper can be found [here](https://github.com/Hadhzy/slodon/paper): TBD
- [`slodon`](https://github.com/Hadhzy/slodon/tree/main/slodon): Slodon is the main package of the project, therefore documentation about it can be found [here](https://slodon.io/).
- [`slodon/api`](https://github.com/Hadhzy/slodon/tree/main/slodon/api): This sub-package is not being used currently, and it might be removed before the release.
- [`slodon/cli`](https://github.com/Hadhzy/slodon/tree/main/slodon/cli): This sub-package is not being used currently, and it might be removed before the release. 
- [`slodon/slodonix`](https://github.com/Hadhzy/slodon/tree/main/slodon/slodonix): The Full Documentation about Slodonix can be found [here](https://slodon.io/slodonix/home/).
- [`slodon/SloScrap`](https://github.com/Hadhzy/slodon/tree/main/slodon/SLoScrap): The Full Documentation about SloScarp can be found [here](https://slodon.io/SloScrap/home.md).
- [`slodon/SloSynth`](https://github.com/Hadhzy/slodon/tree/main/slodon/SloSynth): The Full Documentation about SloSynth can be found [here](link).
- [`_static`](https://github.com/Hadhzy/slodon/tree/main/_static/images): Contains the different logos(*slodon_logo.png*, *slodonix.logo.png*, *SloScrap_logo.png*).

# Workflows 
- `.github`: Contains the workflows that are being used by the project. We currently having the following workflows:
  - `black.yml`: This workflow is responsible for formatting the code of the project, and it is using [black](https://pypi.org/project/black/) to do so.
  - `mypy.yml`: This workflow is responsible for checking the type hints of the project, and it is using [mypy]() to do so.
  - `pylint.yml`: This workflow is responsible for checking the code quality of the project, and it is using [pylint]() to do so.


  These tests need to reach a certain required level to be merged. 
  More information about using them can be found in the [developer guide]().
  (Right now the only server that can be used is Ubuntu)
  The workflows systems need to have cross platform testing.

  <div class="warning" style='background-color: hsla(232,15%,21%,1); color: white; box-shadow: 0 0 5px #2977ff; border: 2px solid #2977ff; border-radius: 12px;'>
<div style='font-size:16px; font-weight:semi-bold; padding: 10px;  border-radius: 10px 10px 0px 0px; background-color: #303952;'>
  <span style="">Note<span> 
</div>
<span>
<div style='margin-left: 11px; padding: 2px; margin-top: 10px; text-align:left'>
<span class='font-style: bold; color: #cf1121'>
Right now <a href="">our workflow</a> system doesn't support cross-platform, therefore you may encounter some issues which we apologise for. We are doing our best to implement this as soon as we possibly can.
</div>
</p></span>
</div>

---

# Task managment
It is really important to spread some information about task managment and how it applies for slodon.

There are ***2*** ways of being informed about the current state of the project.

- Firstly, following up with our Github [projects](https://github.com/Hadhzy/slodon/projects?query=is%3Aopen) board which is being updated and reviewed actively, we highly encourage everyone to repport issues there.
- Secondly, At this stage of the project a loads of discussion is needed, therefore the [discord server](https://discord.gg/gaRuN8jC) could be used as well.


