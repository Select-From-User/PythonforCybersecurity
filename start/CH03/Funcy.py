#!/usr/bin/env python3
# example workign with Functions
#By cory on jul 11

#my function
def print_me(my_message):
    print(my_message)
    return "it worked"

def say_hello(num_times):
        for x in range(num_times):
            print("hello world")

#calling the function
print_me("this is a function")
result = print_me("this is another funtion with return value")
print(result)
say_hello(3)