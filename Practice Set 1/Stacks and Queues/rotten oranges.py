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
    def _push_rotten_oranges(queue: Queue, mtx, visited, n, m):
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 2 and not visited[i][j]:
                    queue.push((i, j, 0))
                    visited[i][j] = True

    @staticmethod
    def _get_neighbours(mtx, i, j, visited, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1 and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1 and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1 and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1 and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _is_rotten_present(mtx, visited, n, m):
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1 and not visited[i][j]:
                    return True
        return False

    @staticmethod
    def rotten_oranges(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        t_max = 0
        queue = Queue()
        Solution._push_rotten_oranges(queue, mtx, visited, n, m)
        while not queue.is_empty():
            i, j, t = queue.pop()
            t_max = max(t_max, t)
            neighbours = Solution._get_neighbours(mtx, i, j, visited, n, m)
            for neighbour in neighbours:
                x, y = neighbour
                visited[x][y] = True
                queue.push((x, y, t + 1))
        rotten_present = Solution._is_rotten_present(mtx, visited, n, m)
        if rotten_present:
            return -1
        return t_max


print(Solution.rotten_oranges([[0, 1, 2],
                               [0, 1, 2],
                               [2, 1, 1]]))

print(Solution.rotten_oranges([[2, 2, 0, 1]]))

print(Solution.rotten_oranges([[2, 2, 2],
                               [0, 2, 0]]))
