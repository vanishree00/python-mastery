#Example 1 — Find  current directory
import os
current_location = os.getcwd()
print(current_location)

#Example 2 — See everything inside  current directory
items = os.listdir()
print(items)

#Example 3 — Create a new folder
os.mkdir("py_modules")
print(" folder created successfully")

#Example 4 — Rename a folder
os.rename("OS_practice", "folder1_by_mkdir")
os.rename("py_modules", "folder2_by_mkdir")

