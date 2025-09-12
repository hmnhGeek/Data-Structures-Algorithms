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
        node = self.head
        item = self.head.data
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def is_bipartite(graph):
        node_colors = {i: None for i in graph}
        for node in graph:
            if node_colors[node] is None:
                if not Solution._bfs_bipartite_check(node, node_colors, graph):
                    return False
        return True

    @staticmethod
    def _bfs_bipartite_check(start_node, node_colors, graph):
        queue = Queue()
        queue.push((start_node, 0))
        while not queue.is_empty():
            node, color = queue.pop()
            node_colors[node] = color
            for adj_node in graph[node]:
                if node_colors[adj_node] is not None:
                    if node_colors[adj_node] == color:
                        return False
                else:
                    queue.push((adj_node, 0 if color == 1 else 1))
        return True


print(
    Solution.is_bipartite(
        {
            1: [2],
            2: [3, 6],
            3: [2, 4],
            4: [3, 5, 7],
            5: [4, 6],
            6: [2, 5],
            7: [4, 8],
            8: [7]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            1: [2],
            2: [1, 3, 5],
            3: [2, 4],
            4: [3, 5, 6],
            5: [2, 4],
            6: [4]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1],
            1: [0, 2],
            2: [1]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [2, 3],
            1: [2],
            2: [0, 1, 3],
            3: [0, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1, 3],
            3: [0, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        }
    )
)
