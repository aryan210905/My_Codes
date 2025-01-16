
class Person:
    j = "abc"
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

obj = Person("Aryan",29,10000000)

print(dir(Person))      # gives info about all methods of an object/class

print(obj.__dict__)     # prints all the objects attributes and methods 
print(Person.__dict__)  # prints all the class attributes and methods

print(help(Person))     # help(class) gives info about the entire class
    