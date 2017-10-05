#!/bin/bash

## If Mac has new mac smell, perform the following

if [ -f "`which brew`" ]
then
  echo "brew installed"
else
  echo "Make sure brew and brew cask are installed and rerun this script."
  echo ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  echo "brew install caskroom/cask/brew-cask"
  exit
fi

brew update

echo "### brew some unix commands"
brew install \
    awscli \
    consul \
    git \
    go \
    graphviz \
    python          \
    python3         \
    terraform \
    vagrant-completion \
    vault

echo "### brew some mac apps (cask)"
brew cask install \
    calibre         \
    colloquy \
    dropbox \
    encryptr        \
    firefox \
    google-chrome   \
    iterm2 \
    kindle          \
    libreoffice     \
    mactex          \
    macvim          \
    nightingale     \
    menumeters      \
    slack \
    textmate        \
    vagrant \
    virtualbox \
    vlc \
    yujitach-menumeters

# Reference
# MenuMeters
# http://www.ragingmenace.com/software/menumeters

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
    backup_previous_install
    clone_janus
  fi
  run_rake
}
install_janus
