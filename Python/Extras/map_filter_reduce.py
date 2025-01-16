def cube(n):
    return n*n*n
l = [1,3,4,5,6,9,6]
# l2 = []
# for i in range(len(l)):
#     l2.append(cube(l[i]))

l2 = list(map(cube,l))

print(l2)

def filter_function(a):
    return a>4

l3 = list(filter(filter_function,l))
print(l3)
 

def reduce_function(x,y):
    return x+y
from functools import reduce
sum = reduce(reduce_function, l)
print(sum)


