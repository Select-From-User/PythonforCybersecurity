import crypt
import os

# Function to test password
def test_password(hashed_password, password_guess):
    # Use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, hashed_password[:hashed_password.rfind("$")])
    # Compare salted guess against hashed pass
    if hashed_guess == hashed_password:
        return True
    return False

# Load a dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/top 10 million.txt", "r")
passwords = f.readlines()
f.close()

# Load a hash file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/shadow", "r")
hash_entries = f.readlines()
f.close()

# Extract hashed passwords from each hash entry in the "shadow.txt" file
hashed_passwords = [entry.strip().split(":")[1] for entry in hash_entries]

# Loop through each hashed password and test against the passwords
for hashed_password in hashed_passwords:
    # Loop through each password
    for password in passwords:
        password = password.strip()
        result = test_password(hashed_password, password)
        if result:
            print("Match found: {0}".format(password))
            break