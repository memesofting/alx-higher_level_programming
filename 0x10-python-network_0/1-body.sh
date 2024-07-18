#!/bin/bash
# Script sends a GET request to a url and displays size of the body of the response
curl -s -w "200" "$1" | wc -c
