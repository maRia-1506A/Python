# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open("poems.txt") as f:
    content = f.read()
    if ("twinkle" in content):
        print("twinkle is present in the content")
    else:
        print("twinkle is not present in the content")
