# while loop

# will execute again and again untill the condition become false
# while is designed to deal with raw thongs . it's all about do manually
# do arithmetic operations with while loop

var = 10
while var <= 10 and var >= 0 :
    print('# {} hello world'.format(var))
    var = var - 1
print("loop completed")


# for loop
# for loop  is designed to deal with structured data types

for i in [1,2,3]: # here list is used. only here iterable things be used
    print(i)


f = {"apple","orange","banana"}

for b in list(f):
    print("i am eating {}".format(b))   # here b is assigned for each time it prints


# range function
# range is functon. format start , stop
print(list(range(50,100,2)))

# break is a keyword which can be used on an if condition inside while or for break the loop

for i in range(0,10):
    if i == 5:
        break
    print(i)

# continue

# continue will cut the loop
# continue stop the current loop and move on to the next item


for i in range(0,100):
    if  i % 2 ==0: #this condition was skipped.actually it prints even number but continue is skip that condition
        continue
    else:
        print("# {} this is odd number ".format(i))

print("loop completed")

# what condition is giving in loop the continue keyword is skip that particular condtion. above exampke





# enumarate()

l = ["apple","banana","orange","grape"]
e = enumerate(l)    #  this is must for enumarate

# for i,v in e:
#     print("# {} {}".format(i,v))

for j in range(len(l)):
    print(e.__next__())


# presss ctrl+/ to make an comment for selectec items
