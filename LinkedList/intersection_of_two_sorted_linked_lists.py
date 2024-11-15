# Problem link - https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1


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
        """
            Overall time complexity is O(n + m) and space complexity is O(n + m).
        """

        # initialize two pointers on the heads of both linked lists.
        i, j = l1.head, l2.head

        # initialize an output linked list.
        l3 = LinkedList()

        # while BOTH the linked lists have some elements to traverse.
        while i is not None and j is not None:
            # if the elements match, push the element into result list and move both pointers.
            if i.data == j.data:
                l3.push(i.data)
                i = i.next
                j = j.next
            # if `i` < `j`, traverse to the next l1 element.
            elif i.data < j.data:
                i = i.next
            # if `j` < `i`, traverse to the next l2 element
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
test([1, 1, 2, 3, 4], [2, 3, 4])
