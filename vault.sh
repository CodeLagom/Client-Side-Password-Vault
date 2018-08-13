#! /bin/bash

pathv=$(pwd)/$line
main_t="main.py"
pathv="$pathv$main_t"
echo $pathv
cd ~
echo "Setup Complete"
echo -e "Command is 'vault'"
echo "Bash Restarting"
echo -e "alias vault='python3 $pathv'" >> .bashrc
exec bash
