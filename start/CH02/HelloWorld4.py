#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created by cory on jul 10

#ask user for their name and age
user_name = input("What is your name? ")
user_age = input("How old are you?")
user_age_num = int(user_age)
#print hello and their name
print(f"Hello {user_name}, in 2 years, you will be "(user_age_num+2))