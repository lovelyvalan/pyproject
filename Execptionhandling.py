import os
import sys

a = 5
b = [1, 2, 0, 4]
c = 2


def devide(a, b):
    if b == 0:
        raise ZeroDivisionError("values cant devided by zero")


try:
    devide(100, b[2])
except (NameError, IndentationError, IndexError, ZeroDivisionError, SyntaxError, KeyError, ValueError) as e:
    print("some error happened: {}".format(e))
    print(e)
except Exception as e:
    print("something happened {} ".format(e))
    print("error : {}".format(sys.exc_info()))
else:
    print("else :is all of the excepts wont work then this statement prints ")
finally:
    print("whatever the case i will work")

# Exception handling must be include these things

"""
1 . try   --> try to execute the code

2. except  -->  when errror is occured the except prints the error or we can assigned what error is occured

3. else   -->  if any errors not occured then else statement works

4. finally  --> if any errors occured or not the finally code works. it works all the time 


# execption handling is not for handle mistakes in our code
# it is also handle the user makes an error
# its handle the errors not in our mistake codes  

"""


