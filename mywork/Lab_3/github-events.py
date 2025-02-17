#!/usr/bin/python3

import os
import json
import requests

# Retrieve GitHub username from environment variable
GHUSER = os.getenv('GITHUB_USER')

# Check if GHUSER is set
if GHUSER is None:
    print("Error: GITHUB_USER environment variable is not set.")
    exit(1)

# Construct the GitHub API URL
url = f'https://api.github.com/users/{GHUSER}/events'

# Fetch data from the API
response = requests.get(url)
r = json.loads(response.text)

# Print the first five GitHub events
for x in r[:5]:
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)

