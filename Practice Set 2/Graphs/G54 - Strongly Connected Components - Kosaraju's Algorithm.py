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
    def _reverse_graph(graph):
        reversed_graph = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed_graph[adj_node].append(node)
        return reversed_graph

    @staticmethod
    def _dfs(graph, visited, node, stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, visited, adj_node, stack)
        stack.push(node)

    @staticmethod
    def _get_main_stack(graph):
        stack = Stack()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, visited, node, stack)
        return stack

    @staticmethod
    def _get_strongly_connected_components(reversed_graph, main_stack):
        result = []
        visited = {i: False for i in reversed_graph}
        while not main_stack.is_empty():
            node = main_stack.pop()
            if not visited[node]:
                traversal_stack = Stack()
                scc = []
                Solution._dfs(reversed_graph, visited, node, traversal_stack)
                while not traversal_stack.is_empty():
                    scc.append(traversal_stack.pop())
                result.append(scc)
        return result

    @staticmethod
    def get_strongly_connected_components(graph):
        reversed_graph = Solution._reverse_graph(graph)
        main_stack = Solution._get_main_stack(graph)
        return Solution._get_strongly_connected_components(reversed_graph, main_stack)


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