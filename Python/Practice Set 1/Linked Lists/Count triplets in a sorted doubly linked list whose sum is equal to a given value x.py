from typing import List


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
    def count_triplets(dll: DoublyLinkedList, target: int):
        if dll.is_empty() or dll.length == 1 or dll.length == 2:
            return []
        result = []
        i, j, k = dll.head, dll.head.next, dll.tail
        while i is not None and i != dll.tail.prev:
            while j is not None and k is not None and (j != k and j.prev != k):
                _sum = i.data + j.data + k.data
                if _sum == target:
                    result.append((i.data, j.data, k.data))
                    j = j.next
                    k = k.prev
                elif _sum > target:
                    k = k.prev
                else:
                    j = j.next
            i = i.next
            j = i.next
            k = dll.tail
        return result


def test(l, target):
    dll = DoublyLinkedList()
    dll.build(*l)
    print(Solution.count_triplets(dll, target))


test([1, 2, 3, 4], 8)
test([1, 2, 3, 4, 5, 6, 7], 17)
test([1, 2, 3, 8, 9], 13)
test([1, 2, 3, 4, 5, 6, 7, 8, 9], 15)
test([7, 33, 88, 91], 40)
test([3, 7, 9, 23, 45], 19)
test([8, 13, 16], 37)
test([1, 2, 4, 5, 6, 8, 9], 17)
test([1, 2, 4, 5, 6, 8, 9], 15)