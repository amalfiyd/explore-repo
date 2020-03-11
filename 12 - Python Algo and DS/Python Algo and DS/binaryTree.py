'''
Binary Tree implementation on Python
Assuming left <= data <= right
'''
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinaryTree(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinaryTree(data)

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

BT = BinaryTree(12)
BT.insert(6)
BT.insert(14)
BT.insert(3)

BT.print()


# # Main class for the Binary Tree
# class Node:
#     # Initialization
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#
#     # Insert
#     # Insertion of a node to the binary tree
#     def insert(self, data):
#         if not self.data:
#             self.data = data
#         else:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#
#     # Print
#     # Iterate through the tree
#     def print(self):
#         if self.left:
#             self.left.print()
#         print(self.data)
#         if self.right:
#             self.right.print()


# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
#
# root.print()
