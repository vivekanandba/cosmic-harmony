#!/bin/bash -x 
sudo apt install python3-pip
python3.10 -m pip install virtualenv
# python3.8 -m virtualenv .venv -p /usr/bin/python3.8
# python3.8 -m virtualenv .venv -p ~/.pyenv/versions/3.8.9/bin/python
python3.10 -m virtualenv .venv
. .venv/bin/activate
