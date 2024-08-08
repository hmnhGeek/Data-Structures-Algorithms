# Problem link - https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1

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

        if self.is_empty():
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


def get_cell(mtx, i, j, n, m):
    # This function checks if a cell of value equal to 1 is available at coordinate (i, j) in the mtx.
    # This takes O(1) time.
    if 0 <= i < n and 0 <= j < m and mtx[i][j] == 1:
        return [(i, j)]
    return []


def convert_mtx_to_graph(mtx):
    # This function, in O(m*n) time, computes the adjacency matrix of the given matrix.
    # This also takes O(4*V) = O(4*m*n) = O(m*n) space.
    n, m = len(mtx), len(mtx[0])
    graph = {}

    # traverse in the matrix
    for i in range(n):
        for j in range(m):
            # if the cell at (i, j) is 1, check its neighbours (if they are also 1s).
            if mtx[i][j] == 1:
                # populate the edge list with those neighbours which are 1. In the worst case,
                # each cell can have 4 neighbours, and hence, 4*V.
                edge_list = []
                edge_list.extend(get_cell(mtx, i - 1, j, n, m))
                edge_list.extend(get_cell(mtx, i, j + 1, n, m))
                edge_list.extend(get_cell(mtx, i + 1, j, n, m))
                edge_list.extend(get_cell(mtx, i, j - 1, n, m))

                # assign the node in the graph with its adjacent cells.
                graph[(i, j)] = edge_list

    return graph


def get_shortest_distance(graph, source, end):
    # This algorith is a classical BFS algorithm using queue data structure.
    # Time complexity is O(V+E) = O(m*n) and space is O(V).

    # initialize the distances of all the nodes from the source node.
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # initialize a visited dictionary to maintain BFS traversal.
    visited = {i: False for i in graph}

    # initialize an empty queue and push source node with distance 0.
    queue = Queue()
    queue.enqueue((0, source))

    while not queue.is_empty():
        # pop the current node with its distance from the source node. Also, mark the node visited.
        distance, node = queue.dequeue()
        visited[node] = True

        # loop on all the adjacent nodes of the graph
        for adj_node in graph[node]:
            # if the adjacent node is not visited and its new distance from the source node is lesser than
            # the previous distance, then update the distances array for this node and push it to the queue.
            if not visited[adj_node] and 1 + distance < distances[adj_node]:
                distances[adj_node] = 1 + distance
                queue.enqueue((1 + distance, adj_node))

    # at the end, return the shortest distance from source node to the end node.
    return distances[end]


def get_shortest(mtx, start, end):
    # Time complexity is O(m*n) and space is O(m*n) for generating the adjacency matrix.
    graph = convert_mtx_to_graph(mtx)
    return get_shortest_distance(graph, start, end)


print(
    get_shortest(
        [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 1]
        ],
        (0, 1),
        (2, 2)
    )
)

print(
    get_shortest(
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
    get_shortest(
        [
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
            ],
        (0, 0),
        (3, 4)
    )
)