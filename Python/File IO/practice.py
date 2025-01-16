
with open("AIML/Python/File IO/practice.txt") as f2:
    data = f2.read()
new_data = data.replace("Python","Java")

print(new_data)

f2.close()
