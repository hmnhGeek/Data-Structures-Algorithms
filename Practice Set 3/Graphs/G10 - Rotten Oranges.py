# Problem link - https://leetcode.com/problems/rotting-oranges/description/
# Solution - https://www.youtube.com/watch?v=yf3oUhkvqA0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=10


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
        if 0 <= i - 1 < n and mtx[i - 1][j] != 0:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] != 0:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] != 0:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] != 0:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _get_initial_nodes(mtx, n, m, queue):
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 2:
                    queue.push((i, j, 0))

    @staticmethod
    def rotten_oranges(mtx):
        """
            Time complexity is O(n*m) and space complexity is O(n*m).
        """

        n, m = len(mtx), len(mtx[0])
        queue = Queue()
        Solution._get_initial_nodes(mtx, n, m, queue)
        max_time_taken = 0
        while not queue.is_empty():
            i, j, t = queue.pop()
            max_time_taken = max(max_time_taken, t)
            neighbours = Solution._get_neighbours(mtx, i, j, n, m)
            for neighbour in neighbours:
                x, y = neighbour
                if mtx[x][y] == 1:
                    # rot here because if we rot after popping from the queue we would need additional conditions to
                    # avoid increasing the max value of time.
                    mtx[x][y] = 2
                    queue.push((x, y, t + 1))

        all_rottened = True
        for i in range(n):
            if 1 in mtx[i]:
                all_rottened = False
            print(mtx[i])
        return max_time_taken if all_rottened else -1


print(
    Solution.rotten_oranges(
        [
            [0, 1, 2],
            [0, 1, 2],
            [2, 1, 1]
        ]
    )
)

print(
    Solution.rotten_oranges([[2, 2, 0, 1]])
)

print(Solution.rotten_oranges([[2, 2, 2], [0, 2, 0]]))
print(Solution.rotten_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution.rotten_oranges([[0, 2]]))
print(Solution.rotten_oranges(
    [
        [2, 1, 0, 2, 1],
        [1, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ]
))
print(Solution.rotten_oranges(
    [
        [2, 1, 0, 2, 1],
        [0, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ]
))
