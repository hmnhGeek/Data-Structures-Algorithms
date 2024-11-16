# Problem link - https://www.naukri.com/code360/problems/arithmetic-expression-evaluation_1170517
# Solution (infix to postfix) - https://www.youtube.com/watch?v=_PU5t-gk_B4
# Solution (evaluating postfix) - https://www.youtube.com/watch?v=m7SGekhd1mQ


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
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        stack = Stack()
        n = len(infix_expression)
        postfix = ""

        # iterate over each character in the infix expression.
        for i in range(n):
            elem = infix_expression[i]

            # if the character is an operand (or a whitespace), add it to the postfix expression.
            if elem not in ExpressionEvaluator._brackets and elem not in ExpressionEvaluator._precedences:
                postfix += elem

            # else if the character is an opening bracket, then push it to the stack.
            elif elem == ExpressionEvaluator._brackets[0]:
                stack.push(elem)

            # else if the character is a closing bracket,
            elif elem == ExpressionEvaluator._brackets[1]:
                # then continuously pop from the stack until you get the corresponding opening bracket.
                while stack.top() != ExpressionEvaluator._brackets[0]:
                    # and while popping, push the popped characters into the postfix expression.
                    postfix += stack.pop()
                # pop the opening bracket.
                stack.pop()
            else:
                # finally, ensure that the top element is an operator and continuously pop from the stack unless the
                # top operator has a lower precedence than the current character.
                while stack.top() in ExpressionEvaluator._precedences and ExpressionEvaluator._precedences[stack.top()] >= ExpressionEvaluator._precedences[elem]:
                    postfix += stack.pop()
                # once the top is either an operator with lower precedence or just an opening bracket, push the current
                # character on the stack.
                stack.push(elem)

        # finally, if the expression got exhausted, pop from the stack until the stack gets empty.
        while not stack.is_empty():
            postfix += stack.pop()

        # return the postfix expression.
        return postfix.strip()

    @staticmethod
    def evaluate_postfix(postfix: str):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        stack = Stack()

        # get a list of operators and operands.
        literals = postfix.split()

        # loop on the literals in O(n) time.
        for literal in literals:
            # if literal is an operand, push the integer version of it in the stack.
            if literal not in ExpressionEvaluator._precedences:
                stack.push(int(literal))
            else:
                # else, if literal is an operator, pop the top 2 elements from the stack and perform the operation.
                # once operation is performed, push back the integer into the stack.
                x = stack.pop()
                y = stack.pop()
                if literal == "+":
                    stack.push(x + y)
                elif literal == "-":
                    stack.push(y - x)
                elif literal == "*":
                    stack.push(y * x)
                elif literal == "/":
                    stack.push(y // x)
                elif literal == "^":
                    stack.push(y ** x)

        # at last, there will be only one element in the stack which would be the final result.
        return stack.pop()

    @staticmethod
    def evaluate(expression):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # get the corresponding postfix expression in O(n) time and O(n) space.
        postfix = ExpressionEvaluator.infix_to_postfix(expression)
        # return the evaluated postfix expression in O(n) time and O(n) space.
        return ExpressionEvaluator.evaluate_postfix(postfix)


print(ExpressionEvaluator.infix_to_postfix("( ( 2 + 3 ) * ( 5 / 2 ) )"))
print(ExpressionEvaluator.infix_to_postfix("( 121 + ( 101 + 0 ) )"))
print(ExpressionEvaluator.infix_to_postfix("( 3 * ( 5 + 2 ) * ( 10 - 7 ) )"))
print(ExpressionEvaluator.evaluate("( ( 2 + 3 ) * ( 5 / 2 ) )"))
print(ExpressionEvaluator.evaluate("( 121 + ( 101 + 0 ) )"))
print(ExpressionEvaluator.evaluate("( 3 * ( 5 + 2 ) * ( 10 - 7 ) )"))