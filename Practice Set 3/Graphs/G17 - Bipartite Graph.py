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
    def _bfs(graph, node, color, colors):
        queue = Queue()
        queue.push((node, color))

        # standard BFS
        while not queue.is_empty():
            curr, col = queue.pop()

            # color the current popped node.
            colors[curr] = col

            # loop on the adjacent nodes
            for adj_node in graph[curr]:
                # if the adjacent node is not colored, push the adjacent node with toggled color in to the queue.
                if colors[adj_node] is None:
                    queue.push((adj_node, 0 if col == 1 else 1))

                # if the adjacent node is colored with same color as this node, return False, it's not a bipartite graph
                elif colors[adj_node] == col:
                    return False

        # else this component is bipartite
        return True

    @staticmethod
    def is_bipartite(graph):
        # create a dictionary to store the colors on the nodes
        colors = {i: None for i in graph}

        # loop on the nodes in the graph
        for node in graph:
            # if this node is not colored, initiate a BFS.
            if colors[node] is None:
                # initiate with color 0.
                if not Solution._bfs(graph, node, 0, colors):
                    # if it is found that this component is not bipartite, return False.
                    return False

        # else return True
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

