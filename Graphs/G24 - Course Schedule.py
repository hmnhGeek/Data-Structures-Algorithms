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
    def _dfs(graph, node, visited, path_visited, stack):
        visited[node] = True
        path_visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                has_cycle = Graph._dfs(graph, adj_node, visited, path_visited, stack)
                if has_cycle:
                    return True
            elif path_visited[adj_node]:
                return True
        path_visited[node] = False
        stack.push(node)
        return False

    @staticmethod
    def get_topological_sort(edges):
        graph = Graph._from_edge_list(edges)
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}
        stack = Stack()

        for node in visited:
            if not visited[node]:
                if Graph._dfs(graph, node, visited, path_visited, stack):
                    break

        if stack.length < len(graph):
            print(-1)

        while not stack.is_empty():
            print(stack.pop(), end=" ")
        print()

    @staticmethod
    def _from_edge_list(edges):
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
        return graph


Graph.get_topological_sort([[0, 1]])
Graph.get_topological_sort([[0, 1], [0, 2], [1, 3], [2, 3]])
Graph.get_topological_sort([[0, 1], [1, 0]])