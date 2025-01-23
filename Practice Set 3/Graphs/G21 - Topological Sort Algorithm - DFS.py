class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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
            node.next = self.head
            self.head = node
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
    def _dfs(graph, node, visited, stack: Stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited, stack)
        stack.push(node)

    @staticmethod
    def topological_sort(graph):
        stack = Stack()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, visited, stack)
        while not stack.is_empty():
            print(stack.pop(), end=" ")
        print()



Solution.topological_sort(
    {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2]
    }
)

Solution.topological_sort(
    {
        0: [],
        1: [0],
        2: [0],
        3: [0]
    }
)

Solution.topological_sort(
    {
        0: [],
        1: [3],
        2: [3],
        3: [],
        4: [0, 1],
        5: [0, 2]
    }
)
