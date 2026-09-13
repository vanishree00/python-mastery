#module is simply a Python file (.py) containing Python code such as:Variables,Functions,Classes,Statements
#We create modules mainly to organize and reuse code.
#Without modules, a large Python program could become one huge file.
#types of modules: built-in modules, user-defined modules, third-party modules

#1. built-in modules (math, random, os, sys, datetime)[pre installed in system]
#These come with Python.
print("MATH MODULE")
import math 
 #The import statement is used to bring a module into your Python program so that you can use its functionality.
print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))
print(math.pow(2,3))
#here math is module . sqrt(), factorial()....are functions inside module

print("RANDOM MODULE")
import random
print(random.randint(1,6))
options=["Alice", "Bob", "Vanishree", "Triveni"]
print(random.choice(options))
cards=["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
print(cards)

print("DATETIME MODULE")
import datetime
right_now=datetime.datetime.now() #get the current exact date and timestamp
print(right_now)
print(right_now.year) #extract just single attribute 
today=datetime.date.today()#calculate a future date(using temdelta)
ten_days_later=today+ datetime.timedelta(days=10)
print(ten_days_later)
#datetime.datetime.now()[1st datetime: go to main time module, 2nd .datetime: look for the toolbox that handels both date+time, .now(): give me the exact moment right this second]
