#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
curl -d "user_id=98" -H "Origin: HolbertonSchool" -sLX put 0.0.0.0:5000/catch_me
