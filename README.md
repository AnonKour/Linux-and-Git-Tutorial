# Linux-and-Git-Tutorial

This is a tutorial that aims to assist in understanding some basic commands on linux and git.

## Linux Commands:

The commands that we are going to cover on this tutorial are the following:

- man&nbsp;&nbsp;&nbsp;[*An interface to the on-line reference manuals*] Should be used along side --help in order to better understand a command.
- pwd&nbsp;&nbsp;&nbsp;[*Prints the full filename of the current working directory.*]
- ls (-l)&nbsp;&nbsp;&nbsp;[*List information about the files (the current directory by default).  Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.*]
- cd&nbsp;&nbsp;&nbsp;[*Navigates to the specified directory.*]
- mkdir&nbsp;&nbsp;&nbsp;[*Create the directory(ies), if they do not already exist.*]
- rm&nbsp;&nbsp;&nbsp;[*Removes files or directories.*]
- cp&nbsp;&nbsp;&nbsp;[*Copies files and directories.*]
- mv&nbsp;&nbsp;&nbsp;[*Moves, renames files.*]
- nano, vi, gedit&nbsp;&nbsp;&nbsp;[*Creates files and edits them, nano and vi are on terminal editors while using another editor such as gedit will open that editor.*]
- touch&nbsp;&nbsp;&nbsp;[*Similar with the other editors although is mostly used to change file timestamps.*]
- chmod&nbsp;&nbsp;&nbsp;[*Change the file mod bits.*]
- grep&nbsp;&nbsp;&nbsp;[*Prints lines matching a pattern.*]
- dolphin ./&nbsp;&nbsp;&nbsp;[*Depending on the operating system the appropriate explorer must be used.*]
- sudo [*Allows a permitted user to execute a command as the superuser or another user.*]
- apt-get 
	- update
	- upgrade
	- pugre
- apt-cache search
- ssh&nbsp;&nbsp;&nbsp;[*OpenSSH SSH client for remote login*]
- scp&nbsp;&nbsp;&nbsp;[*Secure copy for remote file copy*]
- zip, unzip
- ifconfig&nbsp;&nbsp;&nbsp;[*Configures a network interface, also prints network information.*]
- uname&nbsp;&nbsp;&nbsp;[*Prints system information.*]
- ping&nbsp;&nbsp;&nbsp;[*Sends ICMP ECHO_REQUEST to network hosts and provides info regards the jumps.*]

## Git requirements

Git is a version control service that allows us to work on our projects with a use of handy tools such as:
- Versioning along with history.
- Branching
- Stashing
- Even distributing of a release.


- Git Bash installation
```
$ sudo apt install git-all
```
- In order for the example program to run python must be installed.
```
$ python3 --version //In order to check if we already have a version installed.
$ sudo apt-get update
$ sudo apt-get install python3.6
```
- Git clients
```
wget https://release.gitkraken.com/linux/gitkraken-amd64.deb
dpkg -i gitkraken-amd64.deb
```

## Git Commands

Git global setup:
```
$ git config --global user.name "User Name"
$ git config --global user.email "username@somemail.com"
```
Can check it by using:
```
$ git config --list
```
Create a **new repository**:
```
$ git clone git@gitlab.com:UserName/linux-git-tutorial.git
$ cd linux-git-tutorial
$ touch README.md
$ git add README.md
$ git commit -m "add README"
$ git push -u origin master
```
Existing folder:
```
$ cd existing_folder
$ git init
$ git remote add origin git@gitlab.com:UserName//linux-git-tutorial.git
$ git add .
$ git commit -m "Initial commit"
$ git push -u origin master
```
Existing Git repository:
```
$ cd existing_repo
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.com:UserName//linux-git-tutorial.git
$ git push -u origin --all
$ git push -u origin --tags
```
Create a **new commit** and push it to branch master:
```
$ git add .
$ git commit -m "New commit message."
$ git push -u origin master
```

**Fetch** any changes from master in order to **merge** them after:
```
$ git fetch
$ git merge
```

**Pull** any changes from master:
```
$ git pull
```

### Different Version Control repository management services

- https://usersnap.com/blog/gitlab-github/
- https://www.slant.co/topics/153/~best-hosted-version-control-services

### Different Version Control Clients. 

- https://desktop.github.com
- https://www.gitkraken.com

## Useful links

#### For Linux

- https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners

#### For Git

- http://try.github.io for trying out github.
- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners
- https://guides.github.com/features/mastering-markdown aka .md for the creation of README.md
- https://guides.github.com/features/wikis/
- https://help.github.com/en/articles/creating-releases
- https://guides.github.com/introduction/git-handbook/
- https://help.github.com/en/articles/create-a-repo
- https://longair.net/blog/2009/04/16/git-fetch-and-merge/
- https://git-scm.com/book/en/v1/Git-Tools-Stashing
- https://git-scm.com/downloads/guis
In case of an access denied.
- https://gitlab.com/help/ssh/README#generating-a-new-ssh-key-pair

##### For Git Kraken

- https://www.gitkraken.com/downloads/gitkraken-cheat-sheet-219.pdf
