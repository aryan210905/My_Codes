# it may happen that value of an attribute is dependant on any other attribute or function
# changes to the attribute or function would not change the value of the dependant attribute
# so, to make the changes in the dependant attribute as well, we use @property which
# converts the dependee function into a property and changes would also happen to it

class Person:
    def __init__(self,phy,maths,chem):
        self.phy = phy
        self.maths = maths
        self.chem = chem
    
    @property
    def percentage(self):
        print((self.phy+self.maths+self.chem)/3)

a = Person(39,98,46)
a.percentage