file_name = input("Enter a filename or path to read a file : ")
f = open(file_name, 'r')
i = 0
line = f.readline()
while line:
    line = f.readline()
    print(line, end=',')
    print(line.split(','))

    if i % 1000 == 0:
        op = print("Read more? [n]")
        if op == 'n':
            print('exiting')
            break
    i = i + 1

