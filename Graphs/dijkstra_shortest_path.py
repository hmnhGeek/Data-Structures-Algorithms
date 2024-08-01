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
            return
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
        if self.heap[min_child_index] > self.heap[rci]:
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
        if self.heap == []:
            return

        item = self.heap[0]
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        del self.heap[len(self.heap) - 1]
        self.min_heapify_down(0)
        return item


def get_shortest_path(graph, source, end):
    # Time complexity is O(E*log(V) + V). V is added because to traverse the path we are looping for V nodes.
    # Space complexity is O(V) for storing paths and using the priority queue.

    # if either of the nodes is not present in the graph, return -1.
    if source not in graph or end not in graph:
        return -1

    # initialize a priority queue and push the source node with distance 0 into it.
    pq = MinHeap()
    pq.insert((0, source))

    # create distances and parents dictionaries. The idea is to update the parents
    # whenever a shorter path is discovered. At the end, we will just backtrack
    # from end node to source node to find the path from the `parents` dictionary.
    distances = {i: float('inf') for i in graph}
    distances[source] = 0
    parents = {i: None for i in graph}

    # till the time the priority queue is not empty
    while len(pq.heap) != 0:
        # pop the current node and its distance from the source node.
        parent_distance, node = pq.pop()

        # traverse to all the adjacent nodes of the popped node.
        for adj in graph[node]:
            adj_node, weight = adj

            # if a shorter distance from the source node to this adjacent node is found,
            # update the distances array for this adjacent node and update the parents
            # array with the parent of adj_node as node. Insert the adjacent node back
            # to the priority queue.
            if parent_distance + weight < distances[adj_node]:
                distances[adj_node] = parent_distance + weight
                parents[adj_node] = node
                pq.insert((distances[adj_node], adj_node))

    # once the priority queue is empty, we would have the minium distances and the respective
    # parents from the source node. To trace the path, start from the end node till you reach
    # the source node.
    parent = parents[end]
    path = [end]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]

    # if the last node in the path is the source node, return the path by reversing it.
    if path[-1] == source:
        return path[-1: -len(path) - 1: -1]

    # else it means that it was impossible to travel from source node to end node, return -1.
    return -1


print(
    get_shortest_path(
        {
            1: [[2, 2], [4, 1]],
            2: [[1, 2], [3, 4], [5, 5]],
            3: [[2, 4], [5, 1], [4, 3]],
            4: [[1, 1], [3, 3]],
            5: [[2, 5], [3, 1]]
        },
        1,
        5
    )
)

print(
    get_shortest_path(
        {
            1: [[2, 2]],
            2: [[1, 2]]
        },
        1,
        2
    )
)

print(
    get_shortest_path(
        {
            1: [[2, 2]],
            2: [[1, 2]],
            3: []
        },
        1,
        3
    )
)

print(
    get_shortest_path(
        {
            1: [[2, 2], [4, 1]],
            2: [[1, 2], [3, 4], [5, 5]],
            3: [[2, 4], [5, 1], [4, 3]],
            4: [[1, 1], [3, 3]],
            5: [[2, 5], [3, 1]]
        },
        3,
        1
    )
)