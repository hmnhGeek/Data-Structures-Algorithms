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


class RottenOranges:
    @classmethod
    def _get_neighbours(cls, mtx, i, j, n, m):
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

    @classmethod
    def _get_rottened(cls, mtx, n, m, fresh=False):
        target = 2 if not fresh else 1
        result = []
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == target:
                    result.append((i, j))
        return result

    @staticmethod
    def rot(mtx):
        queue = Queue()
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        already_rotten = RottenOranges._get_rottened(mtx, n, m)
        for r in already_rotten:
            queue.push((r[0], r[1], 0))
        time_taken = 0
        while not queue.is_empty():
            x, y, t = queue.pop()
            if not visited[x][y]:
                time_taken = max(time_taken, t)
            visited[x][y] = True
            mtx[x][y] = 2
            neighbours = RottenOranges._get_neighbours(mtx, x, y, n, m)
            for neighbour in neighbours:
                x0, y0 = neighbour
                if not visited[x0][y0]:
                    queue.push((x0, y0, t + 1))
        return time_taken if len(RottenOranges._get_rottened(mtx, n, m, True)) == 0 else -1


print(
    RottenOranges.rot(
        [
            [0, 1, 2],
            [0, 1, 2],
            [2, 1, 1]
        ]
    )
)

print(RottenOranges.rot([[2, 2, 0, 1]]))
print(RottenOranges.rot([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(RottenOranges.rot([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(RottenOranges.rot([[0, 2]]))
