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
    def _get_rotten_oranges(mtx):
        rotten = []
        for i in range(len(mtx)):
            for j in range(len(mtx[0])):
                if mtx[i][j] == 2:
                    rotten.append((i, j))
        return rotten

    @staticmethod
    def _get_fresh_oranges(mtx):
        fresh = 0
        for i in range(len(mtx)):
            for j in range(len(mtx[0])):
                if mtx[i][j] == 1:
                    fresh += 1
        return fresh

    @staticmethod
    def _get_valid_neighbours(mtx, i, j):
        n, m = len(mtx), len(mtx[0])
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
    def rotten_oranges(mtx):
        """
            T: O(mn) and S: O(mn) for queue.
        """

        # O(mn) time.
        all_rotten_oranges = Solution._get_rotten_oranges(mtx)
        max_time_to_rot_all = 0
        queue = Queue()
        for rotten_orange in all_rotten_oranges:
            queue.push((*rotten_orange, 0))

        while not queue.is_empty():
            x, y, t = queue.pop()
            max_time_to_rot_all = max(max_time_to_rot_all, t)
            adj_fresh_oranges = Solution._get_valid_neighbours(mtx, x, y)
            for adj_fresh_orange in adj_fresh_oranges:
                mtx[adj_fresh_orange[0]][adj_fresh_orange[1]] = 2
                queue.push((*adj_fresh_orange, t + 1))

        # O(mn) time.
        all_fresh_oranges_count = Solution._get_fresh_oranges(mtx)
        if all_fresh_oranges_count >= 1:
            return -1
        return max_time_to_rot_all


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
print(Solution.rotten_oranges([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution.rotten_oranges([[0,2]]))
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