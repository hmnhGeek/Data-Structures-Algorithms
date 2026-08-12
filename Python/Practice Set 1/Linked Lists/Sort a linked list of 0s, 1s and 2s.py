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
        if self.is_empty():
            return "[]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result


class Solution:
    @staticmethod
    def sort(linked_list: LinkedList):
        dummy_zero = temp_zero = Node(None)
        dummy_one = temp_one = Node(None)
        dummy_two = temp_two = Node(None)
        curr = linked_list.head
        while curr is not None:
            if curr.data == 0:
                temp_zero.next = curr
                temp_zero = curr
            elif curr.data == 1:
                temp_one.next = curr
                temp_one = curr
            else:
                temp_two.next = curr
                temp_two = curr
            curr = curr.next

        a = dummy_zero.next
        b = dummy_one.next
        c = dummy_two.next

        if a is None and b is None and c is None:
            return
        elif a is None and b is None and c is not None:
            linked_list.head = dummy_two.next
            linked_list.tail = temp_two
        elif a is None and b is not None and c is None:
            linked_list.head = dummy_one.next
            linked_list.tail = temp_one
        elif a is None and b is not None and c is not None:
            linked_list.head = dummy_one.next
            temp_one.next = dummy_two.next
            linked_list.tail = temp_two
        elif a is not None and b is None and c is None:
            linked_list.head = dummy_zero.next
            linked_list.tail = temp_zero
        elif a is not None and b is None and c is not None:
            linked_list.head = dummy_zero.next
            temp_zero.next = dummy_two.next
            linked_list.tail = temp_two
        elif a is not None and b is not None and c is None:
            linked_list.head = dummy_zero.next
            temp_zero.next = dummy_one.next
            linked_list.tail = temp_one
        else:
            linked_list.head = dummy_zero.next
            temp_zero.next = dummy_one.next
            temp_one.next = dummy_two.next
            linked_list.tail = temp_two


l = LinkedList()
for i in [1, 2, 2, 1, 2, 0, 2, 2]:
    l.push(i)
print(l)
Solution.sort(l)
print(l)

print()

l2 = LinkedList()
for i in [2, 2, 0, 1]:
    l2.push(i)
print(l2)
Solution.sort(l2)
print(l2)

print()
l3 = LinkedList()
for i in [1, 1, 2, 0, 2, 0, 1]:
    l3.push(i)
print(l3)
Solution.sort(l3)
print(l3)

print()
l4 = LinkedList()
for i in [1, 1, 2, 1, 2, 2, 1]:
    l4.push(i)
print(l4)
Solution.sort(l4)
print(l4)

print()
l5 = LinkedList()
for i in [0, 2, 2, 2, 0, 0, 0, 0, 2, 2]:
    l5.push(i)
print(l5)
Solution.sort(l5)
print(l5)

print()
l6 = LinkedList()
for i in [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]:
    l6.push(i)
print(l6)
Solution.sort(l6)
print(l6)

print()
l7 = LinkedList()
for i in [0, 0, 0, 0, 0]:
    l7.push(i)
print(l7)
Solution.sort(l7)
print(l7)

print()
l8 = LinkedList()
for i in [1, 1, 1, 1, 1, 1]:
    l8.push(i)
print(l8)
Solution.sort(l8)
print(l8)

print()
l9 = LinkedList()
for i in [2, 2, 2, 2, 2]:
    l9.push(i)
print(l9)
Solution.sort(l9)
print(l9)

print()
l10 = LinkedList()
for i in []:
    l10.push(i)
print(l10)
Solution.sort(l10)
print(l10)