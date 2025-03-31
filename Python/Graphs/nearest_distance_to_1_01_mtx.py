# Problem link - https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1
# Solution - https://www.youtube.com/watch?v=edXdVwkYHF8


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

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


def get_adjacent_nodes(mtx, i, j, n, m):
    # This function returns the 0-valued adjacent nodes of cell (i, j) in O(1) time and O(1) space.
    result = []

    if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
        result.append((i - 1, j))
    if 0 <= j + 1 < m and mtx[i][j + 1] == 0:
        result.append((i, j + 1))
    if 0 <= i + 1 < n and mtx[i + 1][j] == 0:
        result.append((i + 1, j))
    if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
        result.append((i, j - 1))

    return result


def binary_mtx_nearest_1(mtx):
    n, m = len(mtx), len(mtx[0])

    # Both visited and distances matrices will take additional O(nm) space. Hence space complexity is O(nm) and time
    # complexity is also O(nm) because of the while loop.

    # create a visited matrix to not to unnecessarily bloat the queue.
    visited = [[False for _ in range(m)] for _ in range(n)]

    # initialize a distances matrix with inf distance of "nearest 1" for all the nodes.
    distances = [[float('inf') for _ in range(m)] for _ in range(n)]

    # initialize a blank queue for BFS traversal.
    queue = Queue()

    # fill the queue with starting nodes as those which are of value 1 in the matrix (with a distance 0). The idea is
    # to solve this problem in reverse order. Basically find the level order distance of all the nodes from 1 and that
    # will be the same distance from other nodes to these 1s.
    for i in range(n):
        for j in range(m):
            if mtx[i][j] == 1:
                queue.enqueue((i, j, 0))

    # typical BFS algorithm which will run for n*m times (for storing all nm nodes).
    while not queue.is_empty():
        # pop the current node in O(1) time.
        i, j, dist = queue.dequeue()

        # mark the node visited and update the distance of this node with minimum value.
        visited[i][j] = True
        distances[i][j] = min(dist, distances[i][j])

        # get all the adjacent nodes which are 0. We only need to check for 0-valued nodes, as 1-valued nodes will be
        # already covered in the starting push.
        adj_nodes = get_adjacent_nodes(mtx, i, j, n, m)
        for adj_node in adj_nodes:
            # check if the adjacent node is already visited or not and if not visited, push it to queue but increment
            # the distance by 1 unit for the next level in BFS. It takes O(1) time.
            if not visited[adj_node[0]][adj_node[1]]:
                queue.enqueue((adj_node[0], adj_node[1], dist + 1))

    # finally return the closest distance of 1-valued nodes for all the nodes in the matrix.
    return distances


print(
    binary_mtx_nearest_1(
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(
    binary_mtx_nearest_1(
        [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
    )
)

print(
    binary_mtx_nearest_1(
        [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
    )
)

print(
    binary_mtx_nearest_1(
        [
            [0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 0]
        ]
    )
)

print(
    binary_mtx_nearest_1(
        [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 1]
        ]
    )
)
