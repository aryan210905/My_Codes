# Used to change class properties permanently

class Person:
    name = "No Name"    

    @classmethod
    def changeName(cls,newName):
        cls.name = newName
    
    # This also means the same
    # def changeName(self,newName):
    #     self.__class__.name = newName

a = Person()
print(a.name)
print(Person.name)
a.changeName("Ram")
print(Person.name)