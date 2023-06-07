# Functions

"""
function is group of instructions given to a computer to do meaningful task
function key word is def
format : def add():
            <code>
"""


def add(x, y):
    a = x + y
    s = x - y
    m = x * y
    d = x / y
    return {
        "add": a,
        "sub": s,
        "multi": m,
        "div": d,
    }


q = int(input("Enter num 1 : "))
w = int(input("Enter num 2 : "))
obforadd = add(x=q, y=w)  # this is an keyword arguments
print("math operations for {} and {} is {} , ".format(q, w, obforadd))

for i, j in obforadd.items():  # this is the best way to iterate dictionary
    print(i, j)

# some pack unpack
a = 1
b = 2
c = 3
l = [a, b, c]
n, v, k = l
print(n)
print(v)
print(k)


def jumma(*y):
    x = 0
    print(x)
    print(y)
    a = 0           # a = 0
    a = a + x       # a = 0 + 0 = 0 , a = 0
    for i in y:
        a = a + i    # 0= 0 +1   1= 1+ 2   3 = 3+ 3   6= 6 + 4   10 = 10 + 5  = 15
    return  a        # a =1 5

print("add results {}".format(jumma(1 ,2,3,4,5)))


# last video time 1:13:**