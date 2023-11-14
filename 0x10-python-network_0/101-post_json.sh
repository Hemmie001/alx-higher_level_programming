#!/bin/bash
#This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -X POST -H "content_Type: application/json" -d @"$2" "$1"
