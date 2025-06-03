# Write a program to find out the line number where python is present from ques 6
with open("log.txt", "r") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if ("python" in line.lower()):
        print(f"Yes, python is found at line {lineNo}")
        break
    lineNo += 1
else:
    print("No, python is not found")
