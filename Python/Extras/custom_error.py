# raise keyword is used to raise custom errors
a = int(input("Enter input between 10 and 20: "))
if(a<10 or a>20):
    raise ValueError("Invalid input")

