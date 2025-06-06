# Problem link - https://www.geeksforgeeks.org/move-last-element-to-front-of-a-given-linked-list/


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

    def __len__(self):
        return self.length

    def __str__(self):
        if self.length == 0:
            return "[]"
        if self.length == 1:
            return f"[{self.head.data}]"
        result = f"[{self.head.data}, "
        curr = self.head.next
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def move_tail_to_front(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        if self.length == 0 or self.length == 1:
            return
        prev, curr = None, self.head
        while curr != self.tail:
            prev = curr
            curr = curr.next
        prev.next = None
        self.tail = prev
        curr.next = self.head
        self.head = curr


# Example 1
l1 = LinkedList()
l1.build(2, 5, 6, 2, 1)
print(l1)
l1.move_tail_to_front()
print(l1)

# Example 2
l2 = LinkedList()
l2.build(1, 2, 3, 4, 5)
print(l2)
l2.move_tail_to_front()
print(l2)
