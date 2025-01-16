# used to add lot of predefined modules in your code
import math
print(math.sqrt(14))

# use 'from' keyword to import a particular function from a module in the code
from math import sqrt
print(sqrt(14))

# we can import all the functions from a module by 
# from math import *
# However, it is not recommended to do this as this may create confusion

# we use 'as' keyword to name the module by any particular name
import math as m
print(m.sqrt(29))

# we can print all the functions in a module by dir(module)
import math
print(dir(math))

# we can also import functions/variables from our existing files
from docstrings import square
print(square(3))
