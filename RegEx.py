import re
text1 = "The rain in Spain"
pattern1 = "[a-m]"  # set of characters
result1 = re.findall(pattern1, text1)
print(result1)

text2 = "1 is the special character"
pattern2 = "^1"  # starts with
result2 = re.findall(pattern2, text2)
if result2:
    print("yes, 1 is a special character")
else:
    print("no, 1 is not a special character")

text3 = "1 is the special character"
pattern3 = "special$"  # ends with
result3 = re.findall(pattern3, text3)
if result3:
    print("yes, we find special character")
else:
    print("no, we didn't find special character")
