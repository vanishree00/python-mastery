class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
newNode1=Node(10)
newNode2=Node(20)
newNode3=Node(30)
newNode1.next = newNode2
newNode2.next = newNode3
head = newNode1
print(head.data)
print(head.next.data)
print(head.next.next.data)


