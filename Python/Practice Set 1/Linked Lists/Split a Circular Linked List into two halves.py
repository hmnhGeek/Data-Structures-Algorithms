# Problem link - https://www.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1


from math import ceil


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
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
        self.tail.next = self.head
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.length == 0:
            return "[]"
        curr = self.head
        result = "["
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def get_middle_node(self):
        if self.length == 0:
            return
        self.tail.next = None
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def split(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        if self.length == 0 or self.length == 1:
            return
        middle_node = self.get_middle_node()
        next_list_head = middle_node.next
        middle_node.next = None
        tail_of_next_list = self.tail
        old_length = self.length

        # construct linked list 1
        self.tail = middle_node
        self.tail.next = self.head
        self.length = ceil(self.length/2)

        # construct linked list 2
        second = CircularLinkedList()
        second.head = next_list_head
        second.tail = tail_of_next_list
        second.tail.next = next_list_head
        second.length = old_length - self.length

        return self, second


def test(*args):
    l = CircularLinkedList()
    for i in args:
        l.push(i)
    print(l)
    l1, l2 = l.split()
    print(l1)
    print(l2)
    print()


test(10, 4, 9)
test(10, 4, 9, 10)
test(1, 2, 3, 4, 4, 5)
