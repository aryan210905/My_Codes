tup = (1,4,7.3,9.5,"Aryan",True)
# to add/delete element in tuple, we need to convert into list and then add/delete and then
# convert back to tuple

# add "Shah" at the end of tuple
list1 = list(tup)       # converting tuple to list
list1.append("Shah")    # adding "Shah" to list
tup = tuple(list1)            # converting list to tuple
print(tup)

# deleting 9.5 from tuple
list2 = list(tup)
list2.remove(9.5)
tup = tuple(list2)
print(tup)