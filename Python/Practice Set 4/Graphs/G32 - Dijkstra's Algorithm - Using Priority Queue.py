# Problem link - https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
# Solution - https://www.youtube.com/watch?v=V6H1qAeB-l4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=32


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        if 0 <= lci < len(self.heap):
            return lci
        return None

    def get_rci(self, pi):
        rci = 2*pi + 2
        if 0 <= rci < len(self.heap):
            return rci
        return None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
        if 0 <= pi < len(self.heap):
            return pi
        return None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci] < self.heap[min_child_index]:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
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


class HeapNode:
    def __init__(self, distance, node):
        self.distance = distance
        self.node = node

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance


class Solution:
    @staticmethod
    def get_shortest_path(graph, source_node):
        """
            Time complexity is O(E * log(V)) and space complexity is O(V).
        """
        if source_node not in graph:
            return
        distances = {node: 1e6 for node in graph}
        distances[source_node] = 0
        pq = MinHeap()
        pq.insert(HeapNode(distances[source_node], source_node))
        while not pq.is_empty():
            heap_node = pq.pop()
            distance, node = heap_node.distance, heap_node.node
            for adj_node, weight in graph[node]:
                if distances[adj_node] > distance + weight:
                    distances[adj_node] = distance + weight
                    pq.insert(HeapNode(distances[adj_node], adj_node))
        return distances


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
