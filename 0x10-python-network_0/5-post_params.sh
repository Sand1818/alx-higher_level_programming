#!/bin/bash
# Takes in URL, sends a POST request and displays the body of the response
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
