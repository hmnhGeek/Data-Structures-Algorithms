class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


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
        if self.is_empty():
            return "[]"
        curr = self.head
        result = "["
        while curr != self.tail:
            result += f"[{curr.data}, {curr.random.data if curr.random else None}], "
            curr = curr.next
        result += f"[{self.tail.data}, {self.tail.random.data if self.tail.random else None}]]"
        return result


class Solution:
    @staticmethod
    def clone(linked_list: LinkedList) -> LinkedList:
        cloned_linked_list = LinkedList()
        Solution.linear_clone(linked_list)
        Solution.clone_random_pointers(linked_list)
        Solution.extract_cloned_list(cloned_linked_list, linked_list)
        return cloned_linked_list

    @staticmethod
    def extract_cloned_list(cloned_linked_list, linked_list):
        dummy = temp = Node(None)
        curr = linked_list.head
        while curr is not None:
            temp.next = curr.next
            curr.next = curr.next.next
            temp = temp.next
            curr = curr.next
        cloned_linked_list.head = dummy.next
        cloned_linked_list.tail = temp
        cloned_linked_list.length = linked_list.length

    @staticmethod
    def clone_random_pointers(linked_list: LinkedList):
        curr = linked_list.head
        while curr is not None:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

    @staticmethod
    def linear_clone(linked_list: LinkedList):
        curr = linked_list.head
        while curr is not None:
            cloned_curr = Node(curr.data)
            next_curr = curr.next
            curr.next = cloned_curr
            cloned_curr.next = next_curr
            curr = next_curr


# Example 1
l = LinkedList()
for i in [1, 2, 3, 4, 5]:
    l.push(i)
l.head.random = l.head.next.next
l.head.next.random = l.head
l.head.next.next.next.random = l.head.next.next
l.tail.random = l.head.next
print(l)
cloned = Solution.clone(l)
print(cloned)
print()

# Example 2
l = LinkedList()
for i in [7, 13, 11, 10, 1]:
    l.push(i)
l.head.next.random = l.head
l.head.next.next.random = l.tail
l.head.next.next.next.random = l.head.next.next
l.tail.random = l.head
print(l)
cloned = Solution.clone(l)
print(cloned)