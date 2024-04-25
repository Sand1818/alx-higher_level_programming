#!/bin/bash
# Displays all HTTP methods server will accept
curl -si -X OPTIONS   "${1}" | grep "Allow" | cut -c 8-
