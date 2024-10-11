# Problem link - https://www.geeksforgeeks.org/next-smaller-element/


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

    def top(self):
        if self.is_empty():
            return
        return self.head.data

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


class Solution:
    @staticmethod
    def next_smaller(arr):
        """
            Time complexity is O(n)
        """
        stack = Stack()
        result = [None for i in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            while not stack.is_empty() and arr[stack.top()] >= arr[i]:
                stack.pop()
            if stack.is_empty():
                result[i] = -1
            elif arr[stack.top()] < arr[i]:
                result[i] = arr[stack.top()]
            stack.push(i)
        return result


print(Solution.next_smaller([4, 8, 5, 2, 25]))
print(Solution.next_smaller([13, 7, 6, 12]))