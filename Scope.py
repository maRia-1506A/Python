a = 30  # global
b = 50


def func():
    global a
    a = 1  # changing global value

    x = 100  # local
    print(x)
    print("After changing global value, a:", a)


print(a, b)
func()
