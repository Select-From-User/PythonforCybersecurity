#write file for assignment

#open file for writing

f = open("hackme.txt", "w")

#input variables

q1 = input("What is your name? ")
q2 = input("What is your favorite color? ")
q3 = input("What is your first pet's name? ")
q4 = input("What is your mother's maiden name? ")
q5 = input("What elementary school did you attend? ")

#write to file

f.write(f"{q1}\n")
f.write(f"{q2}\n")
f.write(f"{q3}\n")
f.write(f"{q4}\n")
f.write(f"{q5}\n")

#close file
f.close()