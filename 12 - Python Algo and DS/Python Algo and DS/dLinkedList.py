'''
Simple Double Linked List implementation in python
'''

# Auxiliary class for the Node object
class Node:
    # Initialization of Node
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def unlink(self):
        self.next = None
        self.prev = None

# Main class for Double Linked List
class DLinkedList:
    # Initialization of DLinkedList
    def __init__(self):
        self.first = None
        self.last = None

    # Print
    # Print all element in the list, fromFirst determines the direction of the print procedure
    def print(self, fromFirst=True):
        pointer = self.first if fromFirst else self.last
        while pointer:
            print(pointer.value)
            pointer = pointer.next if fromFirst else pointer.prev

    # Append
    # Appending element in the back of the list
    def append(self, node):
        if not self.first and not self.last:
            self.first = node
            self.last = node
        else:
            pointer = self.last
            self.last = node
            self.last.prev = pointer
            pointer.next = self.last

    # Prepend
    # Prepending element in the beginning of the list
    def prepend(self,node):
        if not self.first and not self.last:
            self.first = None
            self.last = None
        else:
            pointer = self.first
            self.first = node
            self.first.next = pointer
            pointer.prev = self.first

    # DeleteFirst
    # Delete node in the list given value and starting point from the left side
    # Assuming only deleting the first occurrence
    def deleteFirst(self, value):
        # if list is empty
        if not self.first and not self.last:
            return
        # if list has only 1 element
        elif not self.first.next and not self.last.prev:
            print("Deleted ", self.first.value)
            self.first = None
            self.last = None
            return
        # if list has only 2 elements
        elif self.first.next == self.last and self.last.prev == self.first:
            # value found in self.first
            if self.first.value == value:
                print("Deleted ", self.first.value)
                self.first = self.last
                self.last.prev = None
                return
            # value found in self.last
            elif self.last.value == value:
                print("Deleted ", self.last.value)
                self.last = self.first
                self.first.next = None
                return
            else:
                print("Element not found")
                return
        # if list has more than 2 elements
        else:
            pointer1 = None
            pointerDel = self.first
            pointer2 = self.first.next
            # Found in first
            if pointerDel.value == value:
                print("Deleted ", pointerDel.value)
                self.first = pointer2
                pointer2.prev = None
                return
            # Found later
            while pointer2 and pointerDel.value != value:
                pointer1 = pointerDel
                pointerDel = pointer2
                pointer2 = pointer2.next
            # if found in self.last
            if pointerDel == self.last:
                if pointerDel.value == value:
                    print("Deleted ", pointerDel.value)
                    self.last = pointer1
                    self.last.next = None
                    return
                else:
                    print("Element not found")
            # if found in the middle
            else:
                print("Deleted ", pointerDel.value)
                pointer1.next = pointer2
                pointer2.prev = pointer1
                return

    # DeleteLast
    # Delete node in the list given value and starting point from the right side
    # Assuming only deleting the first occurrence
    def deleteLast(self, value):
        # if list is empty
        if not self.first and not self.last:
            return
        # if list has only 1 element
        elif not self.first.next and not self.last.prev:
            print("Deleted ", self.first.value)
            self.first = None
            self.last = None
            return
        # if list has only 2 elements
        elif self.first.next == self.last and self.last.prev == self.first:
            # value found in self.first
            if self.first.value == value:
                print("Deleted ", self.first.value)
                self.first = self.last
                self.last.prev = None
                return
            # value found in self.last
            elif self.last.value == value:
                print("Deleted ", self.last.value)
                self.last = self.first
                self.first.next = None
                return
            else:
                print("Element not found")
                return
        # if list has more than 2 elements
        else:
            pointer1 = None
            pointerDel = self.last
            pointer2 = self.last.prev
            # Found in last
            if pointerDel.value == value:
                print("Deleted ", pointerDel.value)
                self.last = pointer2
                pointer2.next = None
                return
            # Found later
            while pointer2 and pointerDel.value != value:
                pointer1 = pointerDel
                pointerDel = pointer2
                pointer2 = pointer2.prev
            # if found in self.first
            if pointerDel == self.first:
                if pointerDel.value == value:
                    print("Deleted ", pointerDel.value)
                    self.first = pointer1
                    self.first.prev = None
                    return
                else:
                    print("Element not found")
            # if found in the middle
            else:
                print("Deleted ", pointerDel.value)
                pointer1.prev = pointer2
                pointer2.next = pointer1
                return

    # InsertAfter
    # Insert element after the given value found
    def insertAfter(self, node, value):
        # if the list is empty
        if not self.first and not self.last:
            self.first = node
            self.last = node
        # if the list has only 1 element
        elif self.first == self.last:
            if self.first.value == value:
                self.first.next = node
                self.last = node
                self.last.prev = self.first
            else:
                print("Element not found")
        # if the list has more than 1 elements
        else:
            pointer = self.first
            while pointer.next and pointer.value != value:
                pointer = pointer.next
            if pointer.value == value:
                # found in the last element
                if pointer == self.last:
                    pointer.next = node
                    node.prev = pointer
                    self.last = node
                # found in the middle
                else:
                    pointer2 = pointer.next
                    pointer.next = node
                    node.prev = pointer
                    node.next = pointer2
                    pointer2.prev = node
            else:
                print('Element not found')



# Test use cases
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

test = DLinkedList()
test.append(node1)
test.append(node2)
test.append(node3)
test.append(node4)
test.append(node5)



