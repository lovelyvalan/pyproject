l = ['valan', 'ditto', 'daniel', 'joel', 'jegan']

for i, p in enumerate(l, start=1):  # start is not mandatory
    print(i, p)
    if i == 3:
        break
print('===================')

first = ['one', 'two', 'thre', 'four']

for i, j in enumerate(first, 1):  # the 1 indicate the index starts from 1 not an zero
    print(i, j)
print('===================')

second = ['five', 'six', 'seven', 'eight']

for i, j in enumerate(second, 5):  # here the index starts from 5. or  we can assign start=5
    print(i, j)

'''
enumarate is used for index the value for above example
we don't give an index number for list l
but enumarate gives an index numbers for l 
we can easyly do operations with the index like break the index value of 3 in above

enumerate() Arguments

The enumerate() function takes two arguments:

    iterable - a sequence, an iterator, or objects that support iteration
    start (optional) - enumerate() starts counting from this number. If start is omitted,
     0 is taken as start.


'''
