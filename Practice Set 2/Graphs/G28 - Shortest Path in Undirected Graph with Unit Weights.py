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
    def get_shortest_path(graph, source):
        if source not in graph:
            return
        queue = Queue()
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        queue.push((source, 0))
        while not queue.is_empty():
            node, distance = queue.pop()
            for adj_node in graph[node]:
                if distances[adj_node] > distance + 1:
                    distances[adj_node] = distance + 1
                    queue.push((adj_node, distances[adj_node]))
        return distances.values()


print(
    Solution.get_shortest_path(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1, 6],
            3: [0, 4],
            4: [3, 5],
            5: [4, 6],
            6: [2, 5, 7, 8],
            7: [6, 8],
            8: [6, 7]
        },
        0
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [3],
            1: [3],
            2: [],
            3: [0, 1]
        },
        3
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1],
            3: [0, 4, 7],
            4: [3, 5, 6, 7],
            5: [4, 6],
            6: [4, 5, 7],
            7: [3, 4, 6]
        },
        0
    )
)