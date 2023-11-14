#!/bin/bash
#kl;kjl;kj
curl --write-out %{http_code} --silent --output /dev/null ${URL}
