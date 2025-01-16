# Student system

class Student:
    def __init__(self,name,marksPhy,marksChem,marksMaths):
        self.name = name
        self.marksPhy = marksPhy
        self.marksChem = marksChem
        self.marksMaths = marksMaths
    def average(self):
        avg = (self.marksPhy + self.marksChem + self.marksMaths)/3
        return avg
    def printData(self):
        print(f"\nName: {self.name}")
        print(f"Marks in Physics: {self.marksPhy}")
        print(f"Marks in Chemistry: {self.marksChem}")
        print(f"Marks in Maths: {self.marksMaths}")
        print(f"Average marks => {self.average()}\n")
    
s1 = Student("Aryan",81,55,86)
s2 = Student("Jay",49,97,43)
s3 = Student("Ram",94,53,88)


s1.printData()
s2.printData()
s3.printData()


