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


class Graph:
    @staticmethod
    def _get_indegrees(graph, indegrees):
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1

    @staticmethod
    def get_topological_sort(graph):
        """
            Time complexity will be O(V + E) and space complexity is O(V).
        """

        # get the indegrees of the nodes from the graph in O(V + E) time.
        indegrees = {i: 0 for i in graph}
        Graph._get_indegrees(graph, indegrees)

        # initialize an empty queue to perform BFS.
        queue = Queue()

        # traverse on the nodes from the graph. Basically, we want to push the 0-degree
        # nodes into the stack for initiating the algorithm.
        for node in indegrees:
            # if the indegree of the node is 0, push it into the queue.
            if indegrees[node] == 0:
                queue.push(node)

        # Typical BFS while loop...
        while not queue.is_empty():
            # pop the current node and print it.
            node = queue.pop()
            print(node, end=" ")

            # traverse on the adjacent nodes.
            for adj_node in graph[node]:
                # reduce the indegree of the adjacent node. Here we are trying the remove the edge between the node
                # `node` and node `adj_node`.
                indegrees[adj_node] -= 1

                # if there are no indegrees to the adjacent node, push it into the queue.
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        print()


Graph.get_topological_sort(
    {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2]
    }
)

Graph.get_topological_sort(
    {
        0: [],
        1: [0],
        2: [0],
        3: [0]
    }
)

Graph.get_topological_sort(
    {
        0: [],
        1: [3],
        2: [3],
        3: [],
        4: [0, 1],
        5: [0, 2]
    }
)