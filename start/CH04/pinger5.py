#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By cory 7/22

import os
import platform
dir_path = os.path.dirname(os.path.realpath(__file__))

def ping_address(ip_address):
     #find our os
    current_os = platform.system().lower()
    if current_os == "windows":
        #build ping command if windows
        ping_cmd = f"ping -n 1 -w 1000 {ip_address}"
    else:
        #build our ping command if linux
        ping_cmd = f"ping -c 1 -w 1 {ip_address} > /dev/null 2>&1"
        #execute the ping command
    exit_code = os.system(ping_cmd)
    if exit_code == 0:
        return True
    return False

#open file
f = open(dir_path + "/ips.txt", "r")
#read file
ip_addresses = f.readlines()
#close file
f.close
#loop results
for ip_address in ip_addresses:
    #clean up address
    ip_address = ip_address.strip()
    #call function
    result = ping_address(ip_address)
   
    #print out results
    if result:
        print(f"{ip_address} is online") 