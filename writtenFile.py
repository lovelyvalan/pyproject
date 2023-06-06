file_name = input("Enter tehe file name : ")
f = open(file_name, 'w')

i = 0
while True:
    f.writelines(str(input(':')))
    if i % 100 == 0:
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

