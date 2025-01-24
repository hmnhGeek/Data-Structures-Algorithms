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
    def has_cycle(graph):
        indegrees = {i: 0 for i in graph}
        Solution._update_indegrees(graph, indegrees)
        queue = Queue()
        for node in graph:
            if indegrees[node] == 0:
                queue.push(node)
        count = 0
        while not queue.is_empty():
            node = queue.pop()
            count += 1
            for adj_node in graph[node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        if count == len(graph):
            return False
        return True

    @staticmethod
    def _update_indegrees(graph, indegrees):
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1


print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2],
            2: [3],
            3: [3]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2],
            2: []
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [3],
            3: []
        }
    )
)
