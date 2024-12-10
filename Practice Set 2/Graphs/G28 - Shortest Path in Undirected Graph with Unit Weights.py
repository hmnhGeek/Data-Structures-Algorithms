# Problem link - https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
# Solution - https://www.youtube.com/watch?v=C4gxoTaI71U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=28


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
    def get_shortest_path(graph, source):
        """
            Overall time complexity is O(V + E) and space complexity is O(V).
        """

        # if source node is not in graph, return
        if source not in graph:
            return

        # define a queue and push the source node with distance 0 into it.
        queue = Queue()
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        queue.push((source, 0))

        # while the BFS is possible.
        while not queue.is_empty():
            # pop the current node.
            node, distance = queue.pop()

            # loop into the adjacent nodes
            for adj_node in graph[node]:
                # update the distance of adjacent node if possible and then push it to the queue.
                if distances[adj_node] > distance + 1:
                    distances[adj_node] = distance + 1
                    queue.push((adj_node, distances[adj_node]))

        # return the shortest paths from the source node.
        return distances.values()


print(
    Solution.get_shortest_path(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1, 6],
            3: [0, 4],
            4: [3, 5],
            5: [4, 6],
            6: [2, 5, 7, 8],
            7: [6, 8],
            8: [6, 7]
        },
        0
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [3],
            1: [3],
            2: [],
            3: [0, 1]
        },
        3
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1],
            3: [0, 4, 7],
            4: [3, 5, 6, 7],
            5: [4, 6],
            6: [4, 5, 7],
            7: [3, 4, 6]
        },
        0
    )
)