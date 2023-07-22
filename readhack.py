#read file for assignment

#open file
f = open("hackme.txt", "r")

#read file and print
contents = f.read()
print("Here is someone to hack - information")
print(contents)

#close file
f.close()