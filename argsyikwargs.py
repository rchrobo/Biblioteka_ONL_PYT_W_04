def funk(*args):
    print(type(args), args)


def funk2(a, b, c):
    print(a, b, c)


def funk3(a, b, *args):
    print(a, b, args)


x = [1, 2, 3]


# funk2(*x)

# funk3(*x)


def funk5(**kwargs):
    print(type(kwargs), kwargs)


funk5(a=1, b=2, c=3)


def funk6(a, b, c):
    print(a, b, c)


s = {'a': 1, 'b': 2, 'c': 3}

funk6(*s)

def funkcja(**kwargs):
    for item in kwargs:
        print (f"wartość w słowniku pod kuczem {item} to {kwargs[item]}")



funkcja(slawek="jest super")








