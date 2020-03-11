class MyArray:
    # Initializing array
    def __init__(self, initializer):
        self.n = len(initializer)
        self.data = initializer

    # Print
    # Print the array
    def print(self):
        for i in range(self.n):
            print(self.data[i])

    # Insertion
    # Insert value to the specified index and move the tailing values by 1
    def insert(self, value, index):
        if index < 0 or index > self.n:
            print("Index out of range")
            return

        temp = []
        for i in range(self.n):
            if index == i:
                temp.append(value)
            temp.append(self.data[i])

        self.data = temp
        self.n = len(self.data)

    # Append
    # Appending items in the last position
    def append(self, value):
        temp = []
        for i in range(self.n):
            temp.append(self.data[i])
        temp.append(value)

        self.data = temp
        self.n = len(self.data)

    # Search
    # Search through the array and return the index
    def search(self, value):
        for i in range(self.n):
            if self.data[i] == value:
                return i

    # Update
    # Update value for a specified index of the array
    def update(self, value, index):
        self.data[index] = value

    # Deletion
    # Delete the specified value from the array, only the first occurrence is deleted
    # if delAll is true, then delete all occurrences
    def delete(self, value, delAll = False):
        temp = []
        delOnce = False
        for i in range(self.n):
            if self.data[i] != value:
                temp.append(self.data[i])
            else:
                if delOnce:
                    temp.append(self.data[i])
                else:
                    if not delAll:
                        delOnce = True

        self.data = temp
        self.n = len(self.data)


temp = [1,2,3,4,5]
testArray = MyArray(temp)
testArray.print()
