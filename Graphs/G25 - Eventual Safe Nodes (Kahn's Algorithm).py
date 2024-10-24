# Problem link - https://www.geeksforgeeks.org/problems/eventual-safe-states/1
# Solution - https://www.youtube.com/watch?v=2gtg3VsDGyc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=26


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


class Graph:
    @staticmethod
    def _get_indegrees(graph, indegrees):
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1

    @staticmethod
    def _topological_sort(graph):
        """
            Overall time complexity is O(V + E) and space complexity is O(V).
        """

        # calculate indegrees of each node in O(V + E) time and O(V) space.
        indegrees = {i: 0 for i in graph}
        Graph._get_indegrees(graph, indegrees)

        # initialize queue for implementing Kahn's Algorithm
        queue = Queue()
        topo_sort = []

        # push all the starting nodes into the queue (nodes having 0 indegrees)
        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)

        # typical BFS...
        while not queue.is_empty():
            # pop the current node and push it to topo sort array.
            current_node = queue.pop()
            topo_sort.append(current_node)

            # iterate on the adjacent nodes of the current popped node.
            for adj_node in graph[current_node]:
                # reduce the indegree of the adjacent node.
                indegrees[adj_node] -= 1
                # if the indegree reaches 0, push it to the queue.
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)

        # finally return the topo sort array.
        return topo_sort

    @staticmethod
    def _get_reversed_graph(graph):
        reversed = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed[adj_node].append(node)
        return reversed

    @staticmethod
    def get_eventual_safe_nodes(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V + E).
        """
        # find the reverse graph representation in O(V + E) time and O(V + E) space.
        reversed_graph = Graph._get_reversed_graph(graph)
        # do a toposort on the reversed graph in O(V + E) time and O(V) space.
        topo_sort = Graph._topological_sort(reversed_graph)
        # return topo sort.
        return topo_sort


print(
    Graph.get_eventual_safe_nodes(
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
    Graph.get_eventual_safe_nodes(
        {
            0: [1],
            1: [2],
            2: [0, 3],
            3: []
        }
    )
)