# Problem link - https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
# Solution - https://www.youtube.com/watch?v=-tgVpUgsQ5k&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=5


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
    def bfs(graph, source):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # edge case
        if source not in graph:
            return

        # take a visited array to track node visits
        visited = {i: False for i in graph}

        # push the source node into the queue.
        queue = Queue()
        queue.push(source)

        # typical BFS...
        while not queue.is_empty():
            # pop the current node and print it if it is not visited.
            node = queue.pop()
            if not visited[node]:
                print(node, end=" ")

            # mark the current node as visited.
            visited[node] = True

            # loop on the adjacent nodes of this node
            for adj_node in graph[node]:
                # if they are not yet visited, push them into the queue.
                if not visited[adj_node]:
                    queue.push(adj_node)
        print()


Solution.bfs(
    {
        1: [2, 6],
        2: [1, 3, 4],
        3: [2],
        4: [2, 5],
        5: [4, 7],
        6: [1, 7, 8],
        7: [5, 6],
        8: [6]
    },
    1
)

Solution.bfs(
    {
        0: [1, 2, 3],
        1: [0],
        2: [0, 4],
        3: [0],
        4: [2]
    },
    0
)

Solution.bfs(
    {
        0: [1, 2],
        1: [0, 2],
        2: [1, 0, 3, 4],
        3: [2],
        4: [2]
    },
    0
)
