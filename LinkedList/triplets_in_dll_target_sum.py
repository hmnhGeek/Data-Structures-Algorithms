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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class Solution:
    @staticmethod
    def solve(dll: DoublyLinkedList, target: int):
        n = dll.length
        i = dll.head
        ans = set()
        while i is not None:
            j, k = i.next, dll.tail
            while j and k and j != k and j.prev != k and k.next != j:
                tgt = i.data + j.data + k.data
                if tgt == target:
                    ans.add((i.data, j.data, k.data))
                    j = j.next
                    k = k.prev
                elif tgt > target:
                    k = k.prev
                else:
                    j = j.next
            i = i.next
        return ans


def test(l, target):
    dll = DoublyLinkedList()
    dll.build(*l)
    print(Solution.solve(dll, target))


test([1, 2, 3, 4], 8)
test([1, 2, 3, 4, 5, 6, 7], 17)
test([1, 2, 3, 8, 9], 13)
test([1, 2, 3, 4, 5, 6, 7, 8, 9], 15)
test([7, 33, 88, 91], 40)
test([3, 7, 9, 23, 45], 19)
test([8, 13, 16], 37)