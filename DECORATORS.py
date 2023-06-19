# from functools import wraps
lang = 'hi'
translation = {
    'samosa_buy': {
        'ta': 'samosa vaangi tharuviya',
        'en': 'can you buy me a samosa',
        'hi': 'ena katha nu therila'
    }
}


def valanhr(func):
    global lang
    def fsstdec(*args, **kwargs):
        msg = func(*args, **kwargs)
        return translation[msg][lang]

    return fsstdec()


@valanhr
def xyz():
    msg = "samosa_buy"
    return msg


print(xyz)

print('====================')

whencalled = {'third': {
    '1st': '1st dictionary',
    '2nd': '2nd dictionary',
    '3rd': '3rd dictionary'
}}


def secfunc(forfunc):
    def wrapper(*args, **kwargs):
        third, ls, printing = forfunc(*args, **kwargs)
        this= whencalled[third][ls],printing
        return this
    return wrapper()


@secfunc
def forcall(ls='1st'):
    printing = 'this is now printedd'
    third = 'third'
    return third, ls, printing


print(forcall)


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)

    return inner


def dollar(func):
    def inner(*args, **kwargs):
        print("$" * 15)
        func(*args, **kwargs)
        print("$" * 15)
        def innerofinner(func):
            print(func)
        #return innerofinner('this is the inner of inner functiion')

    return inner


# @dollar
# @percent
# @star
def printer(msg):
    print(msg)


printer = percent(star(dollar(printer)))
printer(msg="Hello")
