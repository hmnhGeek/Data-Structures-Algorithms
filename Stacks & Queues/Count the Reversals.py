from math import ceil


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


class Solution:
    @staticmethod
    def count_reversals(brackets):
        n = len(brackets)
        if n % 2 == 1:
            return -1
        stack = Stack()
        count_open = 0
        count_closed = 0
        for i in range(n):
            if brackets[i] == "{":
                stack.push(brackets[i])
                count_open += 1
            elif brackets[i] == "}" and not stack.is_empty() and stack.top() == "{":
                stack.pop()
                count_open -= 1
            else:
                count_closed += 1
        return ceil(count_open/2) + ceil(count_closed/2)


print(Solution.count_reversals("}{{}}{{{"))
print(Solution.count_reversals("{{}{{{}{{}}{{"))