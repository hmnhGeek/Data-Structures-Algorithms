# Problem link - https://www.geeksforgeeks.org/problems/circular-linked-list/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def _push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def build(self, *args):
        for i in args:
            self._push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def is_circular(self):
        return self.tail.next is not None


l = LinkedList()
l.build(1, 2, 3, 4, 5, 5)
l.tail.next = l.head
print(l.is_circular())

l1 = LinkedList()
l1.build(1, 2, 3)
print(l1.is_circular())