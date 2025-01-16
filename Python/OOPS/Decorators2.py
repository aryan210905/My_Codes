def decorator(function):
    def wrapper(*args,**kwargs):        # *args == takes arguments as tuple
                                        # **kwargs == takes arguments as dictionary
        print("\nBefore")
        function(*args,**kwargs)
        print("After\n")
    return wrapper


@decorator      # This equivalents to decorator(add)()
def add(a,b):
    print(a+b)

add(2,4)