#!/usr/bin/python3

import os

# Step 5: Prompt user for input
USER_NAME = input("Enter your name: ")
USER_CITY = input("Enter your city: ")
USER_MAJOR = input("Enter your major: ")

# Store inputs in a dictionary (not as environment variables)
user_info = {
    "USER_NAME": USER_NAME,
    "USER_CITY": USER_CITY,
    "USER_MAJOR": USER_MAJOR
}

# Step 6: Retrieve and print stored values
print("\nStored Information:")
print("Name:", user_info["USER_NAME"])
print("City:", user_info["USER_CITY"])
print("Major:", user_info["USER_MAJOR"])

