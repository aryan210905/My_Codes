try:
    a = int(input("Enter value: "))
except:
    print("Some error occured")
finally:
    print("This is always executed")

# finally keyword is always executed irrespective of whether exception happens or not
# we use finally so that when in functions we want some code of function to run 
# even after return call, then that will run in finally but not normally