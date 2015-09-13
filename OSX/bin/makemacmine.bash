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

brew cask install calibre
brew cask install encryptr
brew cask install google-chrome
brew cask install kindle
brew cask install libreoffice  # productivity
brew cask install nightingale  # music player
brew cask install menumeters   # ref below
brew cask install send-to-kindle
brew cask install textmate
brew cask install vlc

# UNIX Tools
brew install macvim


# Some PIP

# install AWS Command Line Tools
sudo pip install awscli


# Reference
# MenuMeters
# http://www.ragingmenace.com/software/menumeters
