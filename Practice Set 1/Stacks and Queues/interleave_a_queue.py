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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class Solution:
    @staticmethod
    def _get_mid_node(queue: Queue) -> Node:
        counter = 0
        curr = queue.head
        while counter != queue.length // 2:
            curr = curr.next
            counter += 1
        return curr

    @staticmethod
    def interleave(queue: Queue):
        if queue.length % 2 == 1:
            return queue

        temp_queue = Queue()
        i, j = queue.head, Solution._get_mid_node(queue)
        temp = j
        while i != temp.next:
            while not temp_queue.is_empty():
                queue.push(temp_queue.pop())
            temp_queue.push(i.data)
            temp_queue.push(j.data)
            i = i.next
            j = j.next
            queue.pop()
        while i.next != j:
            queue.pop()
            i = i.next


# Example 1
q = Queue()
for i in [1, 2, 3, 4]:
    q.push(i)
q.show()
Solution.interleave(q)
q.show()

# Example 2
q = Queue()
for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    q.push(i)
q.show()
Solution.interleave(q)
q.show()