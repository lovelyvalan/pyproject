from OOPS import Car
from OOPS import School


# create an object for class

a = Car('tata', 'indigo', 'tn92s')
b = Car('tata', 'nexon', 'tn92s')
a.batt = 88
a.start()
print('===========')
b.batt = 98
b.start()
print('===========')
a.get_type()  # here a is considered as a class
Car.get_type()
print('===========')
a.build_cars()
print('===========')
a.build_cars1()
print('===========')


k = Car('honda','amaze','tn72')
k.batt=77
print(k.make)
k.make = 'suzuki'
print(k.make)
print('===========')
k.start()
# del k.make
# k.make='hyundai'
# print(k.make)
print('k car type ',k.type )
Car.type='xuv'
print('after renaming k car type ',k.type)
print(Car.__dict__)
print('===========')



print('SCHOOL')

o=School()
o.total=450
print(o.avg())


