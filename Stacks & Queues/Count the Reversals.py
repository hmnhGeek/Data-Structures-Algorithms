# Problem link - https://www.geeksforgeeks.org/problems/count-the-reversals0401/1
# Solution - https://www.youtube.com/watch?v=-n_CsIL3Ts4


from math import ceil


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
    def count_reversals(brackets):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        n = len(brackets)

        # if there are odd number of brackets, return -1.
        if n % 2 == 1:
            return -1

        # create a stack and store counts of opening and closing brackets.
        stack = Stack()
        count_open = 0
        count_closed = 0

        # loop on each index of the brackets.
        for i in range(n):
            # if it's an opening bracket simply push to stack
            if brackets[i] == "{":
                stack.push(brackets[i])
                count_open += 1

            # if it's a closing bracket and the top of the stack is an opening bracket, pop from the stack and decrement
            # the count of open brackets.
            elif brackets[i] == "}" and not stack.is_empty() and stack.top() == "{":
                stack.pop()
                count_open -= 1
            else:
                # else, it was a closing bracket and stack was empty, so increase the closing bracket count.
                count_closed += 1

        # the minimum number of operations would be ceil(open/2) + ceil(close/2).
        return ceil(count_open/2) + ceil(count_closed/2)


print(Solution.count_reversals("}{{}}{{{"))
print(Solution.count_reversals("{{}{{{}{{}}{{"))
print(Solution.count_reversals("}{"))
print(Solution.count_reversals("{{{"))
print(Solution.count_reversals("{{{{"))
print(Solution.count_reversals("{{{{}}"))
print(Solution.count_reversals("}}}{{{"))
