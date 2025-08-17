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


class Solution:
    @staticmethod
    def find_intersection_point(l1: LinkedList, l2: LinkedList):
        tracker = {"i": 0, "j": 1}
        i = l1.head
        j = l2.head
        while i != j:
            i = i.next
            j = j.next
            if i is None:
                if tracker["i"] == 0:
                    i = l2.head
                    tracker["i"] = 1
                else:
                    i = l1.head
                    tracker["i"] = 0
            if j is None:
                if tracker["j"] == 0:
                    j = l2.head
                    tracker["j"] = 1
                else:
                    j = l1.head
                    tracker["j"] = 0
        return i.data if i is not None else -1


# Example 1
l1 = LinkedList()
l1.build(4, 1, 8, 4, 5)
l2 = LinkedList()
l2.build(5, 6, 1)
l2.tail.next = l1.head.next.next
l2.tail = l1.tail
print(Solution.find_intersection_point(l1, l2))
