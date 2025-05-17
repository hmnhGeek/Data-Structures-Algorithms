# Problem link - https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1


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
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.length == 0:
            return "[]"
        if self.length == 1:
            return f"[{self.head.data}]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def remove_duplicates(self):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        mp = set()
        prev, curr = None, self.head
        while curr is not None:
            if curr.data not in mp:
                mp.add(curr.data)
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
                self.length -= 1
        self.tail = prev


l1 = LinkedList()
l1.build(5, 2, 2, 4)
print(l1)
l1.remove_duplicates()
print(l1)

l2 = LinkedList()
l2.build(2, 2, 2, 2, 2)
print(l2)
l2.remove_duplicates()
print(l2)

l3 = LinkedList()
l3.build(1)
print(l3)
l3.remove_duplicates()
print(l3)

l4 = LinkedList()
l4.build(2, 4, 8, 9, 3, 5, 9, 0, 5, 3, 4, 0)
print(l4)
l4.remove_duplicates()
print(l4)
