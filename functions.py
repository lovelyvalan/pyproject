# Functions

"""
function is group of instructions given to a computer to do meaningful task
function key word is def
format : def add():
            <code>
"""

print('FUNCTIONS     THE GROUP OF TASK')


def add(k, x, y):
    a = x + y
    s = x - y
    m = x * y
    d = x / y
    print(k)
    print(x)
    print(y)
    return {
        "add": a,
        "sub": s,
        "multi": m,
        "div": d,
    }


q = int(input("Enter num 1 : "))
w = int(input("Enter num 2 : "))

obforadd = add(9, y=q, x=w)  # this is an keyword arguments

print("math operations for {} and {} is {} , ".format(q, w, obforadd))

for i, j in obforadd.items():  # this is the best way to iterate dictionary
    print(i, j)

print('===========================')

# some pack unpack
a = 1
b = 2
c = 3
l = [a, b, c]
n, v, k = l
print(n)
print(v)
print(k)

print('============================')

print('POSITIONAL ARGUMENTS')


def jumma(*y):
    x = 0
    print(x)
    print(y)
    a = 0  # a = 0
    a = a + x  # a = 0 + 0 = 0 , a = 0
    for i in y:
        a = a + i  # 0= 0 +1   1= 1+ 2   3 = 3+ 3   6= 6 + 4   10 = 10 + 5  = 15
    return a  # a =1 5


print("add results {}".format(jumma(1, 2, 3, 4, 5)))

# outcomes

"""
1. calling functions with parameters (positional arguments)

2 . calling function with keyword argumentrs
         def add(x,y)
         a=input('num1 :')
         b=input('num2 :')
         ob= add(x=a,y=b)   # here we call a,b normally but keyword arg is specify values for that keywords

3. variable number of positional arguments
    
    def sub(x,*y)
        
    sub(1,2,3,4,5) # here 1 is goes for x and 2,3,4,5 goes for y 
                   # but cannot assign *x . it will rase error     

4. number of varibable arguments

        def all_args(x,*y,t=20,**kwargs):
            print('x',x)           
            print('y',y)           
            print('t',t)           
            print('kwargs',kwargs)           

        all_args(1, 2, 3, 4, 5, 6, 77, 8, a=10, b=20, c=30, d=40)
        # here 1 goes for x
        #  2,3,4,5,6,77 goes for *y
        # 8 goes for t
        # a,b,c,d goes for *kwargs
        
        
        # * is for variable number of positional arguments
        # ** is for number of variable arguments
        
"""
print('=============================')
print('number of varibable arguments  and all arguments : '.upper())


def vargs(q, w, e, r, *y, t=20, **kwargs):  # this format is rule by default # the format is
    # positional args,no. of positional args,ordinary kwargs,then real kwargs
    print('q:', q)
    print('w:', w)
    print('e:', e)
    print('r:', r)
    print('t:', t)
    print('y:', y)
    print('kwargs:', kwargs, '# kwargs stands for keyword arguments by default')


vargs(1, 2, 3, 4, 5, 6, 77, 8, a=10, b=20, c=30, d=40)

print('=======================')

print('SWAPPING VIA FUNCTIONS')


def swap(x, y):  # here args are tuple    # x,y = y,x
    return y, x  # here also tuple so packing and unpacking is done here


x = 1
y = 2
v = swap(x, y)
print(v)


def all_args(x, *y, t=20, **kwargs):
    print('x', x)
    print('y', y)
    print('t', t)
    print('kwargs', kwargs)


all_args(1, 2, 3, 4, 5, 6, 77, 8, a=10, b=20, c=30, d=40)

print('========================================')

#  SCOPES    global variable set
print('SCOPES ....   global variable set')

x = 7


def xforfunc(num):
    x = num
    print(x)


def xforglobal(num2):
    global x
    x = num2
    print(x)
    print(x)


print(x)
xforfunc(20)
print(x)
xforglobal(30)
print(x)


def xforafterglobal():
    print('xafterglobal is :', x)


xforafterglobal()

print('=============================')
print('FIRST CLASS FUNCTIONS : ')
print('\nfirst class functions are looks like a class so its called 1st class functions\n'.upper())


def firstfunc(c):
    def secfunc(y, z):
        print(z)
        return c + y

    def thrdfunc(y):
        return c - y

    def frthfunc(y):
        def subfunc(v):
            return v / y

        def subfun2(v):
            return v * y

        return c * y, subfunc(12), subfun2(4)

    return secfunc, thrdfunc, frthfunc,


two, three, four = firstfunc(10)  # here two is the instance variable for secfunc,and three is for thrdfunc
print(two(5, 2))
print(three(8))
print(four(6))

"""
FIRST CLASS FUNCTION 

1. firstfunc is the main function
2. secfunc is the nested function of firstfunc 
3. thrdfunc is the nested function of firstfunc
4. frthfunc is the nested function of firstfunc
5. subfunc is nested function for frthfunc

two, three, four = firstfunc(10)

6. two,three,four are instance variable for firstfunc . then 10 is assigned for c

7. print(four(6))  ---> 6 is assigned for frthfunc(y)  
8. there is subfunc has argument 12 for parameter v 

"""

print('==================================')
print('LAMBDA FUNCTIONS')
print('lamda is the nameless function'.upper())
print('lambda function is the annonymous function it cant be callable...'.upper())
print('')

'''
lambda function only give an result 
it can't be used in other plces
cannot assighn a variable fo that function thats why it is called annonymous function  
'''

l = [10, 20, 30, 40]
print(list(map(lambda x: x + 10, l)))  # here 'l' contains list of valuse all thats considered as x

print('MAP')
print('map is the function take function and list of items for iterable . format (func,iterables)'.upper())


def formap(x):
    return (lambda y: y + x), (lambda y: y - x)  # lambda is a function .this is best.but it wont callable


f, d = formap(4)
print(f(10))
print(d(40))

#  we can do normally

l = [20, 30, 40]
for b in l:
    print(f(b))
    print(d(b))

"""
lambda is the function is simplyfy the code also
main purpose is one time code we cant call it form other functions
format (lambda x : x + 10 )(5)  # here 5 for x 

"""
"""
map is the function it is iterate the values for given function
it is also simplify the code 
format map(function,iterable_list/etc..)
"""
print('-====-')


def globalvalue():
    global sets
    sets = [10, 20, 30, 40, 50,100,101]
    return sets


def forall(x):
    return list(map(lambda y: y + x, sets))


print('g is ', globalvalue())

d = forall(3)
print(d)
# print(d(5))


my_lambda = lambda x: [i ** 2 if i % 2 == 0 else i ** 3 for i in range(x)]
d = my_lambda(10)
print(d)

print(list(filter((lambda x: x <= 100), sets)))

