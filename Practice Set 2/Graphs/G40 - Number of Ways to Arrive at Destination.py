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


class PathsFinder:
    @staticmethod
    def get_num_paths(start_node, parents):
        if start_node not in parents:
            return 0
        if parents[start_node] == [None]:
            return 1
        paths = 0
        for i in parents[start_node]:
            paths += PathsFinder.get_num_paths(i, parents)
        return paths

    @staticmethod
    def get_num_paths_memoized(start_node, parents, dp):
        if start_node not in parents:
            return 0
        if parents[start_node] == [None]:
            return 1
        if dp[start_node] is not None:
            return dp[start_node]
        paths = 0
        for i in parents[start_node]:
            paths += PathsFinder.get_num_paths(i, parents)
        dp[start_node] = paths
        return dp[start_node]


class Solution:
    @staticmethod
    def _get_graph(edges):
        graph = {}
        for edge in edges:
            src, dst, wt = edge
            if src not in graph:
                graph[src] = [[dst, wt]]
            else:
                graph[src].append([dst, wt])
            if dst not in graph:
                graph[dst] = [[src, wt]]
            else:
                graph[dst].append([src, wt])
        return graph

    @staticmethod
    def _get_all_paths(parents):
        pass

    @staticmethod
    def num_ways(edges, source, destination):
        graph = Solution._get_graph(edges)
        queue = Queue()
        distances = {i: 1e6 for i in graph}
        parents = {i: [] for i in graph}
        distances[source] = 0
        parents[source] = [None]
        queue.push((source, distances[source]))
        while not queue.is_empty():
            node, distance = queue.pop()
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > distance + wt:
                    distances[adj_node] = distance + wt
                    parents[adj_node] = [node, ]
                    queue.push((adj_node, distances[adj_node]))
                if distances[adj_node] == distance + wt:
                    if node not in parents[adj_node]:
                        parents[adj_node].append(node)
        return PathsFinder.get_num_paths_memoized(destination, parents, {i: None for i in graph})


print(
    Solution.num_ways(
        [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]],
        0, 6
    )
)
