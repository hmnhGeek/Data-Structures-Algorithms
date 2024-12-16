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
    def cheapest_flights(graph, source, destination, k):
        """
            Time complexity is O(E*log(V)) and space complexity is O(V).
        """

        # edge case check
        if source not in graph or destination not in graph:
            return

        # push the source node with `k + 1` stops being available; extra 1 for destination.
        queue = Queue()
        queue.push((source, 0, k + 1))

        # mark the source node distance as 0
        distances = {i: 1e6 for i in graph}
        distances[source] = 0

        # typical Dijkstra
        while not queue.is_empty():
            # get the node from queue
            node, distance, stops = queue.pop()
            # if there are no stops post this, simply continue to next item in queue.
            if stops == 0:
                continue
            # loop on the adjacent nodes of this node.
            for adj in graph[node]:
                adj_node, wt = adj
                # since stops are available, update the variables if required with one less stop.
                if distances[adj_node] > distance + wt:
                    distances[adj_node] = distance + wt
                    queue.push((adj_node, distances[adj_node], stops - 1))
        # return the min distance with k stops for the destination.
        return distances[destination]


print(
    Solution.cheapest_flights(
        {
            0: [[1, 5], [3, 2]],
            1: [[2, 5], [4, 1]],
            2: [],
            3: [[1, 2]],
            4: [[2, 1]]
        },
        0,
        2,
        2
    )
)

print(
    Solution.cheapest_flights(
        {
            0: [[1, 100]],
            1: [[2, 100], [3, 600]],
            2: [[0, 100], [3, 200]],
            3: []
        },
        0,
        3,
        1
    )
)