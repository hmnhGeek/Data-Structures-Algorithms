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
    def get_nearest_1s(mtx):
        n, m = len(mtx), len(mtx[0])
        queue = Queue()
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    distances[i][j] = 0
                    queue.push((i, j, 0))
        while not queue.is_empty():
            x, y, distance = queue.pop()
            neighbours = Solution._get_neighbours(mtx, x, y, n, m)
            for neighbour in neighbours:
                x0, y0 = neighbour
                if distances[x0][y0] > distance + 1:
                    queue.push((x0, y0, distance + 1))
                    distances[x0][y0] = distance + 1
        for i in distances:
            print(i)
        print()


Solution.get_nearest_1s(
    [
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ]
)

Solution.get_nearest_1s(
    [
        [1, 0, 1],
        [1, 1, 0],
        [1, 0, 0]
    ]
)

Solution.get_nearest_1s([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
Solution.get_nearest_1s(
    [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 0]
    ]
)
