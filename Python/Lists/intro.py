# kinda like arrays
# list = ordered collection of items
# we can store multiple data types in list
# lists are mutable i.e. items in a list can be altered as required after creation of the list


l = [2, 4, 6, 7.9, 1, "Aryan", "Shah", True]
print(l)
print(type(l))

print("\nPrinting by square brackets:",l[0])
print("\nPrinting entire list:")
for i in l:
    print(i,type(i))

# if negative index is accessed, we subtract it from length(list)
print(l[-2]) # l[len(l)-2] i.e. l[6] = "Shah"

print(l)
print(l[:])     # prints entire list
print(l[1:])    # prints entire list starting from index 1
print(l[1:5])   # prints entire list from index 1,2,3,4
print(l[1:5:2]) # prints entire list and jumps twice between each index so prints index 1,3 
# format is [start : end : jump_index]


# used if we want to check whether item is in the list
# kinda like linear search but we cannot find position
if "Aryan" in l:    
    print("Aryan is present in list")
else:
    print("Aryan is not in list")