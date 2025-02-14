class Node:
    def __init__(self, d, n, s):
        self.d = d
        self.n = n
        self.s = s


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci].s < self.heap[min_child_index].s:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].s > self.heap[min_child_index].s:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].s > self.heap[min_child_index].s:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x: Node):
        self.heap.append(x)
        self.min_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.min_heapify_down(0)
        return item


class Solution:
    @staticmethod
    def get_cheapest_flight(graph, source, destination, k):
        if source not in graph or destination not in graph:
            return
        pq = MinHeap()
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        pq.insert(Node(0, source, 0))
        while not pq.is_empty():
            x = pq.pop()
            distance, node, stops_till_now = x.d, x.n, x.s
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > distance + wt and stops_till_now + 1 <= k + 1:
                    distances[adj_node] = distance + wt
                    pq.insert(Node(distances[adj_node], adj_node, stops_till_now + 1))
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
