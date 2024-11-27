# Problem link - https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1
# Solution - https://www.youtube.com/watch?v=edXdVwkYHF8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=13


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
    def _get_valid_neighbours(i, j, n, m, visited):
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
    def _bfs(mtx, i, j, n, m):
        queue = Queue()
        visited = [[False for _ in range(m)] for _ in range(n)]
        queue.push((i, j, 0))
        while not queue.is_empty():
            x, y, d = queue.pop()
            visited[x][y] = True
            if mtx[x][y] == 1:
                return d
            neighbours = Solution._get_valid_neighbours(x, y, n, m, visited)
            for neighbour in neighbours:
                queue.push((*neighbour, d + 1))

    @staticmethod
    def get_nearest_1s(mtx):
        """
            This will take O(m^2 * n^2) time and O(mn) space.
        """

        n, m = len(mtx), len(mtx[0])
        result = [[None for _ in range(m)] for _ in range(n)]

        # for each cell in the matrix, use BFS to determine the nearest 1.
        for i in range(n):
            for j in range(m):
                nearest_1_distance = Solution._bfs(mtx, i, j, n, m)
                if nearest_1_distance is not None:
                    result[i][j] = nearest_1_distance
        for i in result:
            print(i)
        print()


class BetterSolution:
    @staticmethod
    def _get_valid_neighbours(i, j, n, m, visited):
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
    def get_nearest_1s(mtx):
        """
            Overall time complexity is O(mn) and space is O(mn).
        """

        n, m = len(mtx), len(mtx[0])
        result = [[1e6 for _ in range(m)] for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        queue = Queue()

        # push all the starting 1s into the queue in O(mn) time.
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    queue.push((i, j, 0))

        while not queue.is_empty():
            x, y, d = queue.pop()
            visited[x][y] = True
            result[x][y] = min(d, result[x][y])
            neighbours = BetterSolution._get_valid_neighbours(x, y, n, m, visited)
            for neighbour in neighbours:
                queue.push((*neighbour, d + 1))

        for i in result:
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

print()
print()

BetterSolution.get_nearest_1s(
    [
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ]
)

BetterSolution.get_nearest_1s(
    [
        [1, 0, 1],
        [1, 1, 0],
        [1, 0, 0]
    ]
)

BetterSolution.get_nearest_1s([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
BetterSolution.get_nearest_1s(
    [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 0]
    ]
)