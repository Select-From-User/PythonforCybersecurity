import hashlib
import requests
import tkinter as tk
from tkinter import messagebox

# Function to check password
def check_password():
    new_password = password_entry.get()
    encoded_password = new_password.encode()
    digest_password = hashlib.sha1(encoded_password)
    hashed_password = digest_password.hexdigest()

    sha_prefix = hashed_password[:5]
    sha_postfix = hashed_password[5:].upper()

    pwned_dict = check_haveibeenpwned(sha_prefix)

    if sha_postfix in pwned_dict.keys():
        message = f"Password has been compromised {pwned_dict[sha_postfix]} times."
    else:
        message = "Password has not been found, it is safe to use."

    messagebox.showinfo("Password Check Result", message)

# Function to check with Have I Been Pwned API
def check_haveibeenpwned(sha_prefix):
    pwned_dict = {}
    request_uri = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get(request_uri)
    pwned_list = results.text.split("\r\n")
    for pwnd_pass in pwned_list:
        temp_pass = pwnd_pass.split(":")
        pwned_dict[temp_pass[0]] = temp_pass[1]
    return pwned_dict

# Create the main application window with the name 'my_window'
my_window = tk.Tk()
my_window.title("Password Checker")

# Create a label
label = tk.Label(my_window, text="Enter the password to check:")
label.pack()

# Create a text entry widget
password_entry = tk.Entry(my_window)
password_entry.pack()

check_button = tk.Button(my_window, text="Check Password", command=check_password)
check_button.pack()

my_window.mainloop()
