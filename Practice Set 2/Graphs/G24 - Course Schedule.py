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
    def _get_graph(p, g):
        for task in p:
            curr, prev = task
            if curr not in g:
                g[curr] = []
            if prev not in g:
                g[prev] = [curr]
            else:
                g[prev].append(curr)

    @staticmethod
    def _get_indeg(graph, indeg):
        for node in graph:
            for adj_node in graph[node]:
                indeg[adj_node] += 1

    @staticmethod
    def course_schedule(prereq):
        graph = {}
        queue = Queue()
        Solution._get_graph(prereq, graph)
        indeg = {i: 0 for i in graph}
        Solution._get_indeg(graph, indeg)
        topo = []
        for i in indeg:
            if indeg[i] == 0:
                queue.push(i)
        while not queue.is_empty():
            node = queue.pop()
            topo.append(node)
            for adj_node in graph[node]:
                indeg[adj_node] -= 1
                if indeg[adj_node] == 0:
                    queue.push(adj_node)
        if len(topo) == len(graph):
            return topo
        return []


print(
    Solution.course_schedule(
        [
            [1, 0]
        ]
    )
)

print(
    Solution.course_schedule(
        [
            [1, 0],
            [2, 0],
            [3, 1],
            [3, 2]
        ]
    )
)