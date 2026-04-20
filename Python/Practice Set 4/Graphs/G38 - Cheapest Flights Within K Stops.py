# Problem link - https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1
# Solution - https://www.youtube.com/watch?v=9XybHVqTHcQ&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=38


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
    def get_cheapest_flight(graph, source, destination, k):
        """
            We should use a normal queue in this problem because the stops will increment by 1 everytime. So there is
            no need for a min heap. It will only add a log(V) factor to the complexity.

            Time complexity with O(E) in case of queue and O(E * log(V)) in min heap approach.
            Space complexity will be O(V) in both the cases.
        """
        n = len(graph)
        if source not in range(n) or destination not in range(n):
            return
        distances = [1e6 for _ in range(n)]
        distances[source] = 0
        queue = Queue()
        queue.push((source, 0, 0))
        while not queue.is_empty():
            node, stops_taken, distance = queue.pop()
            if node == destination:
                continue
            if stops_taken > k:
                continue
            for adj in graph[node]:
                adj_node, wt = adj
                if wt + distance < distances[adj_node]:
                    if adj_node == destination:
                        queue.push((adj_node, stops_taken, wt + distance))
                    else:
                        queue.push((adj_node, stops_taken + 1, wt + distance))
                    distances[adj_node] = wt + distance
        return distances[destination]


print(
    Solution.get_cheapest_flight(
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
    Solution.get_cheapest_flight(
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

print(
    Solution.get_cheapest_flight(
        {
            0: [[1, 100], [2, 500]],
            1: [[2, 100]],
            2: []
        },
        0,
        2,
        0
    )
)
