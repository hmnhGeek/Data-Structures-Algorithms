class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
            self.tail.next = node
            self.tail = node
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def get_num(self):
        curr = self.head
        num = 0
        while curr is not None:
            num = (num * 10) + curr.data
            curr = curr.next
        return num


class Solution:
    @staticmethod
    def multiply(l1: LinkedList, l2: LinkedList) -> int:
        n1 = l1.get_num()
        n2 = l2.get_num()
        return (n1 * n2) % (10**9 + 7)


# Example 1
l1, l2 = LinkedList(), LinkedList()
l1.build(3, 2)
l2.build(2)
print(Solution.multiply(l1, l2))

# Example 2
l1, l2 = LinkedList(), LinkedList()
l1.build(1, 0, 0)
l2.build(1, 0)
print(Solution.multiply(l1, l2))
