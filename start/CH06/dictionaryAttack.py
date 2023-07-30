#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By cory on 7/29

#import modules
import crypt
import os
#function to test password
def test_password(algorithm_salt, hashed_password, password_guess):
    #use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)
    #compare salted guess against hashed pass
    if hashed_guess == hashed_password:
        return True
    return False
    
#load a dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/top10.txt", "r")
passwords = f.readlines()

#prompt user for algorithm/salt
algorithm_salt = input("what is the algorithm and salt? ")
#prompt user for salted hash
hashed_password = input("what is the full hashed password? ")
#loop through each password

for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("match found: {0}".format(password))
        break