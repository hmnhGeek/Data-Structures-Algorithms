# Problem link - https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
            self.tail = node
        self.length += 1

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def build(self, *args):
        for i in args:
            self.push(i)

    def has_loop(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_loop(self):
        """
            Time complexity is O(1) and space complexity is O(1).
        """
        self.tail.next = None


# Example 1
l1 = LinkedList()
l1.build(1, 2, 3, 4, 5)
l1.show()
print(l1.has_loop())
l1.tail.next = l1.head.next
print(l1.has_loop())
l1.remove_loop()
print(l1.has_loop())

# Example 2
l2 = LinkedList()
l2.build(1, 2, 3, 4, 10, -19)
l2.show()
print(l2.has_loop())
l2.tail.next = l2.head.next.next
print(l2.has_loop())
l2.remove_loop()
print(l2.has_loop())