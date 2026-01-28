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


