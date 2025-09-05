# Problem link - https://www.geeksforgeeks.org/problems/sort-a-linked-list/1
# Solution - https://www.youtube.com/watch?v=8ocB7a_c-Cc


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


class MergeSort:
    @staticmethod
    def find_middle_node(l: LinkedList):
        slow = l.head
        fast = l.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def sort(l: LinkedList):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """
        if l.length == 1:
            return l
        middle_node = MergeSort.find_middle_node(l)
        left = LinkedList()
        left.head = l.head
        left.tail = middle_node
        left.length = l.length//2 + 1 if l.length % 2 == 1 else l.length//2
        right = LinkedList()
        right.head = middle_node.next
        right.tail = l.tail
        right.length = l.length//2
        middle_node.next = None
        left = MergeSort.sort(left)
        right = MergeSort.sort(right)
        return MergeSort.merge(left, right)

    @staticmethod
    def merge(left, right):
        merged = LinkedList()
        i, j = left.head, right.head
        while i is not None and j is not None:
            if i.data <= j.data:
                merged.push(i.data)
                i = i.next
            else:
                merged.push(j.data)
                j = j.next
        while i is not None:
            merged.push(i.data)
            i = i.next
        while j is not None:
            merged.push(j.data)
            j = j.next
        return merged


l = LinkedList()
l.build(40, 20, 60, 10, 50, 30)
print(l)
l = MergeSort.sort(l)
print(l)

print()

l2 = LinkedList()
l2.build(9, 5, 2, 8)
print(l2)
print(MergeSort.sort(l2))