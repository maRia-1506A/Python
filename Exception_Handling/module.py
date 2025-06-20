def myFunc():
    print("hello world")


if __name__ == "__main__":
    # if the code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)  # Output: __main__ (the code is run directly by its own file)
