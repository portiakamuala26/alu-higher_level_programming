#!/bin/bash
# Displays the HTTP methods accepted by a server
curl -s -I -X OPTIONS "$1" | grep Allow | cut -d' ' -f2-
