def average(a,b):
    avg = (a+b)/2
    print(avg)
a = 4
b = 9
average(a,b)    

'''
types of arguments:-
1) Default argument:
    These are initialised while declaration 
    Eg: def average(a=9,b=1):
    Now, if we provide any other values of arguments in function call, then those values are taken
    and not the ones initialised during declaration 

2) Required argument:
    These are required to be passed during function calls as these are not initialised during
    function call

3) Keyword argument
    When argument is declared with a * then it acts as a tuple
    if we declare it with ** then it acts as a dictionary
'''


def product(a=9,b=13):  # default argument
    pro = a*b
    print(pro)
product(a=14,b=20)


def sum(a,b):  # required argument
    sum = a+b
    print(sum)
sum(44,10)

def average(*numbers):  # keyword argument
    print(numbers)
    sum = 0
    for i in numbers:
        sum += i
    print(sum/len(numbers))
average(4,5,6,7,8,9)        # passed as tuple (like array)