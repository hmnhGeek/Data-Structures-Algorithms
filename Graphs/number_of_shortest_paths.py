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


def _get_num_shortest_paths(graph, source, destination):
    # initialize a queue and push source node with distance 0 into it.
    queue = Queue()
    queue.enqueue((source, 0))

    # initialize distances for all the nodes from source node.
    distances = {i: 0 if i == source else float('inf') for i in graph}

    # initialize a parent array to store all the parents which lie in the path
    # till node i.
    parents = {i: set() for i in graph}

    # standard BFS algorithm
    while not queue.is_empty():
        # get the current node with its minimum distance from source node.
        node, distance = queue.dequeue()

        # loop on the adjacent nodes of the current node.
        for adj in graph[node]:
            # store the adjacent node and the edge weight between node and the adjacent node.
            adj_node, weight = adj

            # if the minimum distance of adjacent node from source node is >= edge weight +
            # minimum distance of current node from source node, then update the minimum
            # distance of the adjacent node. Also, if the adjacent node is not destination
            # node, then add the current node as a parent to the set of parents of adj_node.
            # Finally, enqueue the adj_node with updated minimum distance from source node.
            if distances[adj_node] >= distance + weight:
                distances[adj_node] = distance + weight
                if node != destination:
                    parents[adj_node].add(node)
                queue.enqueue((adj_node, distances[adj_node]))

    # count the number of parents for all the nodes except source and destination.
    count_of_paths = {i: len(parents[i]) for i in parents if i != source and i != destination}

    # initialize a variable to count the number of shortest paths.
    num_of_shortest_paths = 0

    # loop in the parents array for the destination node,
    # which has all the parents with the shortest path.
    for parent in parents[destination]:
        # if the parent is the source node, then there is a direct shortest path.
        if parent == source:
            num_of_shortest_paths += 1
        else:
            # else increment number of shortest paths from the count_of_paths array
            num_of_shortest_paths += count_of_paths[parent]

    # return the number of shortest paths.
    return num_of_shortest_paths


def convert_to_graph(arr):
    graph = {}

    for i in range(len(arr)):
        source, dest, wt = arr[i]

        if source not in graph:
            graph[source] = [[dest, wt]]
        else:
            graph[source].append([dest, wt])

        if dest not in graph:
            graph[dest] = [[source, wt]]
        else:
            graph[dest].append([source, wt])

    return graph

print(
    _get_num_shortest_paths(
        {
            0: [[1, 2], [4, 5], [6, 7]],
            1: [[0, 2], [3, 3], [2, 3]],
            2: [[1, 3], [5, 1]],
            3: [[1, 3], [5, 1], [6, 3]],
            4: [[0, 5], [6, 2]],
            5: [[2, 1], [3, 1], [6, 1]],
            6: [[0, 7], [3, 3], [4, 2], [5, 1]]
        },
        0,
        6
    )
)

print(
    _get_num_shortest_paths(
        convert_to_graph([[0, 5, 8], [0, 2, 2], [0, 1, 1], [1, 3, 3], [1, 2, 3], [2, 5, 6], [3, 4, 2], [4, 5, 2]]),
        0,
        5
    )
)

print(
    _get_num_shortest_paths(
        {
            0: [[1, 1], [2, 2], [3, 1], [4, 2]],
            1: [[0, 1], [5, 2]],
            2: [[0, 2], [5, 1]],
            3: [[0, 1], [5, 2], [7, 3], [6, 2]],
            4: [[0, 2], [6, 1]],
            5: [[1, 2], [2, 1], [3, 2], [8, 1]],
            6: [[4, 1], [3, 2], [8, 1]],
            7: [[8, 1], [3, 3]],
            8: [[5, 1], [7, 1], [6, 1]]
        },
        0,
        8
    )
)