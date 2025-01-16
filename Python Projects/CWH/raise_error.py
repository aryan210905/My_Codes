# raise an error if input is not = "Quit" or not an integer

a = input("Enter input: ")
if(a=="Quit" or a.isdigit()):
    raise SystemExit
else:
    raise ValueError("Invalid input")
