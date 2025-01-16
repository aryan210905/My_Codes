'''
A constructor is a special method in a class used to create and initialize an object of a class. 
A constructor is a unique function that gets called automatically when an object is 
created of a class. The main purpose of a constructor is to initialize or assign values 
to the data members of that class. It cannot return any value other than None.

2 types of constructor:
1) Parameterized constructors -> Some arguments are passed along with self
2) Default constructor  -> Only self is passed as an argument   


'''

class Student:
    def __init__(self,name,id,branch):
        self.name = name
        self.id = id
        self.branch = branch
    def info(self):
        print(f"{self.id}. {self.name} is in {self.branch} branch")

a = Student("Aryan",1,"IT")
b = Student("Rahil",2,"CE")

a.info()
b.info()

# it is recommended to pass self in every method of a class
# A constructor is called everytime an object is created