class MinHeap:
    def __init__(self):
        self.heap = []

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return None
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
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
        if len(self.heap) == 0:
            return

        li = len(self.heap) - 1
        item = self.heap[0]
        self.heap[0], self.heap[li] = self.heap[li], self.heap[0]
        del self.heap[li]
        self.min_heapify_down(0)
        return item


# Dijkstra will not work for graphs having even one single negative weight or a negative weight cycle.
# For example, try performing Dijkstra on this graph: {0: {node = 1, wt = -2}, 1: {node = 0, wt = -2}}.
# You will encounter an infinite loop. Therefore, distances should always be positive.
# Also note that a simple Queue can also be used, but a priority queue is greedy in the sense that it
# first looks for the shortest available distance, thereby avoiding comparisons with higher distances.
def dijkstra(graph, source):
    # The time complexity is O(E*log(V)) and space complexity O(V) to store all the
    # nodes in the priority queue.

    # create a priority queue (pq) to store nodes and distances from source node.
    heap = MinHeap()

    # push the source node into the pq with a distance 0 because the starting node
    # will always be at a 0 distance from itself.
    heap.insert((0, source))

    # create a distances dictionary which we will be finally returning. Initialize
    # all of them by infinity at the start and just change the distance of source
    # node to 0.
    distances = {i: float('inf') for i in graph}
    distances[source] = 0

    # while the pq is not empty, we will continuously find the minimum distance
    # from the source node.
    while len(heap.heap) != 0:
        # get the next nearest node
        parent_distance, current_node = heap.pop()

        # for all the adjacent nodes of the next nearest node
        for adj in graph[current_node]:
            adj_node, distance_from_parent = adj

            # check if the distance of the adjacent node from source node can
            # be minimized or not. If it can be, then update the distances dictionary
            # and push the adjacent node's details with the updated distance back
            # into the priority queue.
            if distances[adj_node] > parent_distance + distance_from_parent:
                distances[adj_node] = parent_distance + distance_from_parent
                heap.insert((distances[adj_node], adj_node))

    # once the pq gets empty, then distances dictionary would have stored the minimum
    # distance it would take to reach all the nodes from source node.
    return distances


print(
    dijkstra(
        {
            0: [[1, 4], [2, 4]],
            1: [[0, 4], [2, 2]],
            2: [[0, 4], [1, 2], [3, 3], [4, 1], [5, 6]],
            3: [[2, 3], [5, 2]],
            4: [[2, 1], [5, 3]],
            5: [[2, 6], [3, 2], [4, 3]]
        },
        0
    )
)

print(
    dijkstra(
        {
            0: [[1, 9]],
            1: [[0, 9]]
        },
        0
    )
)

print(
    dijkstra(
        {
            0: [[1, 1], [2, 6]],
            1: [[0, 1], [2, 3]],
            2: [[0, 6], [1, 3]]
        },
        2
    )
)