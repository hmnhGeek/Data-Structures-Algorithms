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
    def _get_valid_neighbours(mtx, i, j, n, m, start_color):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == start_color:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == start_color:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == start_color:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == start_color:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def flood_fill(mtx, new_color, x, y):
        n, m = len(mtx), len(mtx[0])
        if not (0 <= x < n and 0 <= y < m):
            return
        if mtx[x][y] == 0:
            return
        queue = Queue()
        start_color = mtx[x][y]
        queue.push((x, y))
        while not queue.is_empty():
            i, j = queue.pop()
            if mtx[i][j] == start_color:
                mtx[i][j] = new_color
            neighbours = Solution._get_valid_neighbours(mtx, i, j, n, m, start_color)
            for neighbour in neighbours:
                queue.push(neighbour)
        return

    @staticmethod
    def test(mtx, new_color, x, y):
        Solution.flood_fill(mtx, new_color, x, y)
        for i in range(len(mtx)):
            print(mtx[i])
        print()


Solution.test(
    [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ],
    2,
    1,
    1
)

Solution.test(
    [[0, 0, 0], [0, 0, 0]],
    0, 0, 0
)

Solution.test(
    [[0, 0, 0], [0, 0, 0]], 0, 0, 0
)
