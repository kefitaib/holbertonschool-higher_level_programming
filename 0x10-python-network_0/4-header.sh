#!/bin/bash
# takes in a URL , sends a GET request and displays the body of the response
curl "$1" -X GET -d "X-HolbertonSchool-User-Id=98"
