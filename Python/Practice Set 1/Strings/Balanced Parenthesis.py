# Problem link - https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1


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
    brackets_map = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    @staticmethod
    def balanced_parenthesis(string: str) -> bool:
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        stack = Stack()
        for i in range(len(string)):
            bracket = string[i]
            if bracket in Solution.brackets_map.values():
                stack.push(bracket)
            else:
                if stack.is_empty():
                    return False
                if Solution.brackets_map[bracket] == stack.top():
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
