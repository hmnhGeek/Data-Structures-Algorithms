# Problem link - https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1
# Solution - https://www.youtube.com/watch?v=0ytpZyiZFhA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=37


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
        if 0 <= i - 1 < n:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def get_min_effort(mtx):
        """
            Time complexity is O(nm * log(nm)) and space complexity is O(nm).
        """

        n, m = len(mtx), len(mtx[0])

        # create a queue and push the starting node with max diff 0 into it.
        queue = Queue()
        distances = [[1e6 for _ in range(m)] for _ in range(n)]
        distances[0][0] = 0
        queue.push((0, 0, 0))

        # typical Dijkstra
        while not queue.is_empty():
            # pop the node in the path
            x, y, max_diff = queue.pop()
            # get all the neighbours in O(1) time.
            neighbours = Solution._get_neighbours(mtx, x, y, n, m)
            # iterate on the neighbours
            for neighbour in neighbours:
                p, q = neighbour
                # find the absolute difference between distance of (x, y) and (p, q).
                diff = abs(mtx[x][y] - mtx[p][q])
                # current distance of (p, q) > max difference of the path, then update it and push it into the queue.
                if distances[p][q] > max(max_diff, diff):
                    distances[p][q] = max(max_diff, diff)
                    queue.push((p, q, max(max_diff, diff)))
        # at the end, return the minimum distance of the bottom-right cell.
        return distances[n - 1][m - 1]


print(
    Solution.get_min_effort(
        [
            [1, 2, 2],
            [3, 8, 2],
            [5, 3, 5]
        ]
    )
)

print(Solution.get_min_effort([[7, 7], [7, 7]]))
print(Solution.get_min_effort([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(Solution.get_min_effort([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
print(Solution.get_min_effort([[1, 8, 8], [3, 8, 9], [5, 3, 5]]))
print(Solution.get_min_effort(
    [
        [1, 3, 1],
        [9, 9, 3],
        [9, 9, 1]
    ]
))
