#find missing number
nums=[2,1,4,0,5,6]
n=len(nums)
expectedSum=n*(n+1)//2
actualSum=0
for i in nums:
    actualSum+=i
print("the missing number is:", expectedSum-actualSum)    

#reversing string using stack
class Stack:
  def __init__(self):
    self.stack=[]

  def push(self,item):
    self.stack.append(item)

  def pop(self):
    if not self.is_empty():
      return self.stack.pop()
    return None

  def is_empty(self):
    return len(self.stack)==0

def reverse_name(name):
  stack=Stack()
  for char in name:
     stack.push(char)

  reversed_name=""
  while not stack.is_empty():
    reversed_name+=stack.pop()
  return reversed_name

name=input("Enter your name: ")
result=reverse_name(name)
print("original name:", name)
print("Reversed name: ", result)
  
  #paranthesis balance checking
def is_balanced(input_string):
    stack=[]
    pairs={')':'(', ']':'[', '}':'{'}
    for char in input_string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1]!=pairs[char]:
                return False 
            stack.pop()
    return not stack

input_string=input("enter a string: ")
result=is_balanced(input_string)
print("The balancing condition is :", result)       



    
    