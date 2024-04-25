#!/bin/bash
# Sends JSON POST request to URL and displays thes body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
