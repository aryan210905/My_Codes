import aryan

# if __name__ == "__main__" idiom is used to determine whether a script is being
# run directly or being imported as a module into another script

# if we just import aryan.py , still we get an output as the file aryan.py calls the 
# function welcome and due to that we get an output
# to avoid this, we use if __name__ = "__main__"

# if __name__ == "__main__" that means that we are running the file aryan.py only
# if we run the file aryan.py from any other file then
# __name__ == "aryan"  i.e if we run a file from other file, then __name__ = name of
# file. So to ensure that we are running the same file then we need to call any functions
# by if __name__ == "__main__"

# as we called the function in aryan.py under an if condition, then that function
# call will only happen if the file we are running is the original file itself