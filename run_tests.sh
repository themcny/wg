#!/bin/bash
echo "~~~ Intalling Dependencies ~~~"
pip install -r requirements.txt

echo "~~~ Running test_utils ~~~"
python3 test_utils.py
