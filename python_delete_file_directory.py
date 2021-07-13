#Removing a File Using os.remove()
import os
print("Enter file name")
# File name
file = input()

# File location
print("Enter file path")
location = os.path.abspath(input())

# Path
path = os.path.join(location, file)
# Remove the file
os.remove(path)
print(file,"has been removed")
