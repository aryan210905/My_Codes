i = 5
while(i!=30):
    print(i)
    i = i+1
print("Exited the loop\n")

count = int(input("Enter starting index: "))
while(count>=0):
    print(count)
    count = count - 1
else:
    print("We are in else condtion and count =",count)
# we can also use else with while
# whenever a condition which is not matched with the while loop is obtained
# else condition is triggered and statements within it are executed
