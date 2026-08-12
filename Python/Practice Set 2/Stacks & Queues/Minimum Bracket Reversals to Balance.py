# Problem link - https://www.geeksforgeeks.org/problems/count-the-reversals0401/1
# Solution - https://www.youtube.com/watch?v=-n_CsIL3Ts4


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
    def min_reversals(brackets):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        n = len(brackets)
        if n % 2 == 1:
            return
        stack = Stack()
        open_count = close_count = 0
        for i in range(len(brackets)):
            bracket = brackets[i]
            if bracket == "{":
                stack.push(bracket)
                open_count += 1
            elif not stack.is_empty():
                stack.pop()
                open_count -= 1
            else:
                close_count += 1
        if open_count % 2 == 0:
            open_count //= 2
        else:
            open_count = (open_count // 2) + 1
        if close_count % 2 == 0:
            close_count //= 2
        else:
            close_count = (close_count // 2) + 1
        return open_count + close_count


print(Solution.min_reversals("}{{}}{{{"))
print(Solution.min_reversals("{{}{{{}{{}}{{"))
print(Solution.min_reversals("{{"))
print(Solution.min_reversals("}{}{"))
