# Python program to explain os.rmdir() method
import os
# Directory name
print("Directory name")
directory = input()
# Parent Directory
print("Parent Directory name")
parent = os.path.abspath(input())
# Joining both the Path
path = os.path.join(parent, directory)
# Remove the Directory
os.rmdir(path)
print(directory,"Sucessfully Removed")
