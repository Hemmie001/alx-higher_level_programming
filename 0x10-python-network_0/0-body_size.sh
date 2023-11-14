#!/bin/bash
# displays only the status code of the response.
#curl -so /dev/null -w "%{http_code}" "$1"
#curl --write-out "%{http_code}" --silent --output /dev/null "$1"
curl --write-out %{http_code} --silent --output /dev/null ${URL}
