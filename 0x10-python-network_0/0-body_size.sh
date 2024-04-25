#!/bin/bash
# takes URL sends requiest and displays size of body
curl -sI "${1}" | grep "Content-Length" | cut -c 17-
