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
            return
        return self.head.data

    def clear(self):
        self.head = self.tail = None
        self.length = 0


class Solution:
    @staticmethod
    def _get_left_bounds(arr, stack: Stack):
        lb = [0]*len(arr)
        for i in range(len(arr)):
            while not stack.is_empty() and stack.top() < arr[i]:
                stack.pop()
            bound = 0 if stack.top() is None else stack.top()
            lb[i] = bound
            if stack.is_empty():
                stack.push(arr[i])
        return lb

    @staticmethod
    def _get_right_bounds(arr, stack: Stack):
        rb = [0]*len(arr)
        for i in range(-1, -len(arr) - 1, -1):
            while not stack.is_empty() and stack.top() < arr[i]:
                stack.pop()
            bound = 0 if stack.top() is None else stack.top()
            rb[i] = bound
            if stack.is_empty():
                stack.push(arr[i])
        return rb

    @staticmethod
    def trap_rainwater(arr):
        stack = Stack()
        lb = Solution._get_left_bounds(arr, stack)
        stack.clear()
        rb = Solution._get_right_bounds(arr, stack)
        stack.clear()
        n = len(arr)
        water_collected = 0
        for i in range(n):
            if lb[i] != 0 and rb[i] != 0:
                water_collected += (min(lb[i], rb[i]) - arr[i])
        return water_collected


print(Solution.trap_rainwater([3, 0, 1, 0, 4, 0, 2]))
print(Solution.trap_rainwater([3, 0, 2, 0, 4]))
print(Solution.trap_rainwater([1, 2, 3, 4]))
print(Solution.trap_rainwater([2, 1, 5, 3, 1, 0, 4]))
