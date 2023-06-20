#!/bin/bash

apt-get -q -y update
apt-get -q -y install wget
apt-get -q -y install unzip

# install google chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
apt --fix-broken -y install

# install chromedriver
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
