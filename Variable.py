a = 85  # global varibale


def func():
    # a = 3  # local varibale
    global a
    a = 3  # here global a(85) is changed by global keyword
    print(a)


func()
print(a)
