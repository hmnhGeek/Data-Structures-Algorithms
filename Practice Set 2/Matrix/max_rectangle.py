class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return -1
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return -1
        return self.head.data


class MaxAreaInHistogramFinder:
    @staticmethod
    def find(arr):
        n = len(arr)
        stack = Stack()
        max_area = 0
        for i in range(n):
            while not stack.is_empty() and arr[stack.top()] >= arr[i]:
                bar = arr[stack.pop()]
                right = i
                left = stack.top()
                area = bar * (right - left - 1)
                max_area = max(max_area, area)
            stack.push(i)
        while not stack.is_empty():
            bar = arr[stack.pop()]
            right = n
            left = stack.top()
            area = bar * (right - left - 1)
            max_area = max(max_area, area)
        return max_area


print(MaxAreaInHistogramFinder.find([2, 1, 5, 6, 2, 3]))
print(MaxAreaInHistogramFinder.find([2, 4]))
print(MaxAreaInHistogramFinder.find([60, 20, 50, 40, 10, 50, 60]))
print(MaxAreaInHistogramFinder.find([3, 5, 1, 7, 5, 9]))