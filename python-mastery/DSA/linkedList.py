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

     def insert_at_begining(self, data):
        newNode4 = Node(data)
        newNode4.next = self
        return newNode4

newNode1=Node(10)
newNode2=Node(20)
newNode3=Node(30)
newNode1.next = newNode2
newNode2.next = newNode3
head= newNode1
# newNode4= Node(40)   #inserting at begninng
# newNode4.next = head
# head = newNode4
newNode5 = Node(50)   #inserting at end
current = head 
while current.next != None:
   current = current.next
current.next= newNode5    
print(head.data)
print(head.next.data)
print(head.next.next.data)

head.printLinkedList()   #calling the method directly on head node
head =head.insert_at_begining(40)
head.printLinkedList()

