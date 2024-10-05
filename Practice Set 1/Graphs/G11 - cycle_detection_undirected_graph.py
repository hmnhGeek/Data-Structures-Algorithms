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


class Graph:
    @staticmethod
    def _has_cycle(graph, start_node, visited):
        queue = Queue()
        queue.push((start_node, None))
        while not queue.is_empty():
            node, parent = queue.pop()
            if visited[node]:
                return True
            visited[node] = True
            for adj_node in graph[node]:
                if not visited[adj_node]:
                    queue.push((adj_node, node))
        return False

    @staticmethod
    def has_cycle(graph):
        visited = {i: False for i in graph}
        for node in visited:
            if not visited[node]:
                if Graph._has_cycle(graph, node, visited):
                    return True
        return False


print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [5],
            3: [1, 4, 6],
            4: [3],
            5: [7],
            6: [3, 7],
            7: [5, 6]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [],
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
    )
)