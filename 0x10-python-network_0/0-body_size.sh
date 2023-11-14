#!/bin/bash
#This script displays the size of the body of the response of a request
#curl -s -I "$1" | grep Content-Length | awk '{print $2}'
curl_status=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 3 http://0.0.0.0:5000/twi?c0=24+91+24+91+24+91+24+91)``
