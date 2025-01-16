import random 
a = input("Enter choice: Stone / Paper / Scissors: ")

possibility = ["Stone","Paper","Scissors"]
b = random.choice(possibility)
print(f"Computer's choice {b}")

if((a=="Paper" and b=="Stone") or (a=="Scissors" and b=="Paper")
     or (a=="Stone" and b=="Scissors")):
    print("You win")

elif((a=="Stone" and b=="Paper") or (a=="Paper" and b=="Scissors")
     or (a=="Scissors" and b=="Stone")):
    print("You lose")

else:
    print("Draw")