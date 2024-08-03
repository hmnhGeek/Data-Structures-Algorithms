# Problem link - https://leetcode.com/problems/rotting-oranges/
# Solution - https://www.youtube.com/watch?v=yf3oUhkvqA0

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

    def enqueue(self, x):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return

        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        return None if self.is_empty() else self.head.data


def get_rotten_oranges(mtx, n, m):
    # Takes O(n*m) time.
    result = []
    for row in range(n):
        for col in range(m):
            # if the orange is rotten, add it to the result set
            if mtx[row][col] == 2:
                result.append((row, col))

    return result


def get_adjacent(mtx, x, y, n, m):
    # takes O(1) time.
    result = []

    # check if upper cell is in matrix
    if 0 <= x - 1 < n:
        result.append((x - 1, y))

    # check if lower cell is in matrix
    if 0 <= x + 1 < n:
        result.append((x + 1, y))

    # check if left cell is in matrix
    if 0 <= y - 1 < m:
        result.append((x, y - 1))

    # check if right cell is in matrix
    if 0 <= y + 1 < m:
        result.append((x, y + 1))

    return result


def rotten_oranges(mtx):
    # Overall time complexity is O(nm + E) and O(nm) space.

    # initialize n, m representing the number of rows and number of columns in the matrix
    n, m = len(mtx), len(mtx[0])

    # initialize a visited array denoting if a cell in the mtx has been traversed or not via BFS.
    visited = [[False for _ in range(m)] for _ in range(n)]

    # get all the initially rotten oranges as the starting nodes in O(nm) time.
    rotten = get_rotten_oranges(mtx, n, m)

    # initialize a Queue for BFS traversal.
    queue = Queue()

    # store the max time in which all the connected oranges will get rotten
    max_time = float('-inf')

    # mark the starting nodes as visited and push them to queue with a starting time t = 0.
    for ro in rotten:
        x, y = ro
        visited[x][y] = True
        queue.enqueue((x, y, 0))

    # typical BFS algorithm which runs in O(V + E) time where V <= nm. The queue holds at max O(V) nodes.
    while not queue.is_empty():
        x, y, t = queue.dequeue()

        # update the maximum time from the popped node
        max_time = max(max_time, t)

        # get all the adjacent nodes for cell (x, y) in O(1) time.
        adj_nodes = get_adjacent(mtx, x, y, n, m)

        # iterate on the adjacent nodes of the cell.
        for adj_node in adj_nodes:
            x0, y0 = adj_node

            # if the adjacent node is not rotten in the original matrix, and it is not yet visited,
            # then visit it and push it to queue with an incremental time value.
            if mtx[x0][y0] == 1 and not visited[x0][y0]:
                visited[x0][y0] = True
                queue.enqueue((x0, y0, t + 1))

    # now once again iterate on the original and visited matrices in O(nm) time.
    for row in range(n):
        for col in range(m):
            # at any point, if there is an orange, and it is not still visited even after the BFS,
            # then it implies that all the oranges cannot get rotten, return -1.
            if mtx[row][col] != 0 and visited[row][col] == 0:
                return -1

    # otherwise simply return the max time it will take to rotten all the oranges.
    return max_time


print(
    rotten_oranges(
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
    )
)


print(
    rotten_oranges(
        [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ]
    )
)

print(
    rotten_oranges(
        [
            [0, 2]
        ]
    )
)

print(
    rotten_oranges(
        [
            [0, 1, 2],
            [0, 1, 2],
            [2, 1, 1]
        ]
    )
)

print(
    rotten_oranges([[2, 2, 0, 1]])
)