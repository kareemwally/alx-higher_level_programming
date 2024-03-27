#!/bin/bash
# Send a cURL request and store the response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$url"

# Get the size of the response body in bytes
response_size=$(wc -c < "$response_file")

# Display the size
echo "$response_size"

# Clean up the temporary file
rm "$response_file"
