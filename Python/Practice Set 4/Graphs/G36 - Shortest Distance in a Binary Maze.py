# Problem link - https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1
# Solution - https://www.youtube.com/watch?v=U5Mw4eyUmw4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=36


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
        node = self.head
        item = self.head.data
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def shortest_distance(graph, source, destination):
        """
            Overall time complexity is O(m*n*log(mn)) and space complexity is O(m*n).
        """
        n = len(graph)
        m = len(graph[0])
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        distances[source[0]][source[1]] = 0
        queue = Queue()
        queue.push((*source, 0))
        while not queue.is_empty():
            x, y, d = queue.pop()
            neighbours = Solution._get_neighbours(graph, x, y, n, m)
            for neighbour in neighbours:
                if distances[neighbour[0]][neighbour[1]] > 1 + d:
                    distances[neighbour[0]][neighbour[1]] = 1 + d
                    queue.push((*neighbour, 1 + d))
        return distances[destination[0]][destination[1]]

    @staticmethod
    def _get_neighbours(graph, x, y, n, m):
        neighbours = []
        if 0 <= x + 1 < n and graph[x + 1][y] == 1:
            neighbours.append((x + 1, y))
        if 0 <= y - 1 < m and graph[x][y - 1] == 1:
            neighbours.append((x, y - 1))
        if 0 <= x - 1 < n and graph[x - 1][y] == 1:
            neighbours.append((x - 1, y))
        if 0 <= y + 1 < m and graph[x][y + 1] == 1:
            neighbours.append((x, y + 1))
        return neighbours


print(
    Solution.shortest_distance(
        [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 0]
        ],
        (0, 1),
        (2, 2)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1]
        ],
        (0, 0),
        (3, 4)
    )
)

print(
    Solution.shortest_distance(
        [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
         [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]],
        (0, 0),
        (3, 4)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 1, 1, 1],
            [0, 1, 1, 0],
            [0, 0, 1, 1]
        ],
        (0, 0),
        (2, 3)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 1],
            [0, 1]
        ],
        (0, 0),
        (1, 1)
    )
)

print(
    Solution.shortest_distance(
        [
            [1, 0],
            [0, 1]
        ],
        (0, 0),
        (1, 1)
    )
)
