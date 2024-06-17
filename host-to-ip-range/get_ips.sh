#!/bin/bash

# Check if a file containing hostnames is provided as argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file_containing_hostnames>"
    exit 1
fi

# Read hostnames from the file and get their IP addresses
while IFS= read -r hostname; do
    ip=$(host "$hostname" | awk '/has address/ { print $NF }')
    if [ -n "$ip" ]; then
        echo "Hostname: $hostname | IP Address: $ip"
    else
        echo "Failed to resolve IP address for hostname: $hostname"
    fi
done < "$1"
