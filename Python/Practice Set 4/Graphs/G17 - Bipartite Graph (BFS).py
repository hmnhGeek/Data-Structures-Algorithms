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
        node = self.head
        item = self.head.data
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def is_bipartite(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # create a node colors dictionary which will act as visited also. This will take O(V) space.
        node_colors = {i: None for i in graph}
        for node in graph:
            if node_colors[node] is None:
                # This is a component and if it is not bipartite, simply return False.
                if not Solution._bfs_bipartite_check(node, node_colors, graph):
                    return False

        # if all the components are bipartite, return True.
        return True

    @staticmethod
    def _bfs_bipartite_check(start_node, node_colors, graph):
        # For a given component of the original graph, initialize a queue to perform BFS.
        queue = Queue()

        # push the start node with color 0.
        queue.push((start_node, 0))

        # typical BFS...
        while not queue.is_empty():
            # pop the current node with its color and color it.
            node, color = queue.pop()
            node_colors[node] = color

            # loop in the neighbours
            for adj_node in graph[node]:
                # if the adjacent node is colored and the color is same as of this node's color,
                # the graph is not bipartite, therefore, return False.
                if node_colors[adj_node] is not None:
                    if node_colors[adj_node] == color:
                        return False
                else:
                    # if the adj_node is not colored, push it to queue with toggled color value.
                    queue.push((adj_node, 0 if color == 1 else 1))

        # return True if queue got empty as it is a bipartite graph.
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
