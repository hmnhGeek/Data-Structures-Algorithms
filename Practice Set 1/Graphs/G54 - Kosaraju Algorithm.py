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
    def _dfs(graph, visited, node, stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, visited, adj_node, stack)
        stack.push(node)

    @staticmethod
    def _reverse_graph(graph):
        reversed_graph = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed_graph[adj_node].append(node)
        return reversed_graph

    @staticmethod
    def kosaraju(graph):
        stack = Stack()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, visited, node, stack)

        reversed_graph = Solution._reverse_graph(graph)
        visited = {i: False for i in graph}
        temp_stack = Stack()
        strongly_connected_components = []
        while not stack.is_empty():
            node = stack.pop()
            if not visited[node]:
                Solution._dfs(reversed_graph, visited, node, temp_stack)
            component = []
            while not temp_stack.is_empty():
                component.append(temp_stack.pop())

            if len(component) > 0:
                strongly_connected_components.append(component)
        print(strongly_connected_components)


Solution.kosaraju(
    {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [5, 7],
        5: [6],
        6: [4, 7],
        7: []
    }
)