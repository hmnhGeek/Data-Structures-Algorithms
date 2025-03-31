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
        return None if self.is_empty() else self.head.data


def reverse(graph):
    # takes O(V) space
    result = {i: [] for i in graph}
    # takes O(V) space
    indegrees = {i: 0 for i in graph}

    # consumes O(V + E) time.
    for node in graph:
        for adj_node in graph[node]:
            indegrees[node] += 1
            result[adj_node].append(node)

    return result, indegrees


def detect_safe_nodes(graph):
    '''Overall time complexity is O(V + E) and space complexity is O(V + E)'''

    # time complexity is O(V + E) and space is O(V)
    reversed_graph, indegrees = reverse(graph)

    # it will take O(V) space
    result = []

    # apply topological sort algorithm on reversed graph to check safe nodes
    # we will be using Kahn's algorithm to do this. It will also take O(V) space.
    queue = Queue()

    # push all the starting nodes into the queue.
    for node in [k for k, v in indegrees.items() if v == 0]:
        queue.enqueue(node)

    # this while loop will run for V times because all nodes will once go into the
    # queue in the worst case. Overall time complexity is O(V + E) time.
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node)

        for adj_node in reversed_graph[node]:
            indegrees[adj_node] -= 1
            if indegrees[adj_node] == 0:
                queue.enqueue(adj_node)

    # optional to sort the result, it will add time complexity of O(V*log(V))
    result.sort()
    return result

print(
    detect_safe_nodes(
        {
        0: [1],
        1: [2],
        2: [3, 4],
        3: [4, 5],
        4: [6],
        5: [6],
        6: [7],
        7: [],
        8: [1, 9],
        9: [10],
        10: [8],
        11: [9]
    }
    )
)

print(
    detect_safe_nodes(
        {
            0: [1, 2],
            1: [2, 3],
            2: [5],
            3: [0],
            4: [5],
            5: [],
            6: []
        }
    )
)

print(
    detect_safe_nodes(
        {
            0: [1],
            1: [2],
            2: [0, 3],
            3: []
        }
    )
)