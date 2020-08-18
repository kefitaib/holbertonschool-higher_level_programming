#!/bin/bash
# displays only the status code of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
