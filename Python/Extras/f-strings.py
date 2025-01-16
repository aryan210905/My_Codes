# we use f-strings for string formating
# we can add different variables/strings to another string by string formatting

name = "Aryan"
country = "India"
string = f"Hey! My name is {name} and I am from {country} " # this is how f-strings are stored
print(string)

# f-strings came with python 6.0

# we can also add expressions in f-strings
string2 = f"{2*90}"     # stores 180 in string2
print(string2)

# if we want to actually print the variable in f-string then we keep them in double curly braces
string3 = f"Hey! My name is {{name}} and I am from {{country}} "
print(string3)