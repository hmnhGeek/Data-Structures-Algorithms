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


class Graph:
    @staticmethod
    def _get_indegrees(graph, indegrees):
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1

    @staticmethod
    def _topological_sort(graph):
        indegrees = {i: 0 for i in graph}
        Graph._get_indegrees(graph, indegrees)
        queue = Queue()
        topo_sort = []

        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)

        while not queue.is_empty():
            current_node = queue.pop()
            topo_sort.append(current_node)
            for adj_node in graph[current_node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        return topo_sort

    @staticmethod
    def _get_reversed_graph(graph):
        reversed = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed[adj_node].append(node)
        return reversed

    @staticmethod
    def get_eventual_safe_nodes(graph):
        reversed_graph = Graph._get_reversed_graph(graph)
        topo_sort = Graph._topological_sort(reversed_graph)
        return topo_sort

print(
    Graph.get_eventual_safe_nodes(
        {
            0: [1, 2],
            1: [3],
            2: [5],
            3: [0],
            4: [5],
            5: [],
            6: [],
            7: [1]
        }
    )
)