class student:
    name = ""
    roll_No = None
    branch = ""
    def info(self):
        print(f"{self.name} is in {self.branch} branch  ")

a = student()   # a,b,c are objects of class student
b = student()
c = student()

a.name = "Aryan"
a.roll_No = 1
a.branch = "IT"

b.name = "Rahil"
b.roll_No = 2
b.branch = "Computer Engineering"

c.name = "Jay"
c.roll_No = 10
c.branch = "Civil Engineering"

a.info()
b.info()
c.info()

print(type(a))