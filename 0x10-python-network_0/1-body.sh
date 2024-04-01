#!/bin/bash
#getting a body of http
curl -s "$1" | grep -oP '(?<=<body>).*?(?=</body>)'
