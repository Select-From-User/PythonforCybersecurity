#!/usr/bin/env python3
# First example of pinging from Python
# By cory on jul 11
#

import os
import platform

#assign ip to variable  
ip_address = "127.0.0.1"
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
#print out results
print(exit_code)