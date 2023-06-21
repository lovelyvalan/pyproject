'''

The __init__() function is called automatically every time the class is being used to create a new object.

 The self parameter is a reference to the current instance of the class,
  and is used to access variables that belong to the class.

You can delete objects by using the del keywor

Set the age of p1 to 40:
p1.age = 40

'''


'''

Python Inheritance

Inheritance allows us to define a class that 
inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.


Create a Child Class

To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class:

'''


'''
By using the super() function, you do not have to use the name of the parent element,
it will automatically inherit the methods and properties from its parent.


In the example below, the year 2019 should be a variable, 
and passed into the Student class when creating student objects.
 To do so, add another parameter in the __init__() function:


If you add a method in the child class with the same name as a function in the parent class, 
the inheritance of the parent method will be overridden.
'''