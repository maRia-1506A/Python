# multiple inheritance
# class baba:
#     car = 'BMW'
#     home = '10 floor'
#     tk = '1000$'


# class son1:
#     phone = 'Iphone'
#     AC = 'Walton'
#     Microphone = 'Fifine'


# class son2:
#     webcam = 'fifine k0'
#     laptop = 'Walton'
#     camera = 'Fifine'


# class son3(baba, son1, son2):
#     brokenph = ''
#     brokenhm = ''


# k = son3()
# print(k.car)
# print(k.webcam)
# b = baba()


# multilevel inheritance
class baba:
    car = 'BMW'
    home = '10 floor'
    tk = '1000$'


class son1(baba):
    phone = 'Iphone'
    AC = 'Walton'
    Microphone = 'Fifine'


class son2(son1):
    webcam = 'fifine k0'
    laptop = 'Walton'
    camera = 'Fifine'


class son3(son2):
    brokenph = ''
    brokenhm = ''


k = son3()
print(k.car)
print(k.webcam)
b = baba()
