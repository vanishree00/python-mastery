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


print("challenging myself")
#Challenge 1: Write a program that: Imports os,
# Prints your current working directory
#Prints everything inside it
import os
print(os.getcwd())
print(os.listdir())
# Challenge 2
# Create a folder called:
# my_python_work
# Then rename it to:python_projects
# Then delete it.
# So your program should perform:
#Create -> rename -> delete
os.mkdir("my_python_work")
print("new directory created...")
os.rename("my_python_work", "python_projects")
print("renamed is done")
os.rmdir("python_projects")
print("removed sucessfully..")

# Challenge 3 ⭐
# Create this folder structure: os_practice
# Inside it, create:
# os_practice
#     ├── python
#     ├── javascript
#     └── projects
os.mkdir("OS_pracitce")
os.mkdir("OS_pracitce/python") #it's like creating nested folder using path
os.mkdir("OS_pracitce/javascript")
os.mkdir("OS_pracitce/projects")
os.mkdir("OS_pracitce/web development")
print(os.listdir("OS_pracitce"))