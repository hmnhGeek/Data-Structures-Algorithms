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


class Solution:
    @staticmethod
    def get_valid_substring(brackets):
        stack = Stack()
        max_length = 0
        counter = 0
        for i in range(len(brackets)):
            bracket = brackets[i]
            if bracket == "(":
                stack.push(bracket)
            else:
                if not stack.is_empty():
                    stack.pop()
                    counter += 2
                else:
                    max_length = max(max_length, counter)
                    counter = 0
        max_length = max(max_length, counter)
        return max_length


print(Solution.get_valid_substring("(()("))
print(Solution.get_valid_substring("()(())("))
print(Solution.get_valid_substring("(()())"))
print(Solution.get_valid_substring(")())"))
print(Solution.get_valid_substring("(()"))
print(Solution.get_valid_substring(")()())"))
print(Solution.get_valid_substring(""))
print(Solution.get_valid_substring("()))((())"))
print(Solution.get_valid_substring("))(("))
print(Solution.get_valid_substring("()))((((())))))"))
print(Solution.get_valid_substring(")(()"))