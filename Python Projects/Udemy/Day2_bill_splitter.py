print("Welcome to your tip calculator!")
bill = float(input("What was your total bill? $"))
tip = float(input("How much tip you wish to give? "))
people = int(input("How many people are splitting the bill? "))

total_bill = bill + ((tip/100)*bill)
split = total_bill/5
print("Each person should pay: ",split)