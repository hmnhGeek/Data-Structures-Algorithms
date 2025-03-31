# Problem link - https://www.geeksforgeeks.org/problems/expression-contains-redundant-bracket-or-not/0
# Solution - https://www.youtube.com/watch?v=BmZnJehDzyU&t=3105s


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
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        stack = Stack()
        for i in range(len(expression)):
            char = expression[i]
            # if the character is either an operator or opening bracket, push it to the stack.
            if char in ["(", "+", "-", "*", "/"]:
                stack.push(char)
            # if the character is a closing bracket
            elif char == ")":
                # assume the expression to have redundant brackets.
                redundant_present = True
                # while we don't find the opening bracket for this closing bracket...
                while stack.top() != "(":
                    # check if the top is an operator or not.
                    if stack.top() in ["+", "-", "*", "/"]:
                        # if it is an operator, then this bracket is not redundant.
                        redundant_present = False
                    # pop the top element from stack.
                    stack.pop()
                # if `redundant_present` is still true, return True.
                if redundant_present:
                    return True
                # pop the opening bracket
                stack.pop()
        # return False if every character has been checked.
        return False


print(Solution.redundant_brackets("((a+b))"))
print(Solution.redundant_brackets("(a+(b)/c)"))
print(Solution.redundant_brackets("(a+b+(c+d))"))
print(Solution.redundant_brackets("(a+b)"))
print(Solution.redundant_brackets("(a+c*b)+(c))"))
print(Solution.redundant_brackets("(a*b+(c/d))"))
print(Solution.redundant_brackets("((a/b))"))
