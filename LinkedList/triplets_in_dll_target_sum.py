# Problem link - https://www.geeksforgeeks.org/count-triplets-sorted-doubly-linked-list-whose-sum-equal-given-value-x/#expected-approach-using-two-pointers-on2-time-and-o1-space
# Solution - https://www.youtube.com/watch?v=jn2oe9GhkRg


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
        """
            Time complexity is O(n^2) and space complexity is O(1).
        """

        # start i from the first element
        i = dll.head
        ans = set()

        # This will run for n times.
        while i is not None:
            # define j = i + 1 and k = n - 1
            j, k = i.next, dll.tail

            # while j <= k:
            while j and k and j != k and j.prev != k and k.next != j:
                # get sum of (i, j, k).
                tgt = i.data + j.data + k.data

                # tgt matches with target, add the triplet, and move j to j + 1 and k to k - 1.
                if tgt == target:
                    ans.add((i.data, j.data, k.data))
                    j = j.next
                    k = k.prev

                # elif tgt > target, reduce k
                elif tgt > target:
                    k = k.prev
                else:
                    # else increment k
                    j = j.next
            # move to next i.
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
test([1, 2, 4, 5, 6, 8, 9], 17)
test([1, 2, 4, 5, 6, 8, 9], 15)
