# Problem link - https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1
# Solution - https://www.youtube.com/watch?v=C-2_uSRli8o&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=9


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
    def _get_valid_neighbours(mtx, i, j, n, m, start_color):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == start_color:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == start_color:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == start_color:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == start_color:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def flood_fill(mtx, new_color, x, y):
        # Time complexity is O(V + E) = O(n*m + E) = O(nm) and space complexity is O(nm) for the queue.

        # get dimensions of mtx
        n, m = len(mtx), len(mtx[0])
        # if the starting cell is not in mtx return
        if not (0 <= x < n and 0 <= y < m):
            return

        # note the starting color.
        start_color = mtx[x][y]
        # if the new color and starting color are same, do nothing and return
        if start_color == new_color:
            return

        # initialize a queue for BFS
        queue = Queue()
        # push starting cell into the queue.
        queue.push((x, y))

        # perform the BFS
        while not queue.is_empty():
            # get the current cell.
            i, j = queue.pop()

            # if the popped cell has start color, color it with the new color.
            if mtx[i][j] == start_color:
                mtx[i][j] = new_color

            # get valid neighbours of the current cell (valid are those which have color equal to the starting color).
            # This would also mean that they are not yet visited.
            neighbours = Solution._get_valid_neighbours(mtx, i, j, n, m, start_color)

            # push these valid neighbours into the queue.
            for neighbour in neighbours:
                queue.push(neighbour)
        # return from the method call.
        return

    @staticmethod
    def test(mtx, new_color, x, y):
        Solution.flood_fill(mtx, new_color, x, y)
        for i in range(len(mtx)):
            print(mtx[i])
        print()


Solution.test(
    [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ],
    2,
    1,
    1
)

Solution.test(
    [[0, 0, 0], [0, 0, 0]],
    0, 0, 0
)

Solution.test(
    [[0, 0, 0], [0, 0, 0]], 0, 0, 0
)

Solution.test(
    [
        [0, 0, 0],
        [0, 1, 1]
    ],
    1,
    1,
    1
)

Solution.test(
    [
        [2, 2, 2],
        [2, 2, 2]
    ],
    1,
    0, 0
)