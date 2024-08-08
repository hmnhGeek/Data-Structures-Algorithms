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

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


def populate_edge_list(mtx, i, j, n, m, edge_list):
    # In O(1) time, this function populates the edge list for node (i, j).
    if 0 <= i - 1 < n:
        edge_list.append((abs(mtx[i - 1][j] - mtx[i][j]), (i - 1, j)))
    if 0 <= j + 1 < m:
        edge_list.append((abs(mtx[i][j + 1] - mtx[i][j]), (i, j + 1)))
    if 0 <= i + 1 < n:
        edge_list.append((abs(mtx[i + 1][j] - mtx[i][j]), (i + 1, j)))
    if 0 <= j - 1 < m:
        edge_list.append((abs(mtx[i][j - 1] - mtx[i][j]), (i, j - 1)))


def convert_to_graph(mtx):
    # this function converts the matrix to a graph representation. In this conversion,
    # the graph obtained has each node connected to its all the adjacent nodes from the
    # matrix. If cells (i, j) and (x, y) are adjacent, then the weight between them is
    # the absolute difference of mtx[i][j] - mtx[x][y], i.e. |mtx[i][j] - mtx[x][y]|.
    # Overall time complexity of this function is O(m*n) and space is O(4*m*n) with each
    # node having 4 adjacent nodes in the worst case.
    n, m = len(mtx), len(mtx[0])
    graph = {}

    for i in range(n):
        for j in range(m):
            edge_list = []
            populate_edge_list(mtx, i, j, n, m, edge_list)
            graph[(i, j)] = edge_list

    return graph


def get_shortest_path(graph, n, m):
    # Since we are using a queue data structure and not a PQ for Dijkstra here,
    # the time complexity is O(V + E) = O(nm + {2nm - n -m}) = O(nm).
    # Space complexity is O(nm) because in the worst case, the queue will hold
    # all the vertices from the graph.

    # Initialize an empty queue and push the start node (0, 0) with difference 0.
    # We will be using standard Dijkstra's algorithm to compute maximum height
    # delta on each path.
    queue = Queue()
    queue.enqueue((0, (0, 0)))

    # store the minimum differences as infinities.
    min_diffs = {i: float('inf') for i in graph}

    while not queue.is_empty():
        # get the current node from the queue and the minimum effort required to reach it, for now.
        effort, node = queue.dequeue()

        # loop on all the adjacent nodes of this node.
        for adj in graph[node]:
            eff, adj_node = adj

            # if the minimum difference of this adjacent node is more than maximum effort, then
            # update the min_diff of this adjacent node and push the adj_node into the queue.
            # To be more clear, what we are doing here is this: we popped a node from the queue,
            # which in the current path tells that `effort` is the minimum effort till now on this
            # path. If `eff` effort from the adjacent node (from node) is more than `effort`, then
            # it means that on this path, maximum effort is `eff`, isn't it? And if this maximum
            # effort is less than the previously stored maximum effort of adjacent node, then we
            # just update the min_diffs for this adjacent node.
            max_effort_on_current_path = max(eff, effort)
            if min_diffs[adj_node] > max_effort_on_current_path:
                min_diffs[adj_node] = max_effort_on_current_path
                queue.enqueue((min_diffs[adj_node], adj_node))

    # finally, the last node in the min_diffs (and also from the matrix) is the minimum max-effort
    # required from all the possible paths.
    return min_diffs[(n - 1, m - 1)]


def get_min_effort(mtx):
    # first get the graph representation of the problem by converting the matrix into a graph.
    graph = convert_to_graph(mtx)

    # then return the min effort required to reach (n - 1, m - 1) from (0, 0).
    # it's not a direct shortest path, but the distance with minimum height change.
    return get_shortest_path(graph, len(mtx), len(mtx[0]))


print(
    get_min_effort(
        [
            [1, 2, 2],
            [3, 8, 2],
            [5, 3, 5]
        ]
    )
)

print(
    get_min_effort(
        [
            [7, 7],
            [7, 7]
        ]
    )
)

print(get_min_effort([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))

print(
    get_min_effort(
        [
            [1, 3, 1],
            [9, 9, 3],
            [9, 9, 1]
        ]
    )
)

print(
    get_min_effort(
        [
            [2, 6],
            [8, 0],
            [9, 7]
        ]
    )
)