#from https://github.com/Aradhya-Tripathi/fire-watch

#!bin/bash

error="\e[1;31m[ERROR]\e[0m"
execution="\e[0;36m[INFO]\e[0m"

echo -e "$execution [...]"


var=$(black server/ --diff | grep " " -c)
echo $var

if [ $var -eq 0 ];
then
    echo "$execution Server All clean!"
else
    black server/ --diff
    exit 1
fi

var=$(black ml/ --diff | grep " " -c)
echo $var

if [ $var -eq 0 ];
then
    echo "$execution ML All clean!"
else
    black ml/ --diff
    exit 1
fi
