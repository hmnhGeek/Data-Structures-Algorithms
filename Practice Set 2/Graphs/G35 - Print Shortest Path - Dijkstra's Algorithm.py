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
        if self.heap[min_child_index][0] > self.heap[rci][0]:
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
    def get_shortest_path(graph, source, destination):
        if source not in graph or destination not in graph:
            return
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        parents = {i: None for i in graph}
        parents[source] = source
        pq = MinHeap()
        pq.insert((0, source))
        while not pq.is_empty():
            distance, node = pq.pop()
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > distance + wt:
                    distances[adj_node] = distance + wt
                    parents[adj_node] = node
                    pq.insert((distances[adj_node], adj_node))
        path_list = []
        start_node = destination
        while parents[start_node] != start_node:
            path_list.append(start_node)
            start_node = parents[start_node]
        path_list.append(start_node)
        return path_list[-1:-len(path_list)-1:-1]


print(
    Solution.get_shortest_path(
        {
            1: [[2, 2], [4, 1]],
            2: [[1, 2], [3, 4], [5, 5]],
            3: [[2, 4], [4, 3], [5, 1]],
            4: [[1, 1], [3, 3]],
            5: [[2, 5], [3, 1]]
        },
        1,
        5
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 1], [2, 1]],
            1: [[0, 1], [4, 1]],
            2: [[0, 1], [3, 1]],
            3: [[2, 1], [5, 1]],
            4: [[1, 1], [5, 1]],
            5: [[3, 1], [4, 1]]
        },
        0,
        4
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 1], [2, 1]],
            1: [[0, 1], [4, 1], [3, 1]],
            2: [[0, 1], [3, 1]],
            3: [[2, 1], [5, 1], [1, 1]],
            4: [[1, 1], [5, 1]],
            5: [[3, 1], [4, 1]]
        },
        0,
        5
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 4], [7, 8]],
            1: [[0, 4], [2, 8], [7, 11]],
            2: [[1, 8], [8, 2], [5, 4], [3, 7]],
            3: [[2, 7], [5, 14], [4, 9]],
            4: [[3, 9], [5, 10]],
            5: [[6, 2], [2, 4], [3, 14], [4, 10]],
            6: [[7, 1], [8, 6], [5, 2]],
            7: [[0, 8], [1, 11], [8, 7], [6, 1]],
            8: [[2, 2], [7, 7], [6, 6]]
        },
        0,
        4
    )
)

print(
    Solution.get_shortest_path(
        {
            0: [[1, 4], [7, 8]],
            1: [[0, 4], [2, 8], [7, 11]],
            2: [[1, 8], [8, 2], [5, 4], [3, 7]],
            3: [[2, 7], [5, 14], [4, 9]],
            4: [[3, 9], [5, 10]],
            5: [[6, 2], [2, 4], [3, 14], [4, 10]],
            6: [[7, 1], [8, 6], [5, 2]],
            7: [[0, 8], [1, 11], [8, 7], [6, 1]],
            8: [[2, 2], [7, 7], [6, 6]]
        },
        0,
        8
    )
)