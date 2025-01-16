import os
# if(not os.path.exists("Data")):
#     os.mkdir("AIML/Python/OS/Data")       # creates a folder if doesnt exist

# for i in range(0,10):
    # os.mkdir(f"AIML/Python/OS/Data/File {i+1}")       # makes 10 folders

folder = os.listdir("AIML/Python/OS/Data")
print(folder)       

for i in folder:
    print(i,"",end="")  # enlists all the files 
    print(os.listdir(f"AIML/Python/OS/Data/{i}"))   # enlists all the files in the folder


for i in range(0,10):
    os.rename(f"AIML/Python/OS/Data/File {i+1}",f"AIML/Python/OS/Data/Folder {i+1}")

for i in range(0,10):
    print(os.listdir(f"AIML/Python/OS/Data/Folder {i+1}"))
    