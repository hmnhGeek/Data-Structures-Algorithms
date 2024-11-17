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
    _operators = {"+", "-", "*", "/"}

    @staticmethod
    def evaluate_postfix(postfix):
        postfix = postfix.split()
        stack = Stack()
        for i in range(len(postfix)):
            if postfix[i] not in Solution._operators:
                stack.push(int(postfix[i]))
            else:
                a, b = stack.pop(), stack.pop()
                if postfix[i] == "+":
                    stack.push(b + a)
                elif postfix[i] == "-":
                    stack.push(b - a)
                elif postfix[i] == "*":
                    stack.push(b * a)
                else:
                    stack.push(b // a)
        return stack.pop()


print(Solution.evaluate_postfix("2 3 1 * + 9 -"))
print(Solution.evaluate_postfix("1 2 3 + * 8 -"))
print(Solution.evaluate_postfix("100 200 + 2 / 5 * 7 +"))