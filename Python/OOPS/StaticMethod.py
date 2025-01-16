# Static methods are decorators which help us make methods in a class which do not require 
# self as an argument

# It may happen that some methods in a class do not require self as an argument
# but without self, it will throw an error 
# TypeError: Student.hello() takes 0 positional arguments but 1 was given
# So to avoid the error, we will use Static methods

class Student:
    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def hello():
        print("hello")

s1 = Student("Aryan")
print(s1.name)
s1.hello()