# a = True
# print(a=False)
# This will give an error 
# The above lines can be reduced to one line by walrus operator
# it allows us to use conditions within expressions
# it assigns variables values as a part of a larger expression

print(a:=False)
l = [1,3,5,6,2,9]
while((n:=len(l))>0):
    print(l.pop())

