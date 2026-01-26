from typing import List


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
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return None
        return self.head.data


class Utility:
    @staticmethod
    def get_max_area_in_histogram(histogram: List[int]) -> int:
        stack = Stack()
        n = len(histogram)
        max_area = 0
        for i in range(n):
            while not stack.is_empty() and histogram[stack.top()] >= histogram[i]:
                bar = histogram[stack.pop()]
                lb = stack.top() if not stack.is_empty() else -1
                area = bar * (i - lb - 1)
                max_area = max(max_area, area)
            stack.push(i)
        while not stack.is_empty():
            bar = histogram[stack.pop()]
            lb = stack.top() if not stack.is_empty() else -1
            area = bar * (n - lb - 1)
            max_area = max(max_area, area)
        return max_area


print(Utility.get_max_area_in_histogram([60, 20, 50, 40, 10, 50, 60]))
print(Utility.get_max_area_in_histogram([3, 5, 1, 7, 5, 9]))
