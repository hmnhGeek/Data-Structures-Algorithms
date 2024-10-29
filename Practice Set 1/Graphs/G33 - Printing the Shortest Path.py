# Problem link - https://www.youtube.com/watch?v=rp1SMw7HSO8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=35
# Solution - https://www.youtube.com/watch?v=rp1SMw7HSO8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=35


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
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
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


class Graph:
    @staticmethod
    def print_shortest_path_from(source, destination, graph):
        if source not in graph or destination not in graph:
            return

        min_heap = MinHeap()
        distances = {i: 1e6 for i in graph}
        parents = {i: None for i in graph}
        distances[source] = 0
        min_heap.insert((distances[source], source))

        while not min_heap.is_empty():
            distance, node = min_heap.pop()
            for adj in graph[node]:
                adj_node, wt = adj
                if distances[adj_node] > distance + wt:
                    distances[adj_node] = distance + wt
                    parents[adj_node] = node
                    min_heap.insert((distances[adj_node], adj_node))

        trace_back = [destination,]
        parent = destination
        while parents[parent] is not None:
            trace_back.append(parents[parent])
            parent = parents[parent]
        return trace_back[-1:-len(trace_back)-1:-1]


print(
    Graph.print_shortest_path_from(
        1,
        5,
        {
            1: [[2, 2], [4, 1]],
            2: [[1, 2], [3, 4], [5, 5]],
            3: [[2, 4], [4, 3], [5, 1]],
            4: [[1, 1], [3, 3]],
            5: [[2, 5], [3, 1]]
        }
    )
)


print(
    Graph.print_shortest_path_from(
        1,
        4,
        {
            1: [[2, 2], [4, 1]],
            2: [[1, 2], [3, 4]],
            3: [[2, 4], [4, 3]],
            4: [[1, 1], [3, 3]]
        }
    )
)