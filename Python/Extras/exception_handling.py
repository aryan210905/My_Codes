a = input("Enter number for multiplication table: ")
try:       
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("There is some error in your input!!!")


# piece of code in except will happen instead of throwing an error for invalid input
try:
    b = int(input("Enter number in int only: "))
except ValueError:
    print("Invalid input!!")


try:
    dic = {1:100, 2:200, 3:300}
    del dic
    print(dic)
except Exception as e:      # this code prints that particular error which could have 
                            # happened
    print(e)


# in a normal program without try....except, if an exception happens,
# then no further lines of codes will run
# but in try...except, the lines of code after except will run even after facing
# an exception