#!/bin/bash
# Script sends a request to a url and displays size of the body of the response
curl -s "$1" | wc -c
