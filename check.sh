#!/usr/bin/env sh
git_status_display() {
  git status
  #open python script as needed
  python script.py
}
cd python-automation
myVar=$PWD
echo moved into python directory
echo Current directory: $myVar
ls
#call the git_status fucntion
git_status_display
