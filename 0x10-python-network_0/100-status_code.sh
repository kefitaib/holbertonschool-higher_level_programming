#!/bin/bash
# displays only the status code of the response
curl -sL -w "%{http_code}" -I "$1" -o /dev/null
