# Problem link - https://www.geeksforgeeks.org/problems/circular-linked-list/1


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

    def is_circular(self):
        """
            Time complexity is O(1) and space complexity is O(1).
        """
        if self.is_empty():
            return False
        return self.tail.next is not None


l = LinkedList()
l.build(1, 2, 3, 4, 5, 5)
l.tail.next = l.head
print(l.is_circular())

l1 = LinkedList()
l1.build(1, 2, 3)
print(l1.is_circular())
