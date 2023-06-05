# iter () --> make an iterator out of an iterable data types
import sys

# next () --> return the next in list


l = [ 1,2,3,4,5,6,]
l=iter(l)

try:
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
except Exception as e:
    print("error occured {}".format(sys.exc_info()))
    print("Enter correct amount of print statements")


d = {1 : 'one',2:'two'}

for i in iter(d.items()):
    print(i)