# Problem link - https://www.geeksforgeeks.org/introduction-to-circular-queue/

"""
    All operations are O(1) time and O(1) space.
"""


class CircularQueue:
    def __init__(self, n):
        self.queue = [None] * n
        self.capacity = n
        self.front = 0
        self.size = 0

    def push(self, x):
        if self.size == self.capacity:
            print("Queue is full.")
            return

        # wherever is the front pointer, add the current size and take modulo from capacity to get the rear index.
        rear = (self.front + self.size) % self.capacity
        # set the element at rear index to x and increment the size.
        self.queue[rear] = x
        self.size += 1
        # print the queue
        print(self.queue)

    def pop(self):
        if self.size == 0:
            print("Queue is empty.")
            return

        # get the item at the front
        item = self.queue[self.front]
        # set the item at front index to None and decrement the size.
        self.queue[self.front] = None
        self.size -= 1
        # and increment the front pointer (but take modulo)
        self.front = (self.front + 1) % self.capacity
        print(self.queue)
        return item


# Example
queue = CircularQueue(4)
queue.push(4)
queue.push(22)
queue.push(13)
queue.pop()
queue.push(15)
queue.push(4)
queue.push(10)
queue.pop()
queue.pop()
queue.pop()
queue.pop()
queue.pop()
