#!/bin/bash
# displays only the status code of the response
curl -X POST -H "Content-Type: application/json" -d @"$2" + ".json" "$1"
