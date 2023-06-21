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
from CAR.AUTOMOBILE import Automobile



class Car(Automobile):
    type = 'suv'  # class attribute

    def __int__(self, make, model, regno):
        super().__init__(make, model, regno)
        if self.type == "suv":
            self.enginepow = '98%'
        elif self.type == 'xuv':
            self.enginepow = '100%'

    def start(self):
        print('Engine has started')
        print(f'make {self.make} ,model {self.model} ,regno {self.regno} ')
        self.battery()

    @classmethod
    def build_from_Automobile(cls, b: Automobile):
        cls(b.make, b.model, b.regno)
        return cls

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


# NOTES
'''
object is also instance 

if we use @classmethod in before the function the first argument will be a class... example cls...
the argument cls mention the class CAR

self is called whithin the function
but instance object is used when outside of the object or class/function

there is no difference b/w create a staticmethod inside a class and create a normal function outside the class

static method useful when used as in inheritance

'''


class School():

    def __int__(self, total=0):
        self._total = total
        self._value = 0

    def avg(self):
        return self._total / 5

    @property
    def total(self):
        return self._total

    @total.getter
    def total(self):
        print(f'Returning..{self._total} ')

    @total.setter
    def total(self, s):
        print(f'Setting ')
        self._total = s


print('======================')

# BIKE

b = Automobile('bajaj', 'ns', 'tn6961234')
b.make = 'ktm'
b.model = 'duke'
b.regno = 'tn72s1234'
print(b.make)
print(b.model)
print(b.regno)

c = Car.build_from_Automobile(b)
c.start
