#!/bin/bash
echo "~~~ Intalling Dependencies ~~~"
pip install -r requirements.txt

echo -n "Enter the path for the file system you wish to explore:"
read path

read -p "Do you want to run the Flask app now? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

echo "~~~ Running Flask App ~~~"
flask --app "api:create_app(\"$path\")" run
