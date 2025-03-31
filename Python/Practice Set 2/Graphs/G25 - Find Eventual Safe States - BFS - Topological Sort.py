# Problem link - https://www.geeksforgeeks.org/problems/eventual-safe-states/1
# Solution - https://www.youtube.com/watch?v=2gtg3VsDGyc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=25


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
    def _get_reversed_graph(graph, reversed_graph):
        for node in graph:
            for adj_node in graph[node]:
                reversed_graph[adj_node].append(node)

    @staticmethod
    def _populate_indegrees(reversed_graph, indegrees):
        for node in reversed_graph:
            for adj_node in reversed_graph[node]:
                indegrees[adj_node] += 1

    @staticmethod
    def get_safe_nodes(graph):
        """
            Overall time complexity is O(V + E) and space complexity is O(V + E).
        """

        queue = Queue()

        # define a reversed graph and indegrees dictionary and populate them
        reversed_graph = {i: [] for i in graph}
        indegrees = {i: 0 for i in reversed_graph}
        Solution._get_reversed_graph(graph, reversed_graph)
        Solution._populate_indegrees(reversed_graph, indegrees)

        # define safe nodes set
        safe_nodes = set()

        # push all the terminal nodes from the original graph.
        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)

        # typical topo sort...
        while not queue.is_empty():
            # pop the safe node and add it to the result
            node = queue.pop()
            safe_nodes.add(node)

            # loop in the adjacent nodes and add them to queue if applicable.
            for adj_node in reversed_graph[node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)

        # return the safe nodes.
        return safe_nodes
    

print(
    Solution.get_safe_nodes(
        {
            0: [1, 2],
            1: [3],
            2: [5],
            3: [0],
            4: [5],
            5: [],
            6: [],
            7: [1]
        }
    )
)

print(
    Solution.get_safe_nodes(
        {
            0: [1],
            1: [2],
            2: [0, 3],
            3: []
        }
    )
)

print(
    Solution.get_safe_nodes(
        {
            0: [1],
            1: [3],
            2: [4],
            3: [0, 2],
            4: []
        }
    )
)
