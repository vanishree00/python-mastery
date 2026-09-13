class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def printLinkedList(self):  #self act as starting node 
     current = self
     while current!= None:
      print(current.data, end= "-->") 
      current = current.next
     print("None")        
        
newNode1=Node(10)
newNode2=Node(20)
newNode3=Node(30)
newNode1.next = newNode2
newNode2.next = newNode3
head= newNode1
newNode4= Node(40)
newNode4.next = head
head = newNode4
print(head.data)
print(head.next.data)
print(head.next.next.data)

head.printLinkedList()   #calling the method directly on head node


