file_name = input("Enter tehe file name : ")
f = open(file_name, 'w',newline='')

i = 1
while True:
    s = str(input('write anything here . type stop to exit ! \n'))
    f.writelines(s+'\n')   # + and \n for write a line by line commands
    if s == 'stop':
        break
    if i % 10 == 0:
        op = input("Write more ? [y/n]")
        if op == 'n':
            break
        elif op == 'y':
            op
        else:
            while True:
             if op not in ['y','n'] and op.isalpha():
                print('invalid input please enter y or n !')
             else:
                 break

    i = i + 1


fileName=input("enter the file nam eto append : ")

while True:
    ui=input("Enter line to append : q to quit : ")
    if ui == 'q':
        break
    with open(fileName,'a') as f:
        f.writelines(ui + '\n')
    f.close()


