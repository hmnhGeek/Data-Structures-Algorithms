# Problem link - https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1


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

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def get(self, index):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        if index not in range(self.length):
            raise IndexError("List index out of bounds.")
        counter = 0
        curr = self.head
        while counter != index:
            curr = curr.next
            counter += 1
        return curr

    def kth_from_end(self, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = self.length
        from_front_idx = n - k
        return self.get(from_front_idx)


l1 = LinkedList()
l1.build(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(l1, l1.kth_from_end(2).data)

l2 = LinkedList()
l2.build(10, 5, 100, 5)
print(l2, l2.kth_from_end(3).data)
