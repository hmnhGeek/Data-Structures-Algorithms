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
                self.heap[min_child_index], self.heap[pi] = self.heap[pi], self.heap[min_child_index]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi] > self.heap[min_child_index]:
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


class HeapElement:
    def __init__(self, distance, i, j):
        self.d = distance
        self.i = i
        self.j = j

    def __lt__(self, other):
        return self.d < other.d

    def __gt__(self, other):
        return self.d > other.d


class Solution:
    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def get_min_effort(mtx):
        n, m = len(mtx), len(mtx[0])
        pq = MinHeap()
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        distances[0][0] = 0
        pq.insert(HeapElement(0, 0, 0))
        while not pq.is_empty():
            heap_element = pq.pop()
            distance, x, y = heap_element.d, heap_element.i, heap_element.j
            if x == n - 1 and y == m - 1:
                return distance
            neighbours = Solution._get_neighbours(mtx, x, y, n, m)
            for neighbour in neighbours:
                d = abs(mtx[neighbour[0]][neighbour[1]] - mtx[x][y])
                path_effort = max(d, distance)
                if path_effort < distances[neighbour[0]][neighbour[1]]:
                    distances[neighbour[0]][neighbour[1]] = path_effort
                    pq.insert(HeapElement(path_effort, *neighbour))
        return -1


print()
print("Optimal Solution")
print(
    Solution.get_min_effort(
        [
            [1, 2, 2],
            [3, 8, 2],
            [5, 3, 5]
        ]
    )
)

print(Solution.get_min_effort([[7, 7], [7, 7]]))
print(Solution.get_min_effort([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(Solution.get_min_effort([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
print(Solution.get_min_effort([[1, 8, 8], [3, 8, 9], [5, 3, 5]]))
print(Solution.get_min_effort(
    [
        [1, 3, 1],
        [9, 9, 3],
        [9, 9, 1]
    ]
))
