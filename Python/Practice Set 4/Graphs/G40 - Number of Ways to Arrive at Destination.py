# Problem link - https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=%2Fnumber-of-ways-to-arrive-at-destination
# Solution - https://www.youtube.com/watch?v=_-0mx0SmYxA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=40


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
            return
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        parents = {i: set() for i in graph}
        queue = Queue()
        queue.push((0, source))
        while not queue.is_empty():
            d, node = queue.pop()
            if node == destination:
                continue
            for adj_node, wt in graph[node]:
                if d + wt < distances[adj_node]:
                    distances[adj_node] = d + wt
                    parents[adj_node].clear()
                    parents[adj_node].add(node)
                    queue.push((d + wt, adj_node))
                elif d + wt == distances[adj_node]:
                    parents[adj_node].add(node)
                    queue.push((d + wt, adj_node))
        path, paths = [], []
        Solution._get_paths(parents, destination, path, paths)
        return paths

    @staticmethod
    def _get_paths(parents, node, path, paths):
        if len(parents[node]) == 0:
            path.append(node)
            path = path[-1:-len(path)-1:-1]
            paths.append(path)
            return
        for parent in parents[node]:
            Solution._get_paths(parents, parent, path + [node, ], paths)


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
