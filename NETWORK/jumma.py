import sys

print('the lenght of arg is ',len(sys.argv))
print('name of the program',sys.argv[0])

a = int(sys.argv[1])
b = int(sys.argv[2])
c= a + b
print('sum of a,b is ',c)

print('program started')
def main():
    print('this is the main function')

def demo():
    print('this is demo function')
def juma():
    print('this is juma fucntion')

if __name__=="__main__":
    main()
    demo()
    juma()