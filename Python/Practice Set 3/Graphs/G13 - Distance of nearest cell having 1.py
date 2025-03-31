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
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 0:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 0:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def find_distance(mtx):
        """
            Time complexity is O(mn) and space complexity is O(mn).
        """

        n, m = len(mtx), len(mtx[0])

        # create a visited and distances matrix, initialized with False and inf for all the cells.
        visited = [[False for _ in range(m)] for _ in range(n)]
        distances = [[1e6 for _ in range(m)] for _ in range(n)]

        # create a queue and push all the 1s into it with distance as 0. This will take O(nm) time.
        queue = Queue()
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    queue.push((i, j, 0))

        # while not queue is empty (standard BFS)
        while not queue.is_empty():
            # pop the node and the minimum distance from 1
            i, j, distance = queue.pop()
            # mark the node as visited
            visited[i][j] = True
            # update the distance matrix
            distances[i][j] = min(distances[i][j], distance)
            # get the neighbours of the node
            neighbours = Solution._get_neighbours(mtx, i, j, n, m)
            # loop on the neighbours and if it is not visited, push it to queue with 1 unit incremented distance.
            for neighbour in neighbours:
                x, y = neighbour
                if not visited[x][y]:
                    queue.push((x, y, distance + 1))
        # return the distances.
        return distances


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
