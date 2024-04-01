#!/usr/bin/python3
"""a script to make post data into url using urllib module"""
import sys
import urllib.parse
import urllib.request


def send_post_request(url, email):
    try:
        # Encode the email parameter
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data, method='POST')  # Specify method='POST'
        # Create a POST request
        with urllib.request.urlopen(req) as response:
            # Read the response body and decode it
            response_body = response.read().decode('utf-8')
            print(response_body)  # Print the response body
    except urllib.error.HTTPError as e:
        print("HTTP Error: {0}, {1}".format(e.code, e.reason))
    except urllib.error.URLError as e:
        print("URL Error: {0}".format(e.reason))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
