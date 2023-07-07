#!/bin/bash
#this script displays the size of the body of the response of a request
curl -sI "$1" | grep Content-Length | awk '{print $2}'
