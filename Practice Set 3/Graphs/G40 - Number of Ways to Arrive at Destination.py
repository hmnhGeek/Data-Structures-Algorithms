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
    def get_num_ways(graph, source, destination):
        if source not in graph or destination not in graph:
            return -1
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        parents = {i: [] for i in graph}
        parents[source] = [source, ]
        queue = Queue()
        queue.push((source, 0))

        while not queue.is_empty():
            node, distance = queue.pop()
            for adj in graph[node]:
                adj_node, wt = adj
                if distance + wt < distances[adj_node]:
                    distances[adj_node] = distance + wt
                    parents[adj_node] = [node, ]
                    queue.push((adj_node, distance + wt))
                elif distance + wt == distances[adj_node]:
                    if node not in parents[adj_node]:
                        parents[adj_node].append(node)
                    queue.push((adj_node, distance + wt))

        result = set()
        Solution._populate_paths(parents, destination, [destination, ], result)
        return result

    @staticmethod
    def _populate_paths(parents, destination, path, result):
        prev = parents[destination]
        if len(prev) == 1 and prev[0] == destination:
            return
        for p in prev:
            path.append(p)
            Solution._populate_paths(parents, p, path, result)
            if tuple(path) not in result:
                result.add(tuple(path[-1:-len(path)-1:-1]))
            path = [destination, ]


print(
    Solution.get_num_ways(
        {
            0: [[1, 2], [4, 5], [6, 7]],
            1: [[0, 2], [2, 3], [3, 3]],
            2: [[1, 3], [5, 1]],
            3: [[1, 3], [6, 3], [5, 1]],
            4: [[0, 5], [6, 2]],
            5: [[2, 1], [3, 1], [6, 1]],
            6: [[0, 7], [3, 3], [4, 2], [5, 1]]
        },
        0,
        6
    )
)

print(
    Solution.get_num_ways(
        {
            0: [[1, 1], [2, 2], [5, 8]],
            1: [[0, 1], [2, 3], [3, 3]],
            2: [[1, 3], [0, 2], [5, 6]],
            3: [[1, 3], [4, 2]],
            4: [[3, 2], [5, 2]],
            5: [[2, 6], [4, 2], [0, 8]]
        },
        0,
        5
    )
)

