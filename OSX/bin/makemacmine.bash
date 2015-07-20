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

brew cask install google-chrome
brew cask install calibre
brew cask install kindle
brew cask install  send-to-kindle
brew cask install encryptr
brew cask install textmate
brew cask install vlc

brew install macvim
