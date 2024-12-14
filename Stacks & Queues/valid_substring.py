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
    def get_valid(string):
        stack = Stack()
        stack.push(-1)
        max_length = 0
        for i in range(len(string)):
            bracket = string[i]
            if bracket == "(":
                stack.push(i)
            else:
                stack.pop()
                if stack.is_empty():
                    stack.push(i)
                else:
                    length = i - stack.top()
                    max_length = max(length, max_length)
        return max_length


print(Solution.get_valid("()(())("))
print(Solution.get_valid("(()("))
print(Solution.get_valid("(()())"))
print(Solution.get_valid("((()"))
print(Solution.get_valid(")()())"))
