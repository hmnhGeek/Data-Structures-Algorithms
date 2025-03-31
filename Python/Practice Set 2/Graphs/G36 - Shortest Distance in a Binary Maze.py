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
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def shortest_distance(mtx, source, destination):
        """
            Overall time complexity is O(m*n) and space complexity is O(m*n).
        """

        n, m = len(mtx), len(mtx[0])

        # edge case checks
        if source[0] not in range(n) or source[1] not in range(m):
            return
        if destination[0] not in range(n) or destination[1] not in range(m):
            return

        # mark source node in distance matrix as 0.
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        distances[source[0]][source[1]] = 0

        # push the source node into the queue.
        queue = Queue()
        queue.push((*source, 0))

        while not queue.is_empty():
            # pop the current cell
            x, y, distance = queue.pop()
            # get its valid neighbours
            neighbours = Solution._get_neighbours(mtx, x, y, n, m)
            for neighbour in neighbours:
                p, q = neighbour
                # update the distances if required and push it to the queue
                if distances[p][q] > distance + 1:
                    distances[p][q] = distance + 1
                    queue.push((p, q, distances[p][q]))

        # return the shortest distance of the destination cell from the source cell.
        return distances[destination[0]][destination[1]]


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
