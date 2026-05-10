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
    def sort(stack: Stack):
        Solution._sort(stack.head)

    @staticmethod
    def _sort(stack: Stack):
        if stack.head is None or stack.head.next is None:
            return stack
        middle_node = Solution._get_middle_node(stack)
        second_head = middle_node.next
        middle_node.next = None
        first = Stack()
        first.head = stack.head
        first.tail = middle_node
        first.length = stack.length // 2 if stack.length % 2 == 0 else stack.length // 2 + 1
        second = Stack()
        second.head = second_head
        second.tail = stack.tail
        second.length = stack.length // 2
        first = Solution._sort(first)
        second = Solution._sort(second)
        return Solution._merge(first, second)
