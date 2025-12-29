# Part 1, Session 1 - Git and GitHub


## Description

- Git is a distributed and modern Source Control System (DSCM)
- It creates versions of each file, with incremental changes
- Git was created by Linus Torvalds for the development of Linux
- GitHub is a cloud-based PaaS (platform as a service) for Git
- Git can be used locally on your workstation without GitHub
- The .gitignore file - some files/paths shouldn't be stored in git
- Branches - main and features
- Pull Requests (i.e. - PRs) - Peer requests to review and merge feature branch into the main branch

## GitHub Account Creation

 -[Account Creation](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
 -[Types of Accounts](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)

## Installation

 -[Download](https://git-scm.com/install/)
 -[macOS Homebrew](https://formulae.brew.sh/formula/git)

## Configuration

Configure your user.name and user.email.

```
git config --help 

git config --list 

git config --global user.name  "Jane Smith"
git config --global user.email "jane.smith@gmail.com"
```

## Authentication

- Password and SSH (secure shell protocol)
 -[GitHub Authentication Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)

## Demonstration - Git Command Examples


```
md| pull, branching, push, checkout, ls-files, diff, ls-files, help
```

 -[Git Cheat Sheet](https://git-scm.com/cheat-sheet)

## Demonstration - GitHub Desktop UI

 -[Installation](https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop)

<p align="center">
   <img src="img/github-desktop.png" width="60%">
</p>


## Pro Tip: Aliases I use

- Added to ~/.bash_profile (macOS) or Windows 11 Profile as functions
- gb = what branch am I on?
- gls = list files in the repository
- gs = git status
- gup = git pull, reset, gc, branch
- gurl = get the remote origin url

```
alias gb='git branch'
alias gls='git ls-files'
alias gs='git status'
alias gup='git status ; git reset --hard ; git pull ; git gc ; git branch'
alias gurl='git config --get remote.origin.url'
```

### Windows PowerShell Profile Functions 

```
function gb {
    git branch
}

function gls {
    git ls-files
}

function grh {
    git reset --hard
}

function gs {
    git status
}

function gup {
    git status ; git reset --hard ; git pull ; git gc ; git branch
}

function gurl {
    git config --get remote.origin.url
}
```

## References

 -[Linux Torvalds on Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds)
