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

    def enqueue(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return
        item = self.head.data
        self.head = self.head.next
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def is_graph_tree(edges, n, m):
        if m != n - 1:
            return False
        graph = Solution._get_graph(edges)
        queue = Queue()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                if Solution._has_cycle(graph, node, visited, queue):
                    return False
        return True

    @staticmethod
    def _get_graph(edges):
        graph = {}
        for edge in edges:
            node, adj_node = edge
            graph[node] = []
            graph[adj_node] = []
        for edge in edges:
            node, adj_node = edge
            graph[node].append(adj_node)
            graph[adj_node].append(node)
        return graph

    @staticmethod
    def _has_cycle(graph, start_node, visited, queue):
        visited[start_node] = True
        queue.enqueue((start_node, None))
        while not queue.is_empty():
            node, parent = queue.dequeue()
            for adj_node in graph[node]:
                if adj_node == parent:
                    continue
                if visited[adj_node]:
                    return True
                queue.enqueue((adj_node, node))
                visited[adj_node] = True
        return False


if __name__ == "__main__":
    print(Solution.is_graph_tree([
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 3]
    ], 4, 4))

    print(Solution.is_graph_tree([
        [0, 1],
        [1, 2],
        [2, 3]
    ], 4, 3))

    print(Solution.is_graph_tree([
        [0, 1],
        [0, 2],
        [0, 3],
        [4, 1]
    ], 5, 4))

    print(Solution.is_graph_tree([
        [0, 1],
        [1, 2],
        [1, 4],
        [2, 3],
        [1, 3]
    ], 5, 5))

