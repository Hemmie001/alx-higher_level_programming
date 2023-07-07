#!/bin/bash
#this script takes in a URL,
#sends a GET request to the URL, 
#and displays the body of the response

#It display only body of a 200 status code response
#It was requested I make use of curl

curl -sL "$1"i
