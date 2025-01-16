import random
import string
num = random.randint(10,40)   # chooses random number between 10 and 40
                              # a <= num <= b                  
print(num)

num2 = random.random()      # random number between 0.0 and 1.0
print(num2)                 # 0.0 <= num2 < 1.0

l = ["Heads","Tails","Aryan"]
print(random.choice(l))

l2 = [1,3,4,3,5,1,1,9,5,3,2,5,6,1,9]
print(len(l2))
x = int(input("Enter number of values needed: "))
if(x>len(l2)):
    print("Out of range")
else:
    l3 = random.sample(l2,x)
    print(l3)

