class Node:
    def __init__(self, data):
        self.data = data  # instance variable to store the data
        self.next = None  # instance variable with address of next node

    def find(self, data):
        if self.data == data:
            return self
        if self.next is None:
            return None
        return self.next.find(data)


# The 'head' is the first node in a linked list.
head = Node("Maine")
another_node = Node("Idaho")

# Stores to address of Idaho node as the next address of the first node in the list.
head.next = another_node

third_node = Node("Utah")
another_node.next = third_node

# Example of printing the data of the list in order:
# node = head
# while Node is not None:
#     print(node.data)
#     node = node.next

# Example of using find(data) method
print("Found:  " + str(head.find("Utah").data))
