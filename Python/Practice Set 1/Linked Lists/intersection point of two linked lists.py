# Problem link - https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1
# Solution - https://www.youtube.com/watch?v=0DYoPz2Tpt4


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

    def intersect_with(self, node: Node):
        self.tail.next = node
        while self.tail.next is not None:
            self.tail = self.tail.next
            self.length += 1


class Solution:
    @staticmethod
    def find_intersection_point(l1: LinkedList, l2: LinkedList):
        """
            Time complexity is O(n + m) and space complexity is O(1).
        """
        tracker = {"i": 0, "j": 1}
        i = l1.head
        j = l2.head
        while i != j:
            i = i.next
            j = j.next
            if i is None and j is None:
                return None
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
print()

# Example 2
l1 = LinkedList()
l1.build(4, 4, 4)
l2 = LinkedList()
l2.build(4, 4, 4)
l2.intersect_with(l1.head.next)
print(Solution.find_intersection_point(l1, l2))
print()

# Example 3
l1 = LinkedList()
l1.build(3, 2, 4)
l2 = LinkedList()
l2.build(1, 9, 1)
l2.intersect_with(l1.head.next)
print(Solution.find_intersection_point(l1, l2))
print()

# Example 4
l1 = LinkedList()
l1.build(2, 6, 4)
l2 = LinkedList()
l2.build(1, 5)
l2.intersect_with(None)
print(Solution.find_intersection_point(l1, l2))
print()

# Example 5
l1 = LinkedList()
l1.build(2, 6, 4)
print(Solution.find_intersection_point(l1, l1))
print()
