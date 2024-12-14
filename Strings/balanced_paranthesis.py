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
    _map = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    @staticmethod
    def balanced_parenthesis(string):
        stack = Stack()
        for i in range(len(string)):
            elem = string[i]
            if elem in ["[", "{", "("]:
                stack.push(elem)
            elif stack.top() == Solution._map[elem]:
                stack.pop()
            else:
                return False
        return stack.is_empty()


print(Solution.balanced_parenthesis("{([])}"))
print(Solution.balanced_parenthesis("([]"))
print(Solution.balanced_parenthesis("()"))
print(Solution.balanced_parenthesis("[()]{}{[()()]()}"))
print(Solution.balanced_parenthesis("[(])"))
print(Solution.balanced_parenthesis("()[]{}"))
print(Solution.balanced_parenthesis("(]"))
print(Solution.balanced_parenthesis("{[(])}"))
