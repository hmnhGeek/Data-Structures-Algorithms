# Problem link - https://www.geeksforgeeks.org/problems/reverse-a-string-using-stack/1


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
    @staticmethod
    def reverse(string: str):
        """
            Overall time complexity is O(n) and overall space complexity is O(n).
        """

        stack = Stack()

        # This will take O(n) time.
        for i in string:
            stack.push(i)

        # This will take O(n) time.
        result = ""
        while not stack.is_empty():
            result += stack.pop()
        return result


s1 = "GeeksForGeeks"
s1 = Solution.reverse(s1)
print(s1)