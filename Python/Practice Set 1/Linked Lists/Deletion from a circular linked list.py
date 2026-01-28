# Problem link - https://www.geeksforgeeks.org/dsa/deletion-circular-linked-list/


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

    def _delete_head(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = self.tail = None
        else:
            next_head = self.head.next
            node = self.head
            del node
            self.head = next_head
            self.tail.next = next_head
        self.length -= 1

    def _delete_tail(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = self.tail = None
        else:
            prev = self.tail
            while prev.next != self.tail:
                prev = prev.next
            node = self.tail
            prev.next = self.head
            self.tail = prev
            del node
        self.length -= 1

    def delete(self, index):
        if index == 0:
            self._delete_head()
            return
        if index == self.length - 1:
            self._delete_tail()
            return
        if index >= self.length or index < 0:
            return
        prev, curr = self.tail, self.head
        curr_index = 0
        while curr_index != index:
            curr = curr.next
            prev = prev.next
            curr_index += 1
        prev.next = curr.next
        self.length -= 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def __str__(self):
        if self.length == 0:
            return "[]"
        if self.length == 1:
            return f"[{self.head.data}] (next = {self.head.data})"
        curr = self.head
        result = "["
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{self.tail.data}] (next = {self.tail.next.data})"
        return result


# Example 1
l1 = CircularLinkedList()
l1.build(1, 2, 2, 3)
print(l1)
l1.delete(2)
print(l1)

# Example 2
l2 = CircularLinkedList()
l2.build(1, 2, 3, 4)
print(l2)
l2.delete(0)
print(l2)