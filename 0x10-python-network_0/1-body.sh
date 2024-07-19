#!/bin/bash
# Script sends a GET request to a url and displays size of the body of 200 status code response
curl -s -o >(cat) -w "%{http_code}" "$1" | { read -r status; [ "$status" -eq 200 ] && cat; }
