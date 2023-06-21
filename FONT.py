import pyfiglet
import random
# title keyword is used for capitalize every statements
def fatherwish(func):
    def secfunc(*args,**kwargs):
        fonts=pyfiglet.FigletFont.getFonts()
        selfont=random.choice(fonts)
        asciiart=pyfiglet.figlet_format(func(*args,**kwargs),font=selfont)
        return asciiart
    return secfunc
@fatherwish
def fordec():
    fw = (str(input('enter your/any name : ')))
    return fw

fd = fordec()
print(fd)


'''
decorators and yield is just like same
yield is create at the instance
decorate modify the values
just similar not an exact same
'''
