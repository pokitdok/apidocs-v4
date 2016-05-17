#!/bin/bash

# install pip if need be
which_pip=$(which pip)
if [ ${#which_pip} -lt 1 ];then
    sudo easy_install pip
fi

# python aws accessor for deployment
sudo pip install boto3 --ignore-installed six
sudo pip install requests

# install bundler if need be
which_bundle=$(which bundle)
if [ ${#which_bundle} -lt 1 ];then
    sudo gem install bundler
fi

# bundle install dependencies
bundle install