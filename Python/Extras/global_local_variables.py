x = 4
def func():
    global x
    x = 10
func()
print(f"Global variable = {x}")


# suppose we want to make changes to the global variable from a function then to do so
# we use 'global' keyword