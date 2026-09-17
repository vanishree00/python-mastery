class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    # Create a dummy node
    dummy = Node(0)
    dummy.next = head

    prev = dummy
    current = head

    while current != None:

        # Check whether current value is duplicated
        if current.next != None and current.data == current.next.data:

            duplicate_value = current.data

            # Skip all nodes having the duplicate value
            while current !=None and current.data == duplicate_value:
                current = current.next

            # Connect previous node to the next distinct node
            prev.next = current

        else:
            # Current node is distinct
            prev = current
            current = current.next

    return dummy.next


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create the sorted linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(5)

print("Original linked list:")
display(head)

head = remove_duplicates(head)

print("After removing duplicates:")
display(head)