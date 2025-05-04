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
    def _bfs(graph, start_node, visited):
        # edge case
        if start_node not in graph:
            return

        # initialize a queue and push the start node into it and mark it as visited.
        queue = Queue()
        queue.push(start_node)
        visited[start_node] = True

        # standard BFS...
        while not queue.is_empty():
            # pop the node and print it.
            node = queue.pop()
            print(node, end=" ")

            # push the next non-visited adjacent node into queue.
            for adj_node in graph[node]:
                if not visited[adj_node]:
                    queue.push(adj_node)
                    visited[adj_node] = True

    @staticmethod
    def bfs(graph):
        # create a visited array
        visited = {i: False for i in graph}

        # traverse for each component in the graph
        for node in graph:
            if not visited[node]:
                # start bfs from the first node of the component.
                Solution._bfs(graph, node, visited)
        print()


graph1 = {
    1: [2, 6],
    2: [1, 3, 4],
    3: [2],
    4: [2, 5],
    5: [4, 7],
    6: [1, 7, 8],
    7: [5, 6],
    8: [6]
}
Solution.bfs(graph1)

graph2 = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0],
    4: [2]
}
Solution.bfs(graph2)

graph3 = {
    0: [1, 2],
    1: [0, 2],
    2: [1, 0, 3, 4],
    3: [2],
    4: [2]
}
Solution.bfs(graph3)
