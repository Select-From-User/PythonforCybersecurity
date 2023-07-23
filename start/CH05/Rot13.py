#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By cory 7/23

#asking for message
source_message = input("What is your message? ")
#change message to lower case
source_message = source_message.lower()
final_message = "" 

#loop through each letters
for letter in source_message:
    #covert letter to number
    ascii_number = ord(letter)
    #check if letter is between a-z
    if ascii_number >= 97 and ascii_number <= 122:
        #add 13 to number
        ascii_number += 13
        #check if still a letter. if not, subtract 26
        if ascii_number > 122:
            ascii_number -= 26
    final_message = final_message + chr(ascii_number)
#print out message
print(final_message)