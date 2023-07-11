#!/usr/bin/env python3
# First example of pinging from Python
# By cory on jul 11
#

import os

#assign ip to variable  
ip_address = "8.8.8.8"
#build our ping command
ping_cmd = f"ping -c 1 -w 1 {ip_address} > /dev/null 2>&1"
#execute the ping command
exit_code = os.system(ping_cmd)
#print out results
print(exit_code)