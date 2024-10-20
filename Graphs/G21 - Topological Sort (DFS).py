# Problem link - https://www.geeksforgeeks.org/problems/topological-sort/1
# Solution - https://www.youtube.com/watch?v=5lZ0iJMrUMk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=21


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


class Graph:
    @staticmethod
    def _dfs(graph, node, visited, stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Graph._dfs(graph, adj_node, visited, stack)
        stack.push(node)

    @staticmethod
    def get_topological_sort(graph):
        visited = {i: False for i in graph}
        stack = Stack()
        for node in graph:
            if not visited[node]:
                Graph._dfs(graph, node, visited, stack)
        while not stack.is_empty():
            print(stack.pop(), end=" ")
        print()


Graph.get_topological_sort(
    {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2]
    }
)

Graph.get_topological_sort(
    {
        0: [],
        1: [0],
        2: [0],
        3: [0]
    }
)

Graph.get_topological_sort(
    {
        0: [],
        1: [3],
        2: [3],
        3: [],
        4: [0, 1],
        5: [0, 2]
    }
)
