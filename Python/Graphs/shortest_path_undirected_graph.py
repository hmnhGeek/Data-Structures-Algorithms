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

    def front(self):
        return self.head.data if not self.is_empty() else None


def get_shortest_path(g, source):
    '''
        Because we are using a BFS algorithm, the time complexity is O(V + 2E)
        And space complexity is O(2E + V), because V nodes will be stored in the stack.
    '''

    # initially all the nodes will be at infinite distance from the source
    # only the source node will be at distance 0 from itself.
    distances = {i: float('inf') for i in g}
    distances[source] = 0

    # initialize a queue and add the source node into it.
    queue = Queue()
    queue.enqueue(source)

    # typical BFS algorithm (no topological sort)
    while not queue.is_empty():
        # pop the current node and store its distance from the source node
        node = queue.dequeue()
        parent_distance = distances[node]

        # for all the adjacent nodes of this source nodes,
        # if the distance stored previously is greater than the current distance
        # from the parent, update the distance for this adjacent node and push
        # the adjacent node into the queue.
        for adj_node in g[node]:
            if distances[adj_node] > parent_distance + 1:
                distances[adj_node] = parent_distance + 1
                queue.enqueue(adj_node)

    # return the calculated shortest distances from the source node.
    return distances


print(get_shortest_path(
    {
        0: [1, 3],
        1: [0, 2, 3],
        2: [1, 6],
        3: [0, 4],
        4: [3, 5],
        5: [4, 6],
        6: [2, 5, 7, 8],
        7: [6, 8],
        8: [6, 7]
    },
    0
))

print(
    get_shortest_path(
        {
            0: [3],
            1: [3],
            2: [],
            3: [0, 1]
        },
        3
    )
)