class Solution:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

    def linkedList(self):
        current = self
        while current != None:
            print(current.data, end="-->")
            current= current.next  
        print("None")         
    def middleNode(self):
        slow=self
        fast=self
        while fast!=None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
        return slow    

    def deleteNode(self, node):
        node.data = node.next.data
        node.next = node.next.next
        
node1=Solution(1)
node2= Solution(2)
node3=Solution(3)
node4=Solution(4)
node5=Solution(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
head=node1
head.linkedList()
middle = node1.middleNode()
print(f" middle node is : {middle.data} ")
node1.deleteNode(node3)
print("After deleting the given node-")
head.linkedList()
