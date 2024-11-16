# Problem link - https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1


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
        """
            Overall time complexity is thus O(|n - m| + min(n, m)) and space complexity is O(1).
        """

        # store the lengths of the linked lists
        n, m = l1.length, l2.length

        # get the absolute difference in the lengths of the lists
        delta = abs(n - m)

        # store pointers to the heads of both the lists
        curr1, curr2 = l1.head, l2.head

        # This will take O(|n - m|) time.
        # if l1 > l2 in size.
        if n > m:
            # move curr1 (of l1) by delta times, so that both curr1 and curr2 finish at the same time till the tail.
            counter = 0
            while counter != delta:
                curr1 = curr1.next
                counter += 1
        else:
            # move curr2 (of l2) by delta times, so that both curr1 and curr2 finish at the same time till the tail.
            counter = 0
            while counter != delta:
                curr2 = curr2.next
                counter += 1

        # now move both curr1 and curr2 together until curr1 goes None and both the pointers are not same. This will
        # run for smaller length list's length times. That is, O(min(n, m)).
        while curr1 is not None and curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next

        # There are two possibilities now. Either curr1 became None (and curr2 also) or, if they both are not None,
        # they must be pointing to the same node, i.e., intersection node. Return the intersection node.
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
print()

# Example 2
l1 = LinkedList()
l1.build(4, 4, 4)
l1.show()
l2 = LinkedList()
l2.build(4, 4, 4)
l2.intersect_with(l1.head.next)
l2.show()
print(Solution.get_intersection_node(l1, l2))
print()

# Example 3
l1 = LinkedList()
l1.build(3, 2, 4)
l1.show()
l2 = LinkedList()
l2.build(1, 9, 1)
l2.intersect_with(l1.head.next)
l2.show()
print(Solution.get_intersection_node(l1, l2))
print()

# Example 4
l1 = LinkedList()
l1.build(2, 6, 4)
l1.show()
l2 = LinkedList()
l2.build(1, 5)
l2.intersect_with(None)
l2.show()
print(Solution.get_intersection_node(l1, l2))
print()