f = open('AIML/Python/File IO/myfile.txt','r')
# print(f)
text= f.read()
print(text)
f.close()

f2 = open("AIML/Python/File IO/myfile2.txt",'w')
f2.write("HELLO SIRI")
f2.close()

f3 = open("AIML/Python/File IO/myfile2.txt", 'a')
f3.write(" How are you")
f3.close()

# by 'with' keyword, we can directly use file handling functions without closing the file
with open("AIML/Python/File IO/myfile2.txt",'a') as f3:
    f3.write(" I am inside with")
