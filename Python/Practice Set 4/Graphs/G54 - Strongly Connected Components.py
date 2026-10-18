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
        self.head = self.head.next
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def get_strongly_connected_components(graph):
        stack = Solution._get_sorted_order(graph)
        reversed_graph = Solution._get_reversed_graph(graph)
        return Solution._get_scc(reversed_graph, stack)

    @staticmethod
    def _get_sorted_order(graph):
        stack = Stack()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, stack, visited)
        return stack

    @staticmethod
    def _dfs(graph, node, stack, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, stack, visited)
        stack.push(node)

    @staticmethod
    def _get_reversed_graph(graph):
        reversed = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed[adj_node].append(node)
        return reversed

    @staticmethod
    def _get_scc(reversed_graph, stack):
        visited = {i: False for i in reversed_graph}
        strongly_connected_components = []
        while not stack.is_empty():
            node = stack.pop()
            if not visited[node]:
                component = []
                Solution._dfs2(reversed_graph, node, visited, component)
                strongly_connected_components.append(component)
        return strongly_connected_components

    @staticmethod
    def _dfs2(graph, node, visited, component):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs2(graph, adj_node, visited, component)
        component.append(node)


print(
    Solution.get_strongly_connected_components(
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
)

print(
    Solution.get_strongly_connected_components(
        {
            0: [2, 3],
            1: [0],
            2: [1],
            3: [4],
            4: []
        }
    )
)

print(
    Solution.get_strongly_connected_components(
        {
            0: [1],
            1: [2],
            2: [0]
        }
    )
)

print(
    Solution.get_strongly_connected_components(
        {
            1: [2],
            2: [3, 4],
            3: [4, 6],
            4: [1, 5],
            5: [6],
            6: [7],
            7: [5]
        }
    )
)
