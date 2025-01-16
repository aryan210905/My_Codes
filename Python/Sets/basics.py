# cannot be changed 
# unordered collection i.e. in random order
# cannot be accessed using indices as they are unordered
# do not contain repeated items
# even if we feed it repeated values, it will consider only one value

s = {1, "Aryan", 5.7, True, 3, "Shah", 1, False, 1}
print(s)

# if we want to create an empty set and we initialise it as s = {}
# then interpreter will think that this is a empty dictionary
# to avoid this we initialise the empty set as s = set()

s1 = set()
print(type(s1))

# to access set items, we use loops
for i in s:
    print(i)