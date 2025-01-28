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
    def _get_graph(courses):
        graph = {}
        for course in courses:
            graph[course[0]] = []
            graph[course[1]] = []
        indegrees = {i: 0 for i in graph}
        for course in courses:
            nxt, prev = course
            graph[prev].append(nxt)
            indegrees[nxt] += 1
        return graph, indegrees

    @staticmethod
    def _get_topological_sort(graph, indegrees):
        queue = Queue()
        topo = []
        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)
        while not queue.is_empty():
            node = queue.pop()
            topo.append(node)
            for adj_node in graph[node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        return topo

    @staticmethod
    def course_schedule(courses):
        """
            Overall time complexity is O(V + E) and space complexity is O(V).
        """

        # form the graph and get the indegrees from the courses list in O(V + E) time and O(V) space.
        graph, indegrees = Solution._get_graph(courses)

        # get the topological sort (if any) in O(V + E) time and O(V) space.
        topo_sort = Solution._get_topological_sort(graph, indegrees)

        # return the course schedule if toposort is possible.
        if len(topo_sort) == len(graph):
            return topo_sort
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

print(Solution.course_schedule([[0, 1], [1, 0]]))
print(Solution.course_schedule([[1, 2], [2, 3], [2, 4], [3, 4], [4, 3]]))