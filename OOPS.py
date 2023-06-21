print('OOPS')
print(' 1 .MODULES')

# modules are aca like gateway,api
# from image_to_ascii import ImageToAscii
#
# ImageToAscii(imagePath='/home/valan/Desktop/pyproject/blackhat.jpg',outputFile="img.txt")
# print(dir())


print('=================')
print(' 2 . CLASS')
'''
# classification is defined as the class
if a rolesroys is an object is under the category of car is a class 
'''


class Car():
    type = 'suv' # class attribute

    def __init__(self, make, model, regno):
        self._make = make
        self.model = model
        self.regno = regno
        self.batt = 0
        if self.type == "suv":
            self.enginepow='98%'
        elif self.type == 'xuv':
            self.enginepow='100%'

    def start(self):
        print('Engine has started')
        print(f'make {self.make} ,model {self.model} ,regno {self.regno} ')
        self.battery()

    def battery(self):
        print(f'battery {self.batt}% ')

    @classmethod
    def get_type(cls):
        g = cls.type
        print(g)

    @classmethod
    def build_cars(cls):
        g = cls('bmw', 'i20', 'tn69')
        g.start()
        return g

    @staticmethod
    def build_cars1():
        cls = Car
        g = cls('benz', 'i30', 'tn69')
        g.start()
        return g

    @property
    def make(self):
        return self._make


    @make.getter
    def make(self):
        print(f'returning {self._make}')
        return self._make

    @make.setter
    def make(self, make):
        print(f'setting {self._make} to {make}')
        self._make = make

    @make.deleter
    def make(self):
        print(f'Deleting..{self._make}')
        del self._make

# NOTES
'''
object is also instance 

if we use @classmethod in before the function the first argument will be a class... example cls...
the argument cls mention the class Car

self is called whithin the function
but instance object is used when outside of the object or class/function

there is no difference b/w create a staticmethod inside a class and create a normal function outside the class

static method useful when used as in inheritance

'''




class School():


    def __int__(self,total=0):
        self._total=total
        self._value = 0

    def avg(self):
        return self._total/5


    @property
    def total(self):
        return self._total

    @total.getter
    def total(self):
        print(f'Returning..{self._total} ')

    @total.setter
    def total(self,s):
        print(f'Setting ')
        self._total=s


