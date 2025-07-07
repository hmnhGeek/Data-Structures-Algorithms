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
        if self.length == 2:
            return f"[{self.head.data}, {self.tail.data}]"
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def reverse(self):
        if self.length == 0 or self.length == 1:
            return
        prev = None
        curr = self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head


class Solution:
    @staticmethod
    def add(l1: LinkedList, l2: LinkedList):
        l1.reverse()
        l2.reverse()
        result = LinkedList()
        carry = 0
        curr1, curr2 = l1.head, l2.head
        while curr1 is not None and curr2 is not None:
            _sum = curr1.data + curr2.data + carry
            digit = _sum % 10
            carry = _sum // 10
            result.push(digit)
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1 is not None:
            _sum = curr1.data + carry
            digit = _sum % 10
            carry = _sum // 10
            result.push(digit)
            curr1 = curr1.next
        while curr2 is not None:
            _sum = curr2.data + carry
            digit = _sum % 10
            carry = _sum // 10
            result.push(digit)
            curr2 = curr2.next
        while carry != 0:
            digit = carry % 10
            carry = carry // 10
            result.push(digit)
        result.reverse()
        return result


# Example 1
l1 = LinkedList()
l1.build(4, 5)
l2 = LinkedList()
l2.build(3, 4, 5)
l3 = Solution.add(l1, l2)
print(l3)

# Example 2
l1 = LinkedList()
l1.build(0, 0, 6, 3)
l2 = LinkedList()
l2.build(0, 7)
l3 = Solution.add(l1, l2)
print(l3)