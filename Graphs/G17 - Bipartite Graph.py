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
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # if the source node is not present in the graph, return False.
        if source not in graph:
            return False

        # initialize a blank queue for performing BFS.
        queue = Queue()

        # initialize node colors array from the graph.
        node_colors = {i: None for i in graph}

        # set the initial color of the source node and push the source node to queue.
        node_colors[source] = 0
        queue.push(source)

        # perform the BFS traversal.
        while not queue.is_empty():
            # pop the current node and store its color.
            node = queue.pop()
            node_color = node_colors[node]

            # loop on the adjacent nodes of the popped node.
            for adj_node in graph[node]:
                # if the adjacent node is not yet colored, then it's not visited.
                if node_colors[adj_node] is None:
                    # color it with the opposite color of node's color.
                    node_colors[adj_node] = Graph._invert_color(node_color)
                    # and push the adjacent node in to the queue.
                    queue.push(adj_node)
                else:
                    # else, if the node is colored and that too with the same color, then return false
                    # because a bipartite graph cannot have adjacent nodes with same color. However, if
                    # the colors are different, do nothing.
                    if node_colors[adj_node] == node_color:
                        return False
        # finally, if everything turned out to be fine, return True, it's a bipartite graph.
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

print(
    Solution.is_bipartite(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
        0
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 5],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [0, 4]
        },
        4
    )
)