#!/bin/bash
# displays only the status code of the response
curl -sL -w "%{http_code}" -I "www.google.com" -o /dev/null
