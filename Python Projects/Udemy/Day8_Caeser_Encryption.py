def encrypt(message):
    shifts = int(input("Enter number of shifts: "))
    message = message.lower()
    l = list(message)
    print(l)
    s = ""
    for i in l:
        if i == " ":
            continue
        else:
            print(i,end = "->")
            x = ord(i)
            ascii = x + shifts
            i = chr(ascii)
            print(i)
            s = s + i
    return s
def decrypt(code):
    pass
print("Welcome to Caesar Cipher!")
print("Menu:")
print("1.Encrypt")
print("2.Decrypt")
print("3.End")
while True:
    print("What do you want to do?")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            message = input("Enter your message: ")
            code = encrypt(message)
            print(f"Encrypted message is: {code}")
        case 2:
            code = input("Enter a code: ")
            decryptedMessage = decrypt(code)
            print(f"Decrypted message is {decryptedMessage}")
        case 3:
            break
        case _:
            print("Enter valid input only!")