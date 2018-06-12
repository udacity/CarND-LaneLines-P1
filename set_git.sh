#!/bin/bash

# Ask the user for login details
read -p 'Git repository url: ' upstreamVar
read -p 'Git Username: ' userVar
read -p 'Git email: ' emailVar

echo
echo Thankyou $userVar, we now have your credentials
echo for upstream $upstreamVar. You must supply your password for each push.
echo

echo setting up git

git config --global user.name $userVar
git config --global user.email $emailVar
git remote set-url origin $upstreamVar
echo

echo Please verify remote:
git remote -v
echo

echo Please verify credentials:
echo username: git config user.name
echo email git config user.email