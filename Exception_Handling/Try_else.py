try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:  # This is executed only if the try was successful
    print("I'm inside else")
