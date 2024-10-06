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


class DistanceCalculator:
    @staticmethod
    def _get_nearest_1(mtx, i, j, n, m):
        queue = Queue()
        queue.push((i, j, 0))
        while not queue.is_empty():
            x, y, d = queue.pop()
            if 0 <= x - 1 < n:
                if mtx[x - 1][y] == 0:
                    queue.push((x - 1, y, d + 1))
                else:
                    return d + 1
            if 0 <= y + 1 < m:
                if mtx[x][y + 1] == 0:
                    queue.push((x, y + 1, d + 1))
                else:
                    return d + 1
            if 0 <= x + 1 < n:
                if mtx[x + 1][y] == 0:
                    queue.push((x + 1, y, d + 1))
                else:
                    return d + 1
            if 0 <= y - 1 < m:
                if mtx[x][y - 1] == 0:
                    queue.push((x, y - 1, d + 1))
                else:
                    return d + 1

    @staticmethod
    def calc(mtx):
        n, m = len(mtx), len(mtx[0])
        result = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    result[i][j] = 0
                else:
                    nearest_1_distance = DistanceCalculator._get_nearest_1(mtx, i, j, n, m)
                    result[i][j] = nearest_1_distance
        return result


print(
    DistanceCalculator.calc(
        [
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 0]
        ]
    )
)

print(
    DistanceCalculator.calc(
        [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1]
        ]
    )
)

print(
    DistanceCalculator.calc(
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(DistanceCalculator.calc([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]))
print(DistanceCalculator.calc([[1, 0, 0], [0, 0, 1], [0, 1, 1]]))