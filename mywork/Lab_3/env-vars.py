#!/usr/bin/python3

import os

# Step 5: Prompt user for input
USER_NAME = input("Enter your name: Aleeza")
USER_CITY = input("Enter your city: Ashburn")
USER_MAJOR = input("Enter your major: Statistics and Economics")

# Store inputs as environment variables
os.environ["USER_NAME"] = USER_NAME
os.environ["USER_CITY"] = USER_CITY
os.environ["USER_MAJOR"] = USER_MAJOR

# Step 6: Retrieve and print stored environment variables
print("\nStored Environment Variables:")
print("Name:", os.getenv("USER_NAME"))
print("City:", os.getenv("USER_CITY"))
print("Major:", os.getenv("USER_MAJOR"))

