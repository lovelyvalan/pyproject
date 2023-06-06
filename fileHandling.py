file_name = input("Enter your file name : ")  # this is the user input file
f = open(file_name, 'r')  # here 'r' for open a file in read mode
# print(f.readline())             # this is for common read option
# f.close()                       # if ant file is open t will must be closed .that was done here
# i = 0
# while i < 10:
#     print(f.readline())           # readline oly print one line but here we used a loop for print
#     i = i + 1                     # readline at 10 time  so file output show only 10 lines

i = 0
line = f.readline()   # here empty line is stored in an line
while line:           # the loop will continue to execute as long as the variable `line` is not empty or `None`
    line = f.readline()
    print(line)
    if i % 1000 == 0:
        op = input('read more 1000 ? [y/n]:')
        if op == 'n':
            break
        if op == 'y':
            op
        else:
            while True:
                u_i = input('read more 1000 ? [y/n]:')
                if u_i.lower() not in ['y','n'] and u_i.isalpha():
                    print("invalid input ...please Enter 'y'or'n'")
                else:
                    break


    i = i+1
