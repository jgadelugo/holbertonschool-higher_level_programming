#!/bin/bash
# uses curl to display all HTTP methods server will accept
curl -sI "$@" | grep -i Allow | awk '{print $2, $3, $4}'
