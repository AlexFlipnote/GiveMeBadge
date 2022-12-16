#!/bin/bash

# This script will run the python script that will run the program
# It will also check if python is installed and if it is in PATH
# If it is not, it will tell you to install it and put it in PATH
# If you already have it installed, you might have forgotten to put it in PATH

if !command -v python3 &> /dev/null; then
    printf "\033[1;31mpython3 is not found in path!\033[0m\n\n"
    
    echo You might need to install python first!
    echo https://www.python.org/downloads/
    echo 
    echo If you do already have it installed, you might have forgotten to put it in PATH
    echo Reinstall it and make sure to check the box that says \"Add Python to PATH\"
    echo

    # "read" and "exit" are used to make sure that you are able to
    # read the message before the window closes
    read -p "Press any key to continue . . ."
    exit
fi

python3 index.py

# Exit once python script has been terminated
exit