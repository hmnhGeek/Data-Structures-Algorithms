# Problem link - https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
# Solution - https://www.youtube.com/watch?v=ZUFQfFaU-8U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=27


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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
            node.next = self.head
            self.head = node
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

    def top(self):
        if self.is_empty():
            return
        return self.head.data


class Solution:
    @staticmethod
    def _dfs(graph, node, visited, stack):
        visited[node] = True
        for adj in graph[node]:
            adj_node, _ = adj
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited, stack)
        stack.push(node)
    
    @staticmethod
    def get_shortest_paths(graph, source):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # get the topo sort of the graph in the stack
        stack = Stack()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, visited, stack)

        # mark the distance of the source node as 0.
        distances = {i: 1e6 for i in graph}
        distances[source] = 0

        # until the stack gets empty, relax the edges and update the minimum distances.
        while not stack.is_empty():
            node = stack.pop()
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > distances[node] + wt:
                    distances[adj_node] = distances[node] + wt

        # return the shortest paths
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
        },
        6
    )
)

print(
    Solution.get_shortest_paths(
        {
            0: [[1, 2], [2, 1]],
            1: [],
            2: []
        },
        0
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
        },
        0
    )
)
