#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By cory 8/13

#import modules
import hashlib
import requests

#function to check password
def check_haveibeenpwned(sha_prefix):
    pwned_dict = {}
    #perform API request
    request_uri = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get(request_uri)
    #confirm if found
    pwned_list = results.text.split("\r\n")
    for pwnd_pass in pwned_list:
        temp_pass = pwnd_pass.split(":")
        pwned_dict[temp_pass[0]] = temp_pass[1]
    return pwned_dict
#ask for password
new_password = input("What password needs to be checked? ")

#hash the pass
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()

#split password
sha_prefix = hashed_password[0:5]
sha_postfix = hashed_password[5:].upper()


#check password
pwned_dict = check_haveibeenpwned(sha_prefix)
#check results
if sha_postfix in pwned_dict.keys():
    print("password has been compromised {0} times".format(pwned_dict[sha_postfix]))
else:
    print("Password has not been found, it is safe to use")