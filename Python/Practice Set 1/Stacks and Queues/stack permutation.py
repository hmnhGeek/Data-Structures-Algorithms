# Problem link - https://www.geeksforgeeks.org/stack-permutations-check-if-an-array-is-stack-permutation-of-other/
# Solution - https://www.youtube.com/watch?v=q4CbTMLogyk&t=663s


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

    def top(self):
        if self.is_empty():
            return None
        return self.head.data


class Solution:
    @staticmethod
    def is_stack_permutation(a, b):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        stack = Stack()
        i, j = 0, 0
        while i < len(a):
            stack.push(a[i])
            i += 1
            while j < len(b) and stack.top() == b[j]:
                stack.pop()
                j += 1
        return stack.is_empty()


print(Solution.is_stack_permutation([1, 2, 3], [2, 1, 3]))
print(Solution.is_stack_permutation([1, 2, 3], [3, 1, 2]))
print(Solution.is_stack_permutation([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(Solution.is_stack_permutation([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
