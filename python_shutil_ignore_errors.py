# Python program to remove a file by using shutil
import shutil
import os
# location
print("Please input location name")
location = os.path.abspath(input())

# directory
print("Please input directory name")
dir = input()

# path
path = os.path.join(location, dir)

# removing directory
shutil.rmtree(path)
