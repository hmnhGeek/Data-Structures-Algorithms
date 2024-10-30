class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2 * pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2 * pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1) / 2)
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


class BinaryMaze:
    def __init__(self, maze):
        self.graph = maze
        self.n = len(maze)
        self.m = len(maze[0])

    def _get_valid_neighbours(self, i, j):
        neighbours = []

        if 0 <= i - 1 < self.n and self.graph[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < self.m and self.graph[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < self.n and self.graph[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < self.m and self.graph[i][j - 1] == 1:
            neighbours.append((i, j - 1))

        return neighbours

    def shortest_distance(self, from_node, to_node):
        xi, yi = from_node
        xj, yj = to_node
        if 0 <= xi < self.n and 0 <= xj < self.n and 0 <= yi < self.m and 0 <= yj < self.m:
            pq = MinHeap()
            distances = {i: 1e6 for i in range(self.n * self.m)}
            distances[xi * self.m + yi] = 0
            pq.insert((distances[xi * self.m + yi], xi, yi))

            while not pq.is_empty():
                distance, x0, y0 = pq.pop()
                neighbours = self._get_valid_neighbours(x0, y0)
                for neighbour in neighbours:
                    x1, y1 = neighbour
                    adj_node = x1 * self.m + y1
                    if distances[adj_node] > distance + 1:
                        distances[adj_node] = distance + 1
                        pq.insert((distances[adj_node], x1, y1))

            return distances[xj * self.m + yj]


print(
    BinaryMaze(
        [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 0]
        ]
    ).shortest_distance((0, 1), (2, 2))
)

print(
    BinaryMaze(
        [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0],
         [1, 0, 1, 0, 1]]
    ).shortest_distance((0, 0), (3, 4))
)
