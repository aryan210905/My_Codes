# similar to switch in c
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
match a>b:
    case True:
        print(a," is greater than",b)
    case False:
        print(a," is smaller than",b)
    case _:             # default case
        print("Cant say")
