import pyfiglet
import random
# titile keyword is used for capitalize every statements
def fatherwish():
    msg = 'happy fathers day !'.title()
    fonts=pyfiglet.FigletFont.getFonts()
    selfont=random.choice(fonts)
    asciiart=pyfiglet.figlet_format(msg,font=selfont)
    return asciiart

fw=fatherwish()
print(fw)