print('================================')
print('MODULES')

'''
1 . modules are include functions , classes , globals
        inbuiltfunctions    userdefinefunctions

2 . inbuilt modules and user define modules 

3 .  
'''
import img2pdf
print(dir(img2pdf))


'''
if pyprojecr is a module that must have a __init__.py  

from . import 'some variable or function'

 above line . indicates the __init__.py 
 
 then we can import function even variable can be called inside the module
 
'''
# from foldername.filename import classname/func/var
# is there no init file in it , that's not a module

print('================================')
print('CREATE A MODULE')

'''
when you create a python package in new
it means you create a python module
belove codes are represent it
'''

from newmodule import kuku , audible  # here newmodule is a python package .it has a kuku.py and audible.py

kuku.kukufm()
audible.audibleapp()


'''
echo $path
create a bin folder 
PATH=$PATH:/home/valan/Desktop/bin
nano .bashrc
PATH=$PATH://home/valan/Desktop/bin  

if you want to remove it clear this line (/home/valan/Desktop/bin) from PATH

'''

