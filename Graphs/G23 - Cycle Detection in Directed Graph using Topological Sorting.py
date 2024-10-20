# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
# Solution - https://www.youtube.com/watch?v=iTBaI90lpDQ&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=23


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
    def detect_cycle(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # we will be using Kahn's Algorithm to detect a cycle. We know that topological sort is possible only in DAGs.
        # If the topological sort is not possible, then there is a cycle, because the graph given is already directed
        # as per the question.

        # get the indegrees of the nodes.
        indegrees = {i: 0 for i in graph}
        Graph._get_indegrees(graph, indegrees)

        # initiate a queue.
        queue = Queue()

        # push the initial nodes with indegree of 0.
        for node in graph:
            if indegrees[node] == 0:
                queue.push(node)

        # initialize a count variable to store the number of nodes that made it to topological order.
        count = 0

        # typical BFS.
        while not queue.is_empty():
            # pop the current node and increment the count.
            node = queue.pop()
            count += 1

            # loop on the adjacent nodes.
            for adj_node in graph[node]:
                # remove the edge between node and adjacent node.
                indegrees[adj_node] -= 1

                # if the indegree becomes 0, then push the adjacent node to queue.
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)

        # if the queue gets empty before topological sort is completed, then there is a cycle.
        return count != len(graph)


print(
    Graph.detect_cycle(
        {
            0: [1],
            1: [2],
            2: [3],
            3: [3]
        }
    )
)

print(
    Graph.detect_cycle(
        {
            0: [1],
            1: [2],
            2: []
        }
    )
)

print(
    Graph.detect_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
    )
)

print(
    Graph.detect_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [3],
            3: []
        }
    )
)