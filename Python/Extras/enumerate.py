# it is a built in function which allows us to get the index of any element 
# in a collection (list, string, tuple, etc.) at the same time as getting the element

'''
marks = [4,4,6,2,6,9,10,3,1,5]
index = 0
for i in marks:
    print(i)
    if(index == 3):
        print("Heyyyy")
    index += 1

# Here, we have to maintain an extra variable to fetch index of all elements
# to avoid this, we use enumerate(marks)
'''
marks = [4,4,6,2,6,9,10,3,1,5]
for index,i in enumerate(marks):
    print(i)
    if(index == 3):
        print("Heyyyy")

print("\n")

for index, i in enumerate(marks):
    print(f"{index}=>{i}")

print("\n")

# We can also start index from any value by enumerate(marks, start = 4)
fruits = ['apple','banana','orange','kiwi','pineapple']
for index, i in enumerate(fruits, start=3):
    print(f"{index} -> {i}")

