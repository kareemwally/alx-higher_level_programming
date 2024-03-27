#!/bin/bash
# a script to show available options
curl -sI "$1" | grep -i "Allow" | awk '{$2}'
