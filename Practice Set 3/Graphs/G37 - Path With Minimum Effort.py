class Solution:
    @staticmethod
    def _get_neighbours(mtx, i, j, n, m, visited):
        neighbours = []
        if 0 <= i - 1 < n and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _solve(mtx, i, j, max_path_effort, min_effort, visited, n, m):
        if i == 0 and j == 0:
            min_effort[0] = min(min_effort[0], max_path_effort)
            return

        # mark the current cell as path visited.
        visited[i][j] = True

        # get the neighbours in constant time.
        neighbours = Solution._get_neighbours(mtx, i, j, n, m, visited)

        # loop on the neighbours
        for neighbour in neighbours:
            x, y = neighbour[0], neighbour[1]
            # recursively find the max path effort
            Solution._solve(mtx, x, y, max(max_path_effort, abs(mtx[i][j] - mtx[x][y])), min_effort, visited, n, m)

        # while returning, unmark the cell from path visited.
        visited[i][j] = False
        return

    @staticmethod
    def get_min_effort(mtx):
        n, m = len(mtx), len(mtx[0])

        # This will take O(mn) space.
        visited = [[False for _ in range(m)] for _ in range(n)]

        # store the global min effort as reference.
        min_effort = [1e6,]

        # start traversals from the last cell.
        Solution._solve(mtx, n - 1, m - 1, -1e6, min_effort, visited, n, m)

        # return the min effort.
        return min_effort[0]


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


class MinHeap:
    def __int__(self):
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


