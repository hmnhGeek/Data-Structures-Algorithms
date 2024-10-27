# Problem link - https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1


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

    def build(self, l):
        for i in l:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def remove_duplicates(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # HEAD node will always remain the same because we are only removing curr nodes.
        # HEAD is never curr.
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if prev.data == curr.data:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        # However, TAIL node needs to be taken care of. If the last node is repeating, all the nodes
        # post prev will be deleted. Hence, the new tail will be prev node.
        if prev.next is None:
            self.tail = prev


# Example 1
l1 = LinkedList()
l1.build([2, 2, 4, 5, 5, 5])
l1.show()
l1.remove_duplicates()
l1.show()

print()

# Example 2
l1 = LinkedList()
l1.build([2, 2, 2, 2, 2, 2])
l1.show()
l1.remove_duplicates()
l1.show()