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
        if self.heap[rci][0] < self.heap[min_child_index][0]:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[min_child_index], self.heap[pi] = self.heap[pi], self.heap[min_child_index]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[min_child_index], self.heap[pi] = self.heap[pi], self.heap[min_child_index]
            self.min_heapify_down(min_child_index)

    def insert(self, x):
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
    def get_shortest_path(graph, source):
        if source not in graph:
            return
        pq = MinHeap()
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        pq.insert((distances[source], source))
        while not pq.is_empty():
            distance, node = pq.pop()
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > distance + wt:
                    distances[adj_node] = distance + wt
                    pq.insert((distances[adj_node], adj_node))
        return list(distances.values())


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
