#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS google.com -i | grep Allow: | cut -d':' -f2
