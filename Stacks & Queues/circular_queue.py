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
        rear = (self.front + self.size) % self.capacity
        self.queue[rear] = x
        self.size += 1
        print(self.queue)

    def pop(self):
        if self.size == 0:
            print("Queue is empty.")
            return
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.size -= 1
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
