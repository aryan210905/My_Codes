'''
Encoding:
    If string has atleast 3 characters:
        remove first character and append it to the end
        append 3 random characters to start and end of the string
    else:
        reverse the string if not of atleast 3 characters
Decoding:
    If string has atleast 3 characters:
        delete first and last 3 characters 
        Delete last character and append it to start
    else:
        reverse the string if not of atleast 3 characters
'''

import random
import string

s = input("Enter string: ")

print("Operations:")
print("1.Encoding")
print("2.Decoding")
a = int(input("Enter choice: "))

if(a==1):   # encoding
    if(len(s) >= 3):
        first_character = s[0]
        s = s.replace(s[0],"")
        s = s+first_character
        a = ''.join(random.choices(string.ascii_letters+string.digits , k=3))
        s = a + s + a
    else:
        s = s[::-1]
    
    print("Encoded string is: ",s)
    
elif(a==2): # decoding
    if(len(s) >= 3):
        
        s = s[3:len(s)-3]
        ch = s[len(s)-1]
        s = s.replace(ch,"")
        s = ch+s
        print(s)
    else:
        s = s[::-1]
        print(s)
else:
    print("Enter valid input only!")
