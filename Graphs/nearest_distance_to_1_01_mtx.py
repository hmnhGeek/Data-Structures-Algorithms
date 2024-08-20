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

    def enqueue(self, x):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


def get_adjacent_nodes(mtx, i, j, n, m):
    result = []

    if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
        result.append((i - 1, j))
    if 0 <= j + 1 < m and mtx[i][j + 1] == 0:
        result.append((i, j + 1))
    if 0 <= i + 1 < n and mtx[i + 1][j] == 0:
        result.append((i + 1, j))
    if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
        result.append((i, j - 1))

    return result


def binary_mtx_nearest_1(mtx):
    n, m = len(mtx), len(mtx[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    distances = [[0 for _ in range(m)] for _ in range(n)]
    queue = Queue()

    for i in range(n):
        for j in range(m):
            if mtx[i][j] == 1:
                queue.enqueue((i, j, 0))

    while not queue.is_empty():
        i, j, dist = queue.dequeue()
        visited[i][j] = True
        distances[i][j] = dist

        adj_nodes = get_adjacent_nodes(mtx, i, j, n, m)
        for adj_node in adj_nodes:
            if not visited[adj_node[0]][adj_node[1]]:
                queue.enqueue((adj_node[0], adj_node[1], dist + 1))

    return distances


print(
    binary_mtx_nearest_1(
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(
    binary_mtx_nearest_1(
        [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
    )
)

print(
    binary_mtx_nearest_1(
        [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
    )
)
