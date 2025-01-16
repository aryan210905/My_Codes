import string
import random

letters = list(string.ascii_letters)

symbols = list(string.printable)
symbols = symbols[62:90]


numbers = list(string.digits)

x = int(input("Enter number of letters: "))
y = int(input("Enter number of symbols: "))
z = int(input("Enter number of digits: "))

letter2 = random.sample(letters,x)
symbols2 = random.sample(symbols,y)
numbers2 = random.sample(numbers,z)

password = letter2+symbols2+numbers2
for i in password:
    print(i,end="")
