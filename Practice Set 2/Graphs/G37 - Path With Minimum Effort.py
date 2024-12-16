class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


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
        queue = Queue()
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        distances[0][0] = 0
        queue.push((0, 0, 0))
        while not queue.is_empty():
            x, y, max_diff = queue.pop()
            neighbours = Solution._get_neighbours(mtx, x, y, n, m)
            for neighbour in neighbours:
                p, q = neighbour
                diff = abs(mtx[x][y] - mtx[p][q])
                if distances[p][q] > max(max_diff, diff):
                    distances[p][q] = max(max_diff, diff)
                    queue.push((p, q, max(max_diff, diff)))
        return distances[n - 1][m - 1]


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
