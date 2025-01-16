fruit = "Apple"
length = len(fruit) # len(string) returns length of string
print(length)
print(fruit[0:3]) # prints the string from first written index to (second index -1)  
print(fruit[:4]) # automatically considers 0 as first index if not written
print(fruit[:9]) # if 2nd index is greater than length of string then full string is returned
print(fruit[0:-2])  # if any index is -ve then that index is considered as len(string) - index
                    # so here -2 means len(fruit) - 2 and so App is printed
print(fruit[9:3]) # if first index > second index then nothing is printed
