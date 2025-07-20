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
    def find_distance(matrix):
        """
            Time complexity is O(mn) and space complexity is O(mn).
        """
        n, m = len(matrix), len(matrix[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        queue = Queue()
        Solution.populate_queue(matrix, n, m, visited, distances, queue)
        while not queue.is_empty():
            i, j, d = queue.pop()
            neighbours = Solution._get_valid_neighbours(matrix, i, j, n, m, visited)
            for neighbour in neighbours:
                x, y = neighbour
                distances[x][y] = min(distances[x][y], d + 1)
                visited[x][y] = True
                queue.push((x, y, distances[x][y]))
        return distances

    @staticmethod
    def populate_queue(matrix, n, m, visited, distances, queue):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    visited[i][j] = True
                    distances[i][j] = 0
                    queue.push((i, j, 0))

    @staticmethod
    def _get_valid_neighbours(matrix, i, j, n, m, visited):
        result = []
        if n > i - 1 >= 0 == matrix[i - 1][j] and not visited[i - 1][j]:
            result.append((i - 1, j))
        if m > j + 1 >= 0 == matrix[i][j + 1] and not visited[i][j + 1]:
            result.append((i, j + 1))
        if n > i + 1 >= 0 == matrix[i + 1][j] and not visited[i + 1][j]:
            result.append((i + 1, j))
        if m > j - 1 >= 0 == matrix[i][j - 1] and not visited[i][j - 1]:
            result.append((i, j - 1))
        return result


print(
    Solution.find_distance(
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)
print(Solution.find_distance([[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]))
print(Solution.find_distance([[1, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(Solution.find_distance([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution.find_distance([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))