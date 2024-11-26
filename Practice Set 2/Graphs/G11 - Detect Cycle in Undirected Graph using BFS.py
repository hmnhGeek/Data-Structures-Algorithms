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
    def _detect_cycle(graph, node, visited):
        queue = Queue()
        queue.push(node)
        while not queue.is_empty():
            node = queue.pop()
            if visited[node]:
                return True
            visited[node] = True
            for adj_node in graph[node]:
                if not visited[adj_node]:
                    queue.push(adj_node)
        return False

    @staticmethod
    def detect_cycle(graph):
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                component_has_cycle = Solution._detect_cycle(graph, node, visited)
                if component_has_cycle:
                    return True
        return False


print(
    Solution.detect_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 6],
            4: [3],
            5: [2, 7],
            6: [3, 7],
            7: [5, 6]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 6],
            4: [3],
            5: [2, 7],
            6: [3],
            7: [5]
        }
    )
)