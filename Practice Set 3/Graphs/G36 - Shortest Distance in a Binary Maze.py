class Node:
    def __init__(self, distance, i, j):
        self.i = i
        self.j = j
        self.d = distance


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
        if self.heap[rci].d < self.heap[min_child_index].d:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].d > self.heap[min_child_index].d:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].d > self.heap[min_child_index].d:
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
    def shortest_distance(mtx, source, destination):
        n, m = len(mtx), len(mtx[0])
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        distances[source[0]][source[1]] = 0
        pq = MinHeap()
        pq.insert(Node(0, *source))
        while not pq.is_empty():
            node = pq.pop()
            neighbours = Solution._get_neighbours(mtx, node.i, node.j, n, m)
            for neighbour in neighbours:
                x, y = neighbour
                if distances[x][y] > node.d + 1:
                    distances[x][y] = node.d + 1
                    pq.insert(Node(distances[x][y], x, y))
        return distances[destination[0]][destination[1]]

    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1:
            neighbours.append((i, j - 1))
        return neighbours


print(
    Solution.shortest_distance(
        [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 0]
        ],
        (0, 1),
        (2, 2)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1]
        ],
        (0, 0),
        (3, 4)
    )
)

print(
    Solution.shortest_distance(
        [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
         [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]],
        (0, 0),
        (3, 4)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 1, 1, 1],
            [0, 1, 1, 0],
            [0, 0, 1, 1]
        ],
        (0, 0),
        (2, 3)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 1],
            [0, 1]
        ],
        (0, 0),
        (1, 1)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 0],
            [0, 1]
        ],
        (0, 0),
        (1, 1)
    )
)
