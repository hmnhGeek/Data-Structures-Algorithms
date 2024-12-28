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
    def bfs(graph, source):
        if source not in graph:
            return
        visited = {i: False for i in graph}
        queue = Queue()
        queue.push(source)
        while not queue.is_empty():
            node = queue.pop()
            if not visited[node]:
                print(node, end=" ")
            visited[node] = True
            for adj_node in graph[node]:
                if not visited[adj_node]:
                    queue.push(adj_node)
        print()


Solution.bfs(
    {
        1: [2, 6],
        2: [1, 3, 4],
        3: [2],
        4: [2, 5],
        5: [4, 7],
        6: [1, 7, 8],
        7: [5, 6],
        8: [6]
    },
    1
)

Solution.bfs(
    {
        0: [1, 2, 3],
        1: [0],
        2: [0, 4],
        3: [0],
        4: [2]
    },
    0
)

Solution.bfs(
    {
        0: [1, 2],
        1: [0, 2],
        2: [1, 0, 3, 4],
        3: [2],
        4: [2]
    },
    0
)
