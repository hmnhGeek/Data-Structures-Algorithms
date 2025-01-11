class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def put_front(self, k, v):
        node = Node(k, v)
        if self.is_empty():
            self.head.next = self.tail.prev = node
            node.prev = self.head
            node.next = self.tail
        else:
            temp = self.head.next
            self.head.next = node
            node.prev = self.head
            temp.prev = node
            node.next = temp
        self.length += 1

    def pop_back(self):
        if self.is_empty():
            return
        lru = self.tail.prev
        if self.length == 1:
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            next_lru = lru.prev
            next_lru.next = self.tail
            self.tail.prev = next_lru
        del lru
        self.length -= 1

    def move_to_front(self, node):
        if self.length == 1:
            return
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        if self.is_empty():
            self.head.next = self.tail.prev = node
            node.prev = self.head
            node.next = self.tail
        else:
            temp = self.head.next
            self.head.next = node
            node.prev = self.head
            temp.prev = node
            node.next = temp

    def show(self):
        curr = self.head
        while curr is not None:
            print(f"({curr.key}: {curr.value})", end=" ")
            curr = curr.next
        print()


