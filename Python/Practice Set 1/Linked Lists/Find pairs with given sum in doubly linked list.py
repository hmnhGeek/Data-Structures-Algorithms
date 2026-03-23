class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
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
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)


class Solution:
    @staticmethod
    def find_pairs(dll: DoublyLinkedList, target: int):
        pairs = []
        if dll.is_empty():
            return pairs
        i, j = dll.head, dll.tail
        while i != j and j.next != i:
            _sum = i.data + j.data
            if _sum == target:
                pairs.append((i.data, j.data))
                i = i.next
                j = j.prev
            elif _sum > target:
                j = j.prev
            else:
                i = i.next
        return pairs


def test(l, target):
    dll = DoublyLinkedList()
    dll.build(*l)
    print(Solution.find_pairs(dll, target))
    print()


test([1, 5, 6], 6)
test([1, 2, 4, 5, 6, 8, 9], 7)
test([1, 2, 3, 4, 9], 5)
test([1, 10, 11, 12, 27], 7)
