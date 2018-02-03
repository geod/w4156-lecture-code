[![Build Status](https://travis-ci.org/geod/w4156-lecture-code.svg?branch=master)](https://travis-ci.org/geod/w4156-lecture-code)

# w4156-lecture-code
Lecture code accompanying W4156

# Disclaimer
This project is perhaps the only project that can committed with broken tests as the examples are 'start from here and fix issue'

## Step 1: Install Git:
[Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).

### On Mac:
- The easiest is to install Git from the command line. Use the command below:
```
git --version
```
If you don’t have it installed already on your Mac, it will prompt you to install it by showing you a relevant git installation command based on your system's configurations.

You could also use [homebrew](https://brew.sh) which is a package management system for Macs
- In terminal copy and run the following:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew doctor
brew install git
```

### On Windows:
- Download Git from Git for [Windows](http://gitforwindows.org) and install.

### On Linux:
Open a terminal window. Copy & paste the following into the terminal window and hit Return. You may be prompted to enter your password.
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
```

Git downloads for all systems with further instructions, can also be found [here](https://git-scm.com/downloads).

Git will be covered during lectures. Some simple cheat sheets are listed below:
 - [GitHub's Git Cheat Sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
 - [Git reference docs](https://git-scm.com/docs)

## Step 2: For this repository and download:
You are going to 'fork' the repo to have your own copy. This means you can work on labs and commit locally.

To fork it follow these [instructions](https://help.github.com/articles/fork-a-repo/) 

Before you follow the instructions create a directory where you will work. Generally I create two folders
1. /home/me/developer (where I keep all codebases)
2. /home/me/developerTools (where I download any common developer tools across projects)

You then need to clone the fork you have created. See [instructions](https://help.github.com/articles/fork-a-repo/#step-2-create-a-local-clone-of-your-fork)

## Step 3: Install Pycharm IDE:
- Create a JetBrains account using your Columbia/Barnard `.edu` emails to gain student licenses to JetBrains products
- Go to https://www.jetbrains.com/student/ and click `Apply Now` to gain free access to JetBrains products
- Fill in the respective form and follow the steps to have your `.edu` emails authenticated
- Once you’ve been approved, select Pycharm from the list of products available from your JetBrains account and follow the installation guide.

## Step 4: Opening project in Pycharm:
Once you have Pycharm open, click on:

File -> Open -> Project Name, in this case `w4156-lecture-code`

Pycharm allows for the creation and use of virtual environments. We will be using virtual environments in this course to ensure that dependencies, versions, and permissions can be maintained and modified accordingly with relative ease. In this course, we will be using the virtual environment system [virtualenv](https://virtualenv.pypa.io/en/stable/) which can be installed by following these [instructions](https://virtualenv.pypa.io/en/stable/installation/), but we shall instead do it directly from Pycharm because virtualenv comes bundled with Pycharm.

Steps to create a virtual environment in Pycharm can be found [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html).

Remember that we want to use the dependencies stated in `requirements.txt` of the project and python version 3.6 thus, we need to ensure we are using the python 3.6 version of the virtual environment and not that of the computer's Operating System.

If that is a bit confusing you should follow these steps:
- Click on file menu option and go to default settings
- Select Project Interpreter from options on the left
- Click settings “cog wheel” icon at right of project interpreter form and select `add local`
- If you’ve never used a virtual environment on your computer select new environment and configure accordingly choosing base interpreter version to be python 3.6 and check the boxes that follow.
- If you want to use an existing virtual environment on your machine select the second option and make sure you ensure dependencies that appear in requirements.txt file are installed
- At this point, anytime you make a change to requirements.txt, Pycharm will ask you to install the new dependency. For more information, you can check this [link](https://www.jetbrains.com/help/pycharm/creating-requirement-files.html).

If your system does not have python 3.6 to be used as the interpreter for your virtual environment, you can download it from [here](https://www.python.org/downloads/). Once you have python 3.6, you should be good to go and enable it as your base interpreter for your virtual environment.

 If you want to manage multiple python versions on your system; if you're working on a python project for a different class or personal project that uses a specific version, [pyenv](https://github.com/pyenv/pyenv) will help you do just that! However, it only works on Mac and Linux systems. Note if you use pyenv to install python 3.6, it uses a virtual environment so all you have to do is select existing environment option instead of creating a new one from the project interpreter menu.

 Lastly, if Pycharm for some reason is not automatically picking up your `requirements.txt` file as its source for packages and dependencies, you can configure it by going to Settings/Preference dialog then click [Python Integrated Tools](https://www.jetbrains.com/help/pycharm/python-integrated-tools.html?keymap=secondary_mac_os_x), and finally make sure that package requirements file is set to `requirements.txt`.

## Alternative: Setup without Pycharm can also be done as follows:
Assumes [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) is installed.
```
virtualenv --python=python3.6 venv
source bin/venv_activate.sh
pip install -r requirements.txt
```
