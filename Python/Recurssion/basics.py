def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
n = int(input("Enter number for factorial: "))
print(n,"!=",fact(n))

def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return fibo(n-1) + fibo(n-2)
a = int(input("Enter last number of terms in fibonacci series: "))
for i in range(a):
    print(fibo(i),"",end="")
