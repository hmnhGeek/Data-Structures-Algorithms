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
        return item

    def top(self):
        if self.is_empty():
            return
        return self.head.data


class Solution:
    @staticmethod
    def convert_to_postfix(expr):
        operators = ["+", "-", "*", "/"]
        result = ""
        if expr[0] != "(":
            expr = "(" + expr + ")"
        n = len(expr)
        stack = Stack()
        for i in range(n):
            if expr[i] == "(" or expr[i] in operators:
                stack.push(expr[i])
            elif expr[i] == ")":
                while not stack.top() == "(":
                    result += stack.pop()
                stack.pop()
            else:
                result += expr[i]
        return result


print(Solution.convert_to_postfix("(2+4)*(4+6)"))