# w4156-lecture-code
Lecture code accompanying W4156

# Disclaimer
This project is perhaps the only project that can committed with broken tests as the examples are 'start from here and fix issue'

# Dependencies


## Git and Version Control
[Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).

#### Installing Git:
##### On Mac:
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

##### On Windows:
- Download Git from Git for [Windows](http://gitforwindows.org) and install.

##### On Linux:
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

### GitHub and Git 

##### Cloning our projectrepository from GitHub:
To clone/download this repository to your computer:
- Look for the green clone or download button in the code tab of the repository and click on it.
- Copy the https link of the git repository that is displayed
- Open the terminal on your computer and navigate to location where you want your repository to be saved
- Type git clone followed by repository-link-you-copied, so in this case:
```
git clone https://github.com/geod/w4156-lecture-code.git
```
- Cloned repository should now be locally available on your computer in location you specified.
- You could also download a zipped version of the project by clicking download zip option.

## Installing Pycharm IDE:
- You will first need to create a JetBrains account using your Columbia/Barnard `.edu` emails to gain student licenses to JetBrains products
- Go to https://www.jetbrains.com/student/ and click `Apply Now` to gain free access to JetBrains products
- Fill in the respective form and follow the steps to have your `.edu` emails authenticated
- Once you’ve been approved, select Pycharm from the list of products available from your JetBrains account and follow the installation guide.

### Opening project in Pycharm:
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


## Setup without Pycharm can also be done as follows:
Assumes [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) is installed.
```
virtualenv --python=python3.6 venv
source bin/venv_activate.sh
pip install -r requirements.txt
```
