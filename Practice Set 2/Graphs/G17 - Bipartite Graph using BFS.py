# Problem link - https://leetcode.com/problems/is-graph-bipartite/description/
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


class Solution:
    @staticmethod
    def is_bipartite(graph, source_node):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # if the source is not present in graph, return
        if source_node not in graph:
            return

        # take O(V) space to store colors on the nodes.
        colors = {i: None for i in graph}

        # initialize a queue to perform BFS and color first node with True.
        queue = Queue()
        queue.push((source_node, True))

        # while queue is not empty
        while not queue.is_empty():
            # pop the node with its color.
            node, color = queue.pop()
            # if the popped node is already colored, but the color is opposite, it's not a bipartite graph.
            if colors[node] is not None and colors[node] == (not color):
                return False
            # color the node with popped color.
            colors[node] = color
            # loop in the adjacent nodes.
            for adj_node in graph[node]:
                # if the color of adjacent node is not colored, color it with opposite color.
                if colors[adj_node] is None:
                    queue.push((adj_node, not color))
        # return True, it's a bipartite graph.
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
        },
        1
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
        },
        3
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1],
            1: [0, 2],
            2: [1]
        },
        2
    )
)

print(
    Solution.is_bipartite(
        {
            0: [2, 3],
            1: [2],
            2: [0, 1, 3],
            3: [0, 2]
        },
        0
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1, 3],
            3: [0, 2]
        },
        3
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        },
        1
    )
)