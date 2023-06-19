print('YIELD')


def foryield(values):
    for i in values:
        print(f'valaue before multiply {i}')
        yield i * 2


for i in foryield(list(range(1001))):
    print(i)

print('==============================================')


def forreturn(values2):
    l = []
    for i in values2:
        l.append(i*2)
        print(f'values in return function {i}')
    return l


for i in forreturn(range(1001)):
    print(i)
