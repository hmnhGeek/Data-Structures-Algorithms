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

    def get_top(self):
        if self.is_empty():
            return
        return self.head.data


class Solution:
    @staticmethod
    def get_next_greater_elements(arr):
        stack = Stack()
        n = len(arr)
        result = [None]*n
        for i in range(-1, -n - 1, -1):
            if stack.get_top() is None:
                result[i] = -1
                stack.push(arr[i])
                continue
            while not stack.is_empty() and stack.get_top() <= arr[i]:
                stack.pop()
            if stack.is_empty():
                result[i] = -1
            elif stack.get_top() > arr[i]:
                result[i] = stack.get_top()
            stack.push(arr[i])
        return result


print(Solution.get_next_greater_elements([1, 3, 2, 4]))
print(Solution.get_next_greater_elements([6, 8, 0, 1, 3]))
print(Solution.get_next_greater_elements([10, 20, 30, 50]))
print(Solution.get_next_greater_elements([50, 40, 30, 10]))
