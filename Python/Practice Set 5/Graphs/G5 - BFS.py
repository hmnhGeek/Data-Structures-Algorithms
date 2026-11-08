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
        self.head = self.head.next
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def bfs(graph):
        visited = {i: False for i in graph}
        queue = Queue()
        result = []
        for node in graph:
            if not visited[node]:
                Solution._bfs(node, visited, result, queue, graph)
        print(result)

    @staticmethod
    def _bfs(node, visited, result, queue, graph):
        visited[node] = True
        queue.push(node)
        while not queue.is_empty():
            curr = queue.pop()
            result.append(curr)
            for adj_node in graph[curr]:
                if not visited[adj_node]:
                    visited[adj_node] = True
                    queue.push(adj_node)


graph1 = {
    1: [2, 6],
    2: [1, 3, 4],
    3: [2],
    4: [2, 5],
    5: [4, 7],
    6: [1, 7, 8],
    7: [5, 6],
    8: [6]
}
Solution.bfs(graph1)

graph2 = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0],
    4: [2]
}
Solution.bfs(graph2)

graph3 = {
    0: [1, 2],
    1: [0, 2],
    2: [1, 0, 3, 4],
    3: [2],
    4: [2]
}
Solution.bfs(graph3)
