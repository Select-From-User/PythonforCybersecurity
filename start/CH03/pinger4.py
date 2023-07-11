#!/usr/bin/env python3
# First example of pinging from Python
# By cory on jul 11
#

import os
import platform

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

#assign ip to variable  
ip_prefix = "127.0.0."
#create for loop 1-255
for octet in range(255):
    #setup ip address
    ip_address = ip_prefix + str(octet + 1)

    #call function
    result = ping_address(ip_address)
   
    #print out results
    if result:
        print(f"{ip_address} is online") 