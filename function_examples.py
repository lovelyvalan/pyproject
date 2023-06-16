# 1. add two numbers
def sum(x, y):
    return x + y


s = sum(4, 5)
print(s)


# 2. find average number in lists

# def avg():
#     ls = (1, 2, 3, 4, 5)
#     t = sum(*ls)
#     return (lambda x: x / len(ls))(t)


# a = avg()
# print(a)

def func1(*x):
    for i  in x:
        print(i)

func1(20,40,60)
