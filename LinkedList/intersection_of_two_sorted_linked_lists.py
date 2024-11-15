class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def _build(self, _list):
        for i in _list:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class Solution:
    @staticmethod
    def intersect_linked_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
        i, j = l1.head, l2.head
        l3 = LinkedList()
        while i is not None and j is not None:
            if i.data == j.data:
                l3.push(i.data)
                i = i.next
                j = j.next
            elif i.data < j.data:
                i = i.next
            else:
                j = j.next
        return l3


def test(a1, a2):
    l1 = LinkedList()
    l2 = LinkedList()
    l1._build(a1)
    l2._build(a2)
    l3 = Solution.intersect_linked_lists(l1, l2)
    l3.show()


test([1, 2, 2, 3, 4, 4, 5], [1, 4, 4, 5, 5])
test([1, 2, 3, 4, 6], [2, 4, 6, 8])
test([10, 20, 40, 50], [15, 40])