# Problem link - https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1


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


class Utility:
    @staticmethod
    def is_digit(x):
        try:
            float(x)
            return True
        except:
            return False


class Solution:
    @staticmethod
    def evaluate(expr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        stack = Stack()
        for i in range(len(expr)):
            character = expr[i]
            if Utility.is_digit(character):
                stack.push(character)
                continue
            a, b = float(stack.pop()), float(stack.pop())
            if character == "+":
                stack.push(str(a + b))
            elif character == "-":
                stack.push(str(b - a))
            elif character == "*":
                stack.push(str(b * a))
            elif character == "/":
                stack.push(str(b / a))
            else:
                stack.push(str(b ** a))
        return stack.top()


print(Solution.evaluate(["2", "3", "1", "*", "+", "9", "-"]))
print(Solution.evaluate(["2", "3", "^", "1", "+"]))
print(Solution.evaluate(["2", "3", "1", "*", "+", "9", "-"]))
print(Solution.evaluate(["1", "2", "3", "+", "*", "8", "-"]))
print(Solution.evaluate(["100", "200", "+", "2", "/", "5", "*", "7", "+"]))
