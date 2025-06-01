# Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt", "r") as f:
    file = f.read()

if ("python" in file):
    print("Yes, Python contains in the file")
else:
    print("No, Python doesn't contain in the file")
