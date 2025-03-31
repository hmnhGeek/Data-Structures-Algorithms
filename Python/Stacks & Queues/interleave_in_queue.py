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

    def enqueue(self, x):
        node = Node(x)

        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        return None if self.is_empty() else self.head.data

    def show(self):
        curr = self.head

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


def interleave(queue: Queue):
    '''
        Overall time complexity is O(n).
        Overall space complexity is O(n).
    '''

    n = queue.length

    # ensure that queue has an even length
    if n % 2 != 0:
        return

    # create a temporary queue which will hold n/2 elements,
    # by pushing the first half of the queue to temp queue.
    # This process will take O(n/2) time and space each.
    temp = Queue()
    for _ in range(n//2):
        temp.enqueue(queue.dequeue())

    # while the temp queue is not emptied, do the following:
    # first, remove from temp and add it to queue.
    # second, remove from front of queue and push to its back.
    # This whole process will again take O(n/2) time because
    # enqueue and dequeue takes O(1) time.
    while not temp.is_empty():
        # enqueue an element from the temp queue (by removing from temp).
        queue.enqueue(temp.dequeue())

        # push the front element of the queue to its back.
        queue.enqueue(queue.dequeue())


def example1():
    q = Queue()
    for i in [1,2,3,4,5,6,7,8]:
        q.enqueue(i)

    print("Queue before:\n")
    q.show()

    interleave(q)
    print("\n\nQueue afterwards:\n")
    q.show()


def example2():
    q = Queue()

    for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        q.enqueue(i)

    print("Queue before:\n")
    q.show()

    interleave(q)
    print("\n\nQueue afterwards:\n")
    q.show()

print("Example 1")
example1()
print()
print()
print("Example 2")
example2()
