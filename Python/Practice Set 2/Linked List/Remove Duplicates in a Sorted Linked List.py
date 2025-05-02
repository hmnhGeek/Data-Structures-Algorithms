# Problem link - https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1


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
        result = f"[{self.head.data}, "
        curr = self.head.next
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}]"
        return result

    def remove_duplicates(self):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # if there is none, or only 1 element in the list, do nothing.
        if self.length == 0 or self.length == 1:
            return

        # point curr and temp.
        curr = self.head
        temp = self.head.next

        # traverse the linked list
        while curr is not None:
            # while temp's data matches with curr's data, skip temp and move to next.
            # also reduce the length of the linked list, as you've removed one element.
            while temp and temp.data == curr.data:
                temp = temp.next
                self.length -= 1

            # point curr's next to temp (non-matching)
            curr.next = temp

            # if temp has become None, then curr should be the tail.
            if temp is None:
                self.tail = curr

            # update curr
            curr = temp

            # get to the next temp value.
            if temp is not None:
                temp = temp.next


l1 = LinkedList()
l1.build(2, 2, 4, 5)
print(l1)
l1.remove_duplicates()
print(l1)

l2 = LinkedList()
l2.build(2, 2, 2, 2)
print(l2)
l2.remove_duplicates()
print(l2)

l3 = LinkedList()
l3.build(0, 0, 0, 0, 1, 1, 2, 3, 6, 7)
print(l3)
l3.remove_duplicates()
print(l3)