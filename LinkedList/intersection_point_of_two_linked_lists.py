class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" --> ")
            curr = curr.next
        print()

    def intersect_with(self, node: Node):
        self.tail.next = node
        while self.tail.next is not None:
            self.tail = self.tail.next
            self.length += 1


class Solution:
    @staticmethod
    def get_intersection_node(l1: LinkedList, l2: LinkedList) -> Node:
        n, m = l1.length, l2.length
        delta = abs(n - m)
        curr1, curr2 = l1.head, l2.head

        if n > m:
            counter = 0
            while counter != delta:
                curr1 = curr1.next
                counter += 1
        else:
            counter = 0
            while counter != delta:
                curr2 = curr2.next
                counter += 1

        while curr1 is not None and curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1.data if curr1 else None


# Example 1
l1 = LinkedList()
l1.build(4, 1, 8, 4, 5)
l1.show()
l2 = LinkedList()
l2.build(5, 6, 1)
l2.intersect_with(l1.head.next.next)
l2.show()
print(Solution.get_intersection_node(l1, l2))



