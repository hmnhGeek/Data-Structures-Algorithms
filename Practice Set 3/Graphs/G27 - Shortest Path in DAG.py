# Problem link - https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
# Solution - https://www.youtube.com/watch?v=ZUFQfFaU-8U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=27


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


class TopologicalSort:
    @staticmethod
    def _get_indegrees(graph):
        indegrees = {i: 0 for i in graph}
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                indegrees[adj_node] += 1
        return indegrees

    @staticmethod
    def get_topo_sort(graph):
        indegrees = TopologicalSort._get_indegrees(graph)
        queue = Queue()
        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)
        toposort = []
        while not queue.is_empty():
            node = queue.pop()
            toposort.append(node)
            for adj in graph[node]:
                adj_node, wt = adj
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        return toposort


class Solution:
    @staticmethod
    def get_shortest_paths(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # This will take O(V + E) time and O(V) space
        toposort = TopologicalSort.get_topo_sort(graph)

        # O(V) space.
        distances = {i: 1e6 for i in graph}
        distances[toposort[0]] = 0

        # loop on the toposort in O(V) time.
        for i in range(len(toposort)):
            node = toposort[i]
            # update the distances.
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > wt + distances[node]:
                    distances[adj_node] = wt + distances[node]
        return distances.values()


print(
    Solution.get_shortest_paths(
        {
            0: [[1, 2]],
            1: [[3, 1]],
            2: [[3, 3]],
            3: [],
            4: [[0, 3], [2, 1]],
            5: [[4, 1]],
            6: [[4, 2], [5, 3]]
        }
    )
)

print(
    Solution.get_shortest_paths(
        {
            0: [[1, 2], [2, 1]],
            1: [],
            2: []
        }
    )
)

print(
    Solution.get_shortest_paths(
        {
            0: [[2, 4]],
            1: [[0, 3], [2, 2], [3, 5]],
            2: [[4, 2], [3, -3]],
            3: [],
            4: [[3, 2]]
        }
    )
)
