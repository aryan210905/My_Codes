print("Welcome to Treasure Island. Your mission is to find the hidden treasure!")
choice1 = input("Where do you want to go? Left or Right? ")
if(choice1 == "Right"):
    print("Game Over")
elif(choice1 == "Left"):
    choice2 = input("Do you want to swim or wait? Swim or Wait? ")
    if(choice2 == "Swim"):
        print("Game Over")
    elif(choice2 == "Wait"):
        choice3 = input("Which door do you want to choose? Red, Blue or Green? ")
        if(choice3 == "Red" or choice3 == "Blue"):
            print("Game over")
        elif(choice3 == "Green"):
            print("You won!!!!")
        else:
            print("Wrong choice!")
    else:
        print("Wrong choice!")
else:
    print("Wrong choice!")