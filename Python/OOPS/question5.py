class Order:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __gt__(self,order2):
        return self.price > order2.price
    
order1 = Order("Python Crash Course",1412)
order2 = Order("Java",1000)

if(order1>order2):
    print(f"{order1.name} is costlier than {order2.name}")
else:
    print(f"{order1.name} is cheaper than {order2.name}")