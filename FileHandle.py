# delete file
# import os
# os.remove("FileText1.html")

# delete folder
# os.rmdir("lalalalal")

FILE = open("FileText.txt", "r")
# print(FILE.read()) we can print the lines


# Read all lines from the file at once and returns a list of strings.
f = FILE.readlines()
print(f, type(f))
FILE.close()

FILE1 = open("FileText1.html", "a")
FILE1.write("I am Zannatul\n")
FILE1.write("I am Farzana\n")
FILE1.write("I am maria\n")
FILE1.write("I am a BSc student\n")
FILE1.close()
