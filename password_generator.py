#import modules
import hashlib
import requests
import secrets
import string

#define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars
#identify length
pwd_length = int(input("Choose password length: "))

#create password
pwd = ''

for i in range(pwd_length):
    pwd += str(''.join(secrets.choice(alphabet)))

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
#assign the password to checker
new_password = pwd

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
    print("password: " + new_password)
    print("has not been found, it is safe to use")