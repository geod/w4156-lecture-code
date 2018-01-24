# w4156-lecture-code

Lecture code accompanying W4156

# Disclaimer

This project is committed with broken tests as the examples are 'start from here and fix issue'

# Git and Version Control
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. This allows developers to keep track of changes made on their projects and also allows for collaboration with other developers on the same project. Some popular version control systems include git, mercurial, subversion (SVN), but for this course, we shall be using Git.  For more information on version control systems and how they work, go [here](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

### Installing Git:
Before you start using Git, you have to make it available on your computer. Even if it’s already installed, it’s probably a good idea to update to the latest version. You can either install it as a package or via another installer, or download the source code and compile it yourself.

##### On Mac:
- The easiest is to install Git from the command line. Use the command below:

    `git --version`

If you don’t have it installed already on your Mac, it will prompt you to install it.

You could also use [homebrew](https://brew.sh) which is a package management system for Macs
- In terminal copy and run the following:  
- `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
- `brew doctor`
- `brew install git`

##### On Windows:
- Download Git from Git for Windows (http://gitforwindows.org) and install it.

##### On Linux:
Open a terminal window. Copy & paste the following into the terminal window and hit Return. You may be prompted to enter your password.
- `sudo apt-get update`
- `sudo apt-get upgrade`
- `sudo apt-get install git`

Git downloads for all systems with further instructions, can also be found [here](https://git-scm.com/downloads).

Git can be a little confusing to begin with because there are so many commands.These links provide some insight on basic ones you should know and will be using frequently during the course.
 - https://orga.cat/posts/most-useful-git-commands
 - https://github.com/bpassos/git-commands


### GitHub and Git 
GitHub is a web-based hosting service for version control using git. It is mostly used for maintaining software code. It offers all of the distributed version control and source code management functionality of Git as well as adding its own features. Most of the work done between developers involves cloning, pushing and pulling changes made from a software project/repository that is hosted on GitHub.

##### Cloning our repository from GitHub:
To clone/download this repository to  your computer:
- Look for the green clone or download button in the code tab of the repository and click on it.
- Copy on the https link of the git repository
- Open the terminal on your computer and navigate to location where you want your repository to be saved
- Type git clone followed by repository-link-you-copied, so in this case:
` git clone https://github.com/geod/w4156-lecture-code.git`
- Cloned repository should now be locally available on your computer in location you specified.
- You could also download a zipped version of the project by clicking download zip option.

### Working with Pycharm
Pycharm is a python IDE: An integrated development environment (IDE). IDEs are software applications that provide comprehensive facilities to computer programmers such as a source code editor, build automation tools, and a debugger.

##### Installing Pycharm:
- You will first need to create a JetBrains account using your Columbia/Barnard .edu emails to gain student licenses to JetBrains products
- Go to https://www.jetbrains.com/student/ and click "Apply Now" to gain free access to JetBrains products
- Once you’ve been approved, select Pycharm from the list of products available and follow the installation guide. You may need to verify your license/activation code before you can have full access to these products. This information can be obtained from your JetBrains account once approved.

##### Opening project in Pycharm:
Pycharm allows for the creation and use of virtual environments. We will be using virtual environments in this course to ensure that dependencies, versions, and permissions can be maintained and modified accordingly with relative ease. In this course, we will be using the virtual environment system [virtualenv](https://virtualenv.pypa.io/en/stable/) which can be installed by following these [instructions](https://virtualenv.pypa.io/en/stable/installation/), but we shall instead do it directly from Pycharm because it has virtualenv installed already.

Steps to create a virtual environment in Pycharm can be found [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html). Remember that we want to use the dependencies stated in `requirements.txt` of the project and python version 3.6

If that is a bit confusing you should follow these steps:
- Click on file menu option and go to default settings
- Select Project Interpreter from options on the left
- Click settings “cog wheel” at right of project interpreter form and select add local
- If you’ve never used a virtual environment on your computer select new environment and configure accordingly choosing base interpreter version to be python 3.6 and check the boxes that follow
- If you want to use an existing virtual environment on your machine select the second option and make sure you ensure dependencies that appear in requirements.txt file are installed
- At this point, anytime you make a change to requirements.txt, Pycharm will ask you to install the new dependency. For more information, you can check this [link](https://www.jetbrains.com/help/pycharm/creating-requirement-files.html).

###### Setup without Pycharm can also be done as follows:
1. `virtualenv --python=python3.6 venv`
2. `source bin/venv_activate.sh`
3. `pip install -r requirements.txt`

This assumes you have [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) already installed on your computer.
