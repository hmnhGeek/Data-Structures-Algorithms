# Problem link - https://leetcode.com/problems/valid-parentheses/description/
# Solution - https://www.youtube.com/watch?v=xwjS0iZhw4I


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


class Solution:
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    @staticmethod
    def balanced_parenthesis(string):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        stack = Stack()

        # loop on the string
        for i in range(len(string)):
            # if the ith character is an opening bracket, push it to stack.
            if string[i] in ["(", "{", "["]:
                stack.push(string[i])
            else:
                # if it's a closing bracket, then first of all pop from the stack
                top = stack.pop()

                # if the top is None (stack is empty) or the opening of this closing bracket does not match with the
                # top of the stack, then the parenthesis are unbalanced, return False.
                if top is None or Solution.mapping[string[i]] != top:
                    return False

        # finally, if the stack got empty after full loop, return True, else False.
        return stack.is_empty()


print(Solution.balanced_parenthesis("())"))
print(Solution.balanced_parenthesis("[()]{}{[()()]()}"))
print(Solution.balanced_parenthesis("{([])}"))
print(Solution.balanced_parenthesis("()"))
print(Solution.balanced_parenthesis("([]"))
print(Solution.balanced_parenthesis("[(])"))
print(Solution.balanced_parenthesis("()[]{}"))
print(Solution.balanced_parenthesis("(]"))