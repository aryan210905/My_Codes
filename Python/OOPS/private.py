# To make an attribute private add 2 underscores before the name of the attribute
# Private attributes can only by accessed within the class and not outside the class
class Account:
    def __init__(self,name,accNo,accPass):
        self.name = name
        self.accNo = accNo
        self.__accPass= accPass     # Made private by adding 2 underscores
    def printPass(self):
        print(self.__accPass)
a = Account("Aryan",214,3555)

# if we try to access the private property outside the class, it will give an error