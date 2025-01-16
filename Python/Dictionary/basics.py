# ordered collection of items with a key to access those items faster

dic = {             # dic = { key : value ,......}
    100 : "Aryan",
    110 : "Rahil",
    120 : "Jay",
    130 : "Suman"
}

print(dic)
print(type(dic))
print(dic[120])     # print value of key = 120
print(dic.get(120)) # also prints value of key = 120 but difference is that
                    # in dic.get(key), if key is not present it will not throw
                    # an error but in dic[key] it will throw error if key is 
                    # not present

print(dic.keys())   # prints all keys in dictionary
for key in dic.keys():  # prints all keys using loops
    print(key)

print(dic.values()) # prints all values in dictionary

for key, value in dic.items():  # prints all keys with their values
    print(key,value)



# hence, to use all keys we use dic.keys()
# to use all values, we use dic.values()
# to use all items i.e. keys and values, we use dic.items