import sys

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.head[0] = sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2*pos) + 1

    def isLeaf(self, pos):
        if (pos >= self.size // 2) and (pos <= self.size):
            return True
        return False

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if (
                (self.heap[pos] < self.heap[self.leftChild(pos)]) or
                (self.heap[pos] < self.heap[self.rightChild(pos)])
            ):
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.heap[self.size]

        while self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.heap[self.parent(current)])
            current = self.heap[self.parent(current)]

    def print(self):
        for i in range(1, (self.size//2) + 1):
            print(self.heap[i],
                  self.heap[self.leftChild(i)],
                  self.heap[self.rightChild(i)])

    def extractMax(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.maxHeapify(self.front)
        return popped

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.front = 1
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = -1 * sys.maxsize

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return (2 * pos)

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if (
            (pos >= self.size // 2) and
            (pos <= self.size)
        ):
            return True
        return False

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.heap[pos] > self.heap[self.leftChild(pos)] or
            self.heap[pos] > self.heap[self.rightChild(pos)]):
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.heap[self.size]

        while self.heap[current] < self.heal[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print(self):
        for i in range(1, (self.size//2) + 1):
            print(
                self.heap[i],
                self.heap[self.leftChild(i)],
                self.heap[self.rightChild(i)]
            )
