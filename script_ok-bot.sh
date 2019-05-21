#!/bin/bash

# install pip
sudo apt update
sudo apt install python3-pip

# install mariadb
sudo apt install mariadb-server

# install git and clone project
sudo apt-get install git 
git clone https://github.com/Haikouhi/ok-bot.git
cd ok-bot

# install, create virtual env and activate it
pip install virtualenv
virtualenv -p python3 venv
cd venv
source bin/activate
cd ..

# install requirements
pip3 install -r "requirements.txt"

