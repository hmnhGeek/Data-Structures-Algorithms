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


class ExpressionEvaluator:
    _precedences = {None: -1, "+": 0, "-": 0, "/": 1, "*": 1, "^": 2}
    _brackets = ["(", ")"]

    @staticmethod
    def infix_to_postfix(infix_expression: str):
        stack = Stack()
        n = len(infix_expression)
        postfix = ""
        for i in range(n):
            elem = infix_expression[i]
            if elem not in ExpressionEvaluator._brackets and elem not in ExpressionEvaluator._precedences:
                postfix += elem
            elif elem == ExpressionEvaluator._brackets[0]:
                stack.push(elem)
            elif elem == ExpressionEvaluator._brackets[1]:
                while stack.top() != ExpressionEvaluator._brackets[0]:
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack.top() in ExpressionEvaluator._precedences and ExpressionEvaluator._precedences[stack.top()] >= ExpressionEvaluator._precedences[elem]:
                    postfix += stack.pop()
                stack.push(elem)
        while not stack.is_empty():
            postfix += stack.pop()
        return postfix


print(ExpressionEvaluator.infix_to_postfix("((2+3)*(5/2))"))
print(ExpressionEvaluator.infix_to_postfix("(121+(101+0))"))
print(ExpressionEvaluator.infix_to_postfix("(3 * (5 + 2) * (10 - 7))"))