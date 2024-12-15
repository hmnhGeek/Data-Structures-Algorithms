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
    def redundant_brackets(expression: str) -> bool:
        stack = Stack()
        for i in range(len(expression)):
            char = expression[i]
            if char in ["(", "+", "-", "*", "/"]:
                stack.push(char)
            elif char == ")":
                redundant_present = True
                while stack.top() != "(":
                    if stack.top() in ["+", "-", "*", "/"]:
                        redundant_present = False
                    stack.pop()
                if redundant_present:
                    return True
                stack.pop()
        return False


print(Solution.redundant_brackets("((a+b))"))
print(Solution.redundant_brackets("(a+(b)/c)"))
print(Solution.redundant_brackets("(a+b+(c+d))"))
print(Solution.redundant_brackets("(a+b)"))
print(Solution.redundant_brackets("(a+c*b)+(c))"))
print(Solution.redundant_brackets("(a*b+(c/d))"))
print(Solution.redundant_brackets("((a/b))"))
