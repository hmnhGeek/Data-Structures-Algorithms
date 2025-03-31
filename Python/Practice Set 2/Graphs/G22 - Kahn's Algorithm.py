# Problem link - https://www.geeksforgeeks.org/problems/topological-sort/1
# Solution - https://www.youtube.com/watch?v=73sneFXuTEg&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=22


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
    def _get_indegrees(graph, indegrees):
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1

    @staticmethod
    def topo_sort(graph):
        """
            Overall time complexity is O(V + E) and space complexity is O(V).
        """

        # queue for BFS
        queue = Queue()

        # get the indegrees of the nodes in O(V + E) time and O(V) space.
        indegrees = {i: 0 for i in graph}
        Solution._get_indegrees(graph, indegrees)

        # push all the nodes to the queue which have no indegree.
        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)

        # while the queue is not empty...
        while not queue.is_empty():
            # pop the node and print it.
            node = queue.pop()
            print(node, end=" ")

            # iterate on the adjacent nodes
            for adj_node in graph[node]:
                # decrement the indegree of this adjacent node
                indegrees[adj_node] -= 1
                # if the adj node is totally disconnected, push it to the queue.
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        print()


Solution.topo_sort(
    {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2]
    }
)

Solution.topo_sort(
    {
        0: [],
        1: [0],
        2: [0],
        3: [0]
    }
)

Solution.topo_sort(
    {
        0: [],
        1: [3],
        2: [3],
        3: [],
        4: [0, 1],
        5: [0, 2]
    }
)
