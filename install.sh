#!/bin/bash

# init git submodules
./init-submodule.sh

# pip-install required modules
pip install -r requirements.txt

# install Openscad using git submodule
./ubuntu-essentials-install/appinstall/3Dprint/openscad/install.sh