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
    def rotten_oranges(mtx):
        """
            Time complexity is O(nm) and space complexity is O(nm).
        """

        # get the initial rotten oranges in O(nm) time and O(nm) space in worst case.
        initial_rotten, n, m = Solution.get_rotten_oranges(mtx)

        # visited matrix occupying O(nm) space.
        visited = [[False for _ in range(m)] for _ in range(n)]

        # store the result variable denoting the total time taken to rot all the oranges.
        time_taken = 0

        # initialize a queue and push the rotten oranges into it. Also mark them visited as you go.
        queue = Queue()
        for o in initial_rotten:
            visited[o[0]][o[1]] = True
            queue.push((*o, 0))

        # typical BFS...
        while not queue.is_empty():
            # get the rotten orange from the queue.
            i, j, t0 = queue.pop()

            # update the time taken.
            time_taken = max(time_taken, t0)

            # get the fresh neighbour oranges.
            neighbours = Solution._get_neighbours(mtx, i, j, n, m, visited)

            # push these fresh oranges into the queue after rotting them.
            for neighbour in neighbours:
                x, y = neighbour
                visited[x][y] = True
                mtx[x][y] = 2
                queue.push((x, y, t0 + 1))

        # check if even a single fresh orange is still present.
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    return -1

        # return the minimum time taken to rot all the oranges.
        return time_taken

    @staticmethod
    def get_rotten_oranges(mtx):
        n, m = len(mtx), len(mtx[0])
        result = []
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 2:
                    result.append((i, j))
        return result, n, m

    @staticmethod
    def _get_neighbours(mtx, i, j, n, m, visited):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1 and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1 and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1 and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1 and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
        return neighbours


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