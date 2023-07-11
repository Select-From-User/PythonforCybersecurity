#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created by cory on jul 10

#ask user for their name and age
user_name = input("What is your name? ")
user_age = input("How old are you?")
user_age_num = int(user_age) + 2
#print hello and their name
print(f"Hello {user_name}"f",in 2 years, you will be {user_age_num}")