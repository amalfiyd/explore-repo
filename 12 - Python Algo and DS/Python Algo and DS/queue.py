# Aux class for node
class Node:
    # Initialization
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Main class for queue
class Queue:
    # Initialization
    # Initialize the Queue
    def __init__(self):
        self.front = None
        self.back = None


    # Print
    # Print the Queue
    def print(self):
        pointer = self.front
        while pointer:
            print(pointer.value)
            pointer = pointer.next

    # Insertion
    # Inserting element to the back of the queue
    def insert(self, node):
        if not self.front and not self.back:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    # Delete
    # Deleting element from the front
    def pop(self):
        if not self.front and not self.back:
            return
        elif not self.front.next:
            self.front = None
            self.back = None
        else:
            pointer = self.front
            pointer = pointer.next
            self.front = pointer

node3 = Node(3)
node2 = Node(2)
node1 = Node(1)

myQueue = Queue()
myQueue.insert(node1)
myQueue.insert(node2)
myQueue.insert(node3)