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


class Solution:
    @staticmethod
    def get_min(start, arr, end):
        queue = Queue()
        distances = {i: 1e6 for i in range(10**5)}
        distances[start] = 0
        queue.push((distances[start], start))
        while not queue.is_empty():
            distance, node = queue.pop()
            if node == end:
                return distance
            for item in arr:
                adj_node = node * item
                adj_node = adj_node % 10**5
                if distances[adj_node] > distance + 1:
                    distances[adj_node] = distance + 1
                    queue.push((distance + 1, adj_node))
        return -1


print(Solution.get_min(3, [2, 5, 7], 30))
print(Solution.get_min(7, [3, 4, 65], 66175))
