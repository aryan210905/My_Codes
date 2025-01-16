class Person:
    @staticmethod
    def hello():
        print("Hello World!")

class Student(Person):      # Student class inherits attributes and methods of 
                            # Person class
    def __init__(self,rollNo,grade):
        self.rollNo = rollNo
        self.grade = grade

a1 = Student(14,99)
a2 = Student(12,93)

print(a1.grade)
print(a2.rollNo)
a2.hello()


'''
Types of inheritance:
    1) Single inheritance
        One parent class and one child class
        class child(parent)
    2) Multiple inheritance
        Multiple parents and one child class
        class child(parent1,parent2,parent3,....)
    3) Multi-level inheritance
        child of one parent is parent of one more child
        class child(parent)
        class grandchild(child)
    4) Hybrid inheritance
        Contains both single and multiple inheritances
    5) Hierarchial inheritance
        one parent and multiple child classes
        class child1(parent)
        class child2(parent)
        class child3(parent)


'''