import os

f = open("AIML/Python/File IO/myfile2.txt","r")
# data = f.read()     # reads entire data
# print(data) 

# We cannot use f.readline() properly after using f.read()

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()

# deleting a file
# f = open("AIML/Python/File IO/test_file.txt","w")
os.remove("AIML/Python/File IO/test_file.txt")