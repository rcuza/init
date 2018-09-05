#!/bin/bash

## If Mac has new mac smell, perform the following

if [ -f "`which brew`" ]
then
  echo "** brew installed"
else
  echo "ERR missing brew"
  echo "Make sure brew and brew cask are installed and rerun this script."
  echo "curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install > /tmp/brew_install_from_init"
  echo "ruby /tmp/brew_install_from_init"
  exit
fi

if [ -f "$(which ansible)" ]
then
  echo "** ansible installed"
else
  brew update && brew install ansible
fi

if [ -d "ansible" ]
then
  cd ansible && ansible-playbook makemacmine.yml && cd -
else
  echo "ERR missing ansible directory"
  echo "you might need to run 'git clone https://github.com/rcuza/init.git' to get it"
  exit
fi

####
# Install Janus
# https://raw.githubusercontent.com/carlhuda/janus/master/bootstrap.sh (4a7a9f2)
####
function die()
{
    echo "${@}"
    exit 1
}

function backup_previous_install()
{
  # Add .old to any existing Vim file in the home directory
  for filepath in "${HOME}/.vim" "${HOME}/.vimrc" "${HOME}/.gvimrc"; do
    if [ -e $filepath ]; then
      mv "${filepath}" "${filepath}.old" || die "Could not move ${filepath} to ${filepath}.old"
      echo "${filepath} has been renamed to ${filepath}.old"
    fi
  done
}

function clone_janus()
{
  # Clone Janus into .vim
  git clone --recursive https://github.com/carlhuda/janus.git "${HOME}/.vim" \
    || die "Could not clone the repository to ${HOME}/.vim"
}

function run_rake()
{
  # Run rake inside .vim
  pushd "${HOME}/.vim" || die "Could not go into the ${HOME}/.vim"
  rake || die "Rake failed."
  popd
}

function install_janus()
{
  if [ ! -e "${HOME}/.vim/janus" -o "$1" == "--force" ]; then
    echo "** installing janus"
    backup_previous_install
    clone_janus
  else
    echo "** janus installed"
  fi
  echo "** updating janus"
  run_rake
}
install_janus
