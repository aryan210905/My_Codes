class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def printNos(self):
        print(f"{self.real} + {self.img}i")
    def __add__(self,num):
        newReal = self.real + num.real
        newImg = self.img + num.img
        return Complex(newReal,newImg)

a = Complex(4,3)
b = Complex(1,5)

c = a + b
c.printNos()