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
    def get_shortest_path(graph, source, destination):
        if source not in graph or destination not in graph:
            return
        distances = {i: 1e6 for i in graph}
        parents = {i: None for i in graph}
        distances[source] = 0
        parents[source] = source
        queue = Queue()
        queue.push((source, distances[source]))
        while not queue.is_empty():
            node, distance = queue.pop()
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > wt + distance:
                    distances[adj_node] = wt + distance
                    parents[adj_node] = node
                    queue.push((adj_node, distances[adj_node]))
        path = [destination,]
        start_node = destination
        while parents[start_node] != start_node:
            start_node = parents[start_node]
            path.append(start_node)
        return path[-1:-len(path)-1:-1]


print(
    Solution.get_shortest_path(
        {
            1: [[2, 2], [4, 1]],
            2: [[1, 2], [3, 4], [5, 5]],
            3: [[2, 4], [4, 3], [5, 1]],
            4: [[1, 1], [3, 3]],
            5: [[2, 5], [3, 1]]
        },
        1,
        5
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 1], [2, 1]],
            1: [[0, 1], [4, 1]],
            2: [[0, 1], [3, 1]],
            3: [[2, 1], [5, 1]],
            4: [[1, 1], [5, 1]],
            5: [[3, 1], [4, 1]]
        },
        0,
        4
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 1], [2, 1]],
            1: [[0, 1], [4, 1], [3, 1]],
            2: [[0, 1], [3, 1]],
            3: [[2, 1], [5, 1], [1, 1]],
            4: [[1, 1], [5, 1]],
            5: [[3, 1], [4, 1]]
        },
        0,
        5
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 4], [7, 8]],
            1: [[0, 4], [2, 8], [7, 11]],
            2: [[1, 8], [8, 2], [5, 4], [3, 7]],
            3: [[2, 7], [5, 14], [4, 9]],
            4: [[3, 9], [5, 10]],
            5: [[6, 2], [2, 4], [3, 14], [4, 10]],
            6: [[7, 1], [8, 6], [5, 2]],
            7: [[0, 8], [1, 11], [8, 7], [6, 1]],
            8: [[2, 2], [7, 7], [6, 6]]
        },
        0,
        4
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 4], [7, 8]],
            1: [[0, 4], [2, 8], [7, 11]],
            2: [[1, 8], [8, 2], [5, 4], [3, 7]],
            3: [[2, 7], [5, 14], [4, 9]],
            4: [[3, 9], [5, 10]],
            5: [[6, 2], [2, 4], [3, 14], [4, 10]],
            6: [[7, 1], [8, 6], [5, 2]],
            7: [[0, 8], [1, 11], [8, 7], [6, 1]],
            8: [[2, 2], [7, 7], [6, 6]]
        },
        0,
        8
    )
)