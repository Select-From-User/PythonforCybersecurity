#!/usr/bin/env python3
# Sample script that writes to a file
# By cory 7/22/23

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
#open file for writing

f = open(dir_path + "/testfile.txt", "w")

#write to the file
print("hello world")
f.write("hello world\n")
f.write("hello world\n")
f.write("hello world\n")
#close the file
f.close()

