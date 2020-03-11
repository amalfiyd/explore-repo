# Aux class for Node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Main class for stack
class Stack:
    # Initialization
    # Initialize stack object
    def __init__(self):
        self.top = None

    # Print
    # Print the elements in the stack from top to bottom
    def print(self):
        pointer = self.top
        headStr = "  <-- Top"
        while pointer:
            print(pointer.value, (headStr if pointer == self.top else ''))
            pointer = pointer.next

    # Push
    # Push new element into the stack
    def push(self, node):
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    # Pop
    # Pop the top element from the stack
    def pop(self):
        if not self.top or not self.top.next:
            self.top = None
            return

        self.top = self.top.next

node3 = Node(3)
node2 = Node(2)
node1 = Node(1)

myStack = Stack()
myStack.push(node1)
myStack.push(node2)
myStack.push(node3)