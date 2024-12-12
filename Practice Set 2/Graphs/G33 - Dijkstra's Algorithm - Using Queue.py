# Problem link - https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
# Solution - https://www.youtube.com/watch?v=V6H1qAeB-l4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=32


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
            Time complexity is O(E * log(V)) and space complexity is O(V).
        """

        # if source node is not in graph, return
        if source not in graph:
            return

        # define distances and mark source node distance as 0.
        distances = {i: 1e6 for i in graph}
        distances[source] = 0

        # define a queue and push source node.
        queue = Queue()
        queue.push((source, 0))

        # typical BFS
        while not queue.is_empty():
            # pop the current node and distance
            node, distance = queue.pop()

            # loop on the adjacent nodes
            for adj in graph[node]:
                adj_node, wt = adj
                # update the adjacent node's distance and push it to the queue if needed
                if distances[adj_node] > distance + wt:
                    distances[adj_node] = distance + wt
                    queue.push((adj_node, distances[adj_node]))

        # return the shortest distances.
        return distances.values()


print(
    Solution.get_shortest_path(
        {
            0: [[1, 4], [2, 4]],
            1: [[0, 4], [2, 2]],
            2: [[0, 4], [1, 2], [3, 3], [5, 6], [4, 1]],
            3: [[2, 3], [5, 2]],
            4: [[2, 1], [5, 3]],
            5: [[3, 2], [2, 6], [4, 3]]
        },
        0
    )
)


print(
    Solution.get_shortest_path(
        {
            0: [[1, 9]],
            1: [[0, 9]]
        },
        0
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 1], [2, 6]],
            1: [[0, 1], [2, 3]],
            2: [[0, 6], [1, 3]]
        },
        2
    )
)