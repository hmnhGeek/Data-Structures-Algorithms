# Problem link - https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1
# Solution - https://www.youtube.com/watch?v=9XybHVqTHcQ&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=38


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
    def get_cheapest_flight_cost(graph, source, destination, num_stops_bearable):
        if source not in graph or destination not in graph:
            return
        pq = MinHeap()
        distances = {i: 1e6 for i in graph}
        distances[source] = 0

        # insert with +1 stops because we will count the destination as one of the stops.
        pq.insert((distances[source], source, num_stops_bearable + 1))

        while not pq.is_empty():
            distance, node, k = pq.pop()
            if node == destination:
                return distance

            # if for the popped node, no more stops are available and it's not even the destination node,
            # then do nothing and continue to the next element in the PQ.
            if k == 0:
                continue

            for adj in graph[node]:
                adj_node, edge_wt = adj
                if distances[adj_node] > distance + edge_wt:
                    distances[adj_node] = distance + edge_wt
                    # we have consumed one stop now, hence, k - 1.
                    pq.insert((distances[adj_node], adj_node, k - 1))
        return distances[destination]


print(
    Graph.get_cheapest_flight_cost(
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
    Graph.get_cheapest_flight_cost(
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

print(
    Graph.get_cheapest_flight_cost(
        {
            0: [[1, 5], [3, 5]],
            1: [[2, 2], [4, 1]],
            2: [],
            3: [[1, 2]],
            4: [[2, 1]]
        },
        0,
        2,
        2
    )
)