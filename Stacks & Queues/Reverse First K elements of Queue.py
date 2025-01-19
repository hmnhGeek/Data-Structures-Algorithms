class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
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

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        if self.is_empty():
            return
        return self.head.data

    def _reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def _get_kth_node(self, k):
        curr, counter = self.head, 1
        while counter != k:
            curr = curr.next
            counter += 1
        return curr

    def reverse(self, k):
        if k <= 0:
            return
        kth_node = None
        if k >= self.length:
            kth_node = self.tail
        else:
            kth_node = self._get_kth_node(k)

        temp = kth_node.next
        kth_node.next = None
        temp_queue = Queue()
        temp_queue.head = self.head
        temp_queue.tail = kth_node
        temp_queue._reverse()
        self.head = temp_queue.head
        temp_queue.tail.next = temp


def test(*args):
    k = args[-1]
    q = Queue()
    for i in range(len(args) - 1):
        q.push(args[i])
    q.show()
    q.reverse(k)
    q.show()


test(1, 2, 3, 4, 5, 3)
test(4, 3, 2, 1, 4)
