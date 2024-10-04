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


class FloodFill:
    @classmethod
    def _get_neighbours(cls, matrix, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and matrix[i - 1][j] != 0:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and matrix[i][j + 1] != 0:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and matrix[i + 1][j] != 0:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and matrix[i][j - 1] != 0:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def bfs(graph, start_x, start_y, new_color):
        queue = Queue()
        queue.push((start_x, start_y))
        n, m = len(graph), len(graph[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        while not queue.is_empty():
            x, y = queue.pop()
            visited[x][y] = True
            original = graph[x][y]
            if graph[x][y] != new_color:
                graph[x][y] = new_color

            neighbours = FloodFill._get_neighbours(graph, x, y, n, m)
            for adj in neighbours:
                x0, y0 = adj
                if graph[x0][y0] == original and not visited[x0][y0]:
                    queue.push((x0, y0))
        return graph


print(
    FloodFill.bfs(
        [
            [1, 1, 1],
            [2, 2, 0],
            [2, 2, 2]
        ],
        2, 0, 3
    )
)

print(FloodFill.bfs([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(FloodFill.bfs([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
