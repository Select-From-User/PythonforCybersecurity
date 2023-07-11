#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created by cory on jul 10

#ask user for their name
user_name = input("What is your name? ")

#print hello and their name
print("Hello {0}!".format(user_name))
print(f"Hello {user_name}")
print("Hello " + user_name)
print("Hello", user_name)
message = "Hello" + user_name
print(message)
