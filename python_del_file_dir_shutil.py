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

# onerror function to handle exception
def handler(func, path, exc_info):
    print("Inside handler")
    print(exc_info)


# removing directory
shutil.rmtree(path,onerror = handler)
