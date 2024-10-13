# Problem link - https://www.geeksforgeeks.org/problems/bipartite-graph/1
# Solution - https://www.youtube.com/watch?v=-vu34sct1g8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=17


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
    def _invert_color(color):
        if color == 0:
            return 1
        return 0

    @staticmethod
    def is_bipartite(graph, source):
        if source not in graph:
            return False
        queue = Queue()
        node_colors = {i: None for i in graph}
        node_colors[source] = 0
        queue.push(source)

        while not queue.is_empty():
            node = queue.pop()
            node_color = node_colors[node]
            for adj_node in graph[node]:
                if node_colors[adj_node] is None:
                    node_colors[adj_node] = Graph._invert_color(node_color)
                    queue.push(adj_node)
                else:
                    if node_colors[adj_node] == node_color:
                        return False
        return True


class Solution:
    @staticmethod
    def is_bipartite(graph, source):
        return Graph.is_bipartite(graph, source)


print(
    Solution.is_bipartite(
        {
            0: [1],
            1: [0, 2],
            2: [1]
        },
        1
    )
)

print(
    Solution.is_bipartite(
        {
            0: [2, 3],
            1: [3],
            2: [0, 3],
            3: [0, 1, 2]
        },
        2
    )
)