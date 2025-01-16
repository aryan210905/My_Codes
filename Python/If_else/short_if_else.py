a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"{a}>{b}") if a>b else print(f"{a}<{b}") if a<b else print(f"{a}={b}")

c = 9 if a>b else 0
print(c)