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


class Solution:
    _operators = {"+", "-", "*", "/"}

    @staticmethod
    def evaluate_postfix(postfix):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # split postfix expression by whitespace.
        postfix = postfix.split()

        # initialize a stack
        stack = Stack()

        # iterate on each element of the postfix list.
        for i in range(len(postfix)):
            # if the ith element is a operand, push it to stack.
            if postfix[i] not in Solution._operators:
                stack.push(int(postfix[i]))
            else:
                # else, if it's an operator, pop the top 2 operands from the stack
                # and perform the operation and push back the final result back on
                # the stack.
                a, b = stack.pop(), stack.pop()
                if postfix[i] == "+":
                    stack.push(b + a)
                elif postfix[i] == "-":
                    stack.push(b - a)
                elif postfix[i] == "*":
                    stack.push(b * a)
                else:
                    stack.push(b // a)
        # at last, if the postfix expression was valid, the stack will have only one element as the final result,
        # return it.
        return stack.pop()


print(Solution.evaluate_postfix("2 3 1 * + 9 -"))
print(Solution.evaluate_postfix("1 2 3 + * 8 -"))
print(Solution.evaluate_postfix("100 200 + 2 / 5 * 7 +"))