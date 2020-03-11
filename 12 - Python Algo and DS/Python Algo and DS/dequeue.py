'''
Simple dequeue implementation in python
'''

# Auxiliary class for the Node object
class Node:
    # Initialization of Node
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# Main class for Dequeue
class Dequeue:
    # Initialization of Dequeue
    def __init__(self):
        self.front = None
        self.back = None

    # Print
    # Printing all element, isFront indicates if printing is done from the front or the back
    def print(self, isFront=True):
        if isFront:
            pointer = self.front
            while pointer:
                print(pointer.value)
                pointer = pointer.next
        else:
            pointer = self.back
            while pointer:
                print(pointer.value)
                pointer = pointer.prev

    # addFront
    # Adding element in the front of the queue
    def addFront(self, node):
        if not self.front and not self.back:
            self.front = node
            self.back = node
        else:
            pointer = self.front
            self.front = node
            self.front.next = pointer
            pointer.prev = self.front

    # addBack
    # Adding element in the back of the queue
    def addBack(self, node):
        if not self.front and not self.back:
            self.front = node
            self.back = node
        else:
            pointer = self.back
            self.back = node
            self.back.prev = pointer
            pointer.next = self.back

    # removeFront
    # Remove element in the front of the queue
    def removeFront(self):
        if not self.front and not self.back:
            return
        elif not self.front.next and not self.back.prev:
            print("Deleted ", self.front.value)
            self.front = None
            self.back = None
        else:
            print("Deleted ", self.front.value)
            self.front = self.front.next
            self.front.prev = None

    # removeBack
    # Remove element in the front of the queue
    def removeBack(self):
        if not self.front and not self.back:
            return
        elif not self.back.prev and not self.front.next:
            print("Deleted ", self.back.value)
            self.front = None
            self.back = None
        else:
            print("Deleted ", self.back.value)
            self.back = self.back.prev
            self.back.next = None

# Test use cases
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

test = Dequeue()
test.addFront(node1)
test.addFront(node2)
test.addFront(node3)


