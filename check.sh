#!/usr/bin/sh
git_status_display() {
  set flag=0
  #if there is a chnage in git status
  if [[ `git status --porcelain` ]]; then
    git status
    flag=1
  else
    echo no change in git repo
    flag=1
  fi
  return $flag
}

#open python script as needed
run_python_character_script() {
  python script.py
}

main() {
  myVar=$PWD
  echo Current directory: $myVar

  #var for fucntion
  git_status_display
  set result=$?
  if [[ $result -eq 0 ]]; then
    echo launching atom
    atom
  elif [[ $result -eq 1 ]]; then
    run_python_character_script
  fi
}

main
