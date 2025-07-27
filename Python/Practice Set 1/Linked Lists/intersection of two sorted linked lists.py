# Problem link - https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1


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

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result


class Solution:
    @staticmethod
    def find_intersection(l1: LinkedList, l2: LinkedList) -> LinkedList:
        """
            Time complexity is O(n + m) and space complexity is O(n + m).
        """
        l3 = LinkedList()
        curr1 = l1.head
        curr2 = l2.head
        while curr1 is not None and curr2 is not None:
            if curr1.data == curr2.data:
                l3.push(curr1.data)
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1.data < curr2.data:
                curr1 = curr1.next
            else:
                curr2 = curr2.next
        return l3


l1 = LinkedList()
l1.build(1, 2, 3, 4, 6)
l2 = LinkedList()
l2.build(2, 4, 6, 8)
l3 = Solution.find_intersection(l1, l2)
print(l3)

l1 = LinkedList()
l1.build(10, 20, 40, 50)
l2 = LinkedList()
l2.build(40)
l3 = Solution.find_intersection(l1, l2)
print(l3)

l1 = LinkedList()
l1.build(10, 20, 40, 50)
l2 = LinkedList()
l2.build(100)
l3 = Solution.find_intersection(l1, l2)
print(l3)