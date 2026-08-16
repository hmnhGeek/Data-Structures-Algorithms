# Problem link - https://www.geeksforgeeks.org/dsa/expression-contains-redundant-bracket-not/


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
        self.head = self.head.next
        self.length -= 1
        return item

    def top(self):
        return self.head.data if self.head else None


class Solution:
    @staticmethod
    def check_redundant_brackets(expr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        stack = Stack()
        for i in range(len(expr)):
            character = expr[i]
            if character == '(' or character in ['+', '-', '/', '*']:
                stack.push(character)
            elif character == ')':
                if stack.top() == '(':
                    return True
                while not stack.top() == '(':
                    stack.pop()
                stack.pop()
        return False


print(Solution.check_redundant_brackets("((a+b))"))
print(Solution.check_redundant_brackets("((a+b)*c)"))
print(Solution.check_redundant_brackets("(a+(b)/c)"))
