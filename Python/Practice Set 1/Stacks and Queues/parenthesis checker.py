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
    def balanced_parenthesis(brackets):
        stack = Stack()
        d = {"}": "{", "]": "[", ")": "("}
        opening_brackets = ["[", "{", "("]
        for i in range(len(brackets)):
            bracket = brackets[i]
            if bracket in opening_brackets:
                stack.push(bracket)
                continue
            top_bracket = stack.top()
            if d[bracket] != top_bracket:
                return False
            stack.pop()
        return stack.is_empty()


print(Solution.balanced_parenthesis("())"))
print(Solution.balanced_parenthesis("[()]{}{[()()]()}"))
print(Solution.balanced_parenthesis("{([])}"))
print(Solution.balanced_parenthesis("()"))
print(Solution.balanced_parenthesis("([]"))
print(Solution.balanced_parenthesis("[(])"))
print(Solution.balanced_parenthesis("()[]{}"))
print(Solution.balanced_parenthesis("(]"))
