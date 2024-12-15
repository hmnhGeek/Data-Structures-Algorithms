# Problem link - https://www.geeksforgeeks.org/find-pairs-given-sum-doubly-linked-list/#expected-approach-using-two-pointer-technique-on-time-and-o1-space


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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class Solution:
    @staticmethod
    def find_pairs(dll: DoublyLinkedList, target: int) -> List[tuple]:
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # keep left and right pointers on the extremes of the DLL.
        left, right = dll.head, dll.tail
        # keep a result variable to store the valid pairs
        result = []

        # while left is coming before right
        while left != right and (not right.next == left):
            _sum = left.data + right.data
            # if sum == target, add the (left, right) pair in the result and move both pointers.
            if _sum == target:
                result.append((left.data, right.data))
                left = left.next
                right = right.prev
            elif _sum > target:
                # if sum is larger than target, we must reduce from right
                right = right.prev
            else:
                # else if sum is smaller than target, we must increase sum by increasing left
                left = left.next
        # return the result
        return result


def test(l, target):
    dll = DoublyLinkedList()
    dll.build(*l)
    dll.show()
    print(Solution.find_pairs(dll, target))
    print()


test([1, 5, 6], 6)
test([1, 2, 4, 5, 6, 8, 9], 7)
test([1, 2, 3, 4, 9], 5)
test([1, 10, 11, 12, 27], 7)
