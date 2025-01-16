class Employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    def showDetail(self):
        print(self.role,self.dept,self.sal)

class Engineer(Employee):
    def __init__(self,name,age,role,dept,sal):
        self.name = name
        self.age = age
        super().__init__(role,dept,sal)
    def printData(self):
        print(self.name,self.age, end=" ")
        super().showDetail()

a1 = Engineer("Aryan",20,"AI Engineer","AI/ML","1000000")
a1.printData()