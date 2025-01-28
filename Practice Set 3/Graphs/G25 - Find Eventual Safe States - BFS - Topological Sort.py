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
    def get_safe_nodes(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # get the reversed graph and the indegrees dictionary.
        reversed, indeg = Solution._get_reversed_graph(graph)
        queue = Queue()

        # store the safe nodes in this list
        safe_nodes = []

        # push the starting nodes.
        for node in indeg:
            if indeg[node] == 0:
                queue.push(node)

        # typical topological sort.
        while not queue.is_empty():
            node = queue.pop()
            safe_nodes.append(node)
            for adj_node in reversed[node]:
                indeg[adj_node] -= 1
                if indeg[adj_node] == 0:
                    queue.push(adj_node)
        return safe_nodes

    @staticmethod
    def _get_reversed_graph(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """
        reversed = {i: [] for i in graph}
        indeg = {i: 0 for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed[adj_node].append(node)
                indeg[node] += 1
        return reversed, indeg



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
