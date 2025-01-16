class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printData(self):
        print(f"Name = {self.name} , Age = {self.age}")
a = Student("Aryan",20)
b = Student("Jay",24)

a.printData()
b.printData()

del a.name      # Deletes properties of an object
del b           # Deletes entire object too

