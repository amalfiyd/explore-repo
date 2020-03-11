# Main class of LinkedList
class LinkedList:
    # Initialization
    # Initialize the linked list with head == None
    def __init__(self):
        self.head = None

    # Print
    # Print through the elements of the linked list
    def print(self):
        pointer = self.head
        while pointer:
            print(pointer.value)
            pointer = pointer.next

    # Prepend
    # Prepending element to the beginning of the list
    def prepend(self, node):
        node.next = self.head
        self.head = node

    # Append
    # Appending element to the end of the list
    def append(self, node):
        pointer = self.head
        while pointer.next:
            pointer = pointer.next

        pointer.next = node

    # Adding in the middle
    # Adding element in the middle, assuming insertion is after the first value
    def add(self, node, value):
        pointer = self.head
        while pointer:
            if pointer.value == value:
                if pointer.next:
                    node.next = pointer.next
                    pointer.next = node
                else:
                    pointer.next = node
            pointer = pointer.next

    # Delete
    # Delete node on the linked list based on given value
    def delete(self, value):
        pointer = self.head

        if not pointer:
            return

        if pointer.value == value:
            self.head = None
            self.value = None

            return

        pointerEarly = pointer.next
        while pointerEarly:
            if pointerEarly.value != value:
                pointer = pointer.next
                pointerEarly = pointerEarly.next
            else:
                pointer.next = pointerEarly.next
                return

        self.print()
        return


# Aux class of the node of Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node5 = Node('node 5')
node4 = Node('node 4')
node3 = Node('node 3')
node2 = Node('node 2', node3)
node1 = Node('node 1', node2)

tempLL = LinkedList()
tempLL.head = node1
tempLL.append(node4)
tempLL.append(node5)
tempLL.print()
