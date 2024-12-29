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
    def is_stack_permutation(arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        stack = Stack()
        i, j = 0, 0
        while i < len(arr1):
            while stack.top() == arr2[j]:
                stack.pop()
                j += 1
            stack.push(arr1[i])
            i += 1
        while j < len(arr2) and stack.top() == arr2[j]:
            stack.pop()
            j += 1
        return stack.is_empty()


print(Solution.is_stack_permutation([1, 2, 3], [2, 1, 3]))
print(Solution.is_stack_permutation([1, 2, 3], [3, 1, 2]))
print(Solution.is_stack_permutation([1,2,3,4,5],[4, 5, 3, 2, 1]))
print(Solution.is_stack_permutation([1,2,3,4,5],[4, 3, 5, 1, 2]))
