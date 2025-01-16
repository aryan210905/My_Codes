a = 4
b = 10

'''
1)  
    temp = a
    a = b
    b = temp
2)
    a = a+b
    b = a-b
    a = a-b

'''

a,b = b,a
print(f"{a},{b}")