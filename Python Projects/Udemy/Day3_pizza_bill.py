print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L: ")
pep = input("Do you want pepporani on your pizza? Y or N: ")
cheese = input("Do you want extra cheese on your pizza? Y or N: ")
bill = 0
if(size=="S"):
    bill += 15
elif(size=="M"):
    bill += 20
elif(size=="L"):
    bill += 25
else:
    print("Wrong input")
if(pep == "Y"):
    if(size=="S"):
        bill += 2
    else:
        bill += 3
if(cheese == "Y"):
    bill += 1

print(f"Your total bill is ${bill}")

