# Problem link - https://www.geeksforgeeks.org/problems/course-schedule/1
# Solution - https://www.youtube.com/watch?v=WAOfKpxYHR8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=24


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
    def course_schedule(mtx):
        """
            Overall time complexity is O(V + E) and space complexity is O(V).
        """
        graph = Solution._get_graph(mtx)
        indegrees = Solution._get_indegrees(graph)
        queue = Queue()
        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)
        result = []
        while not queue.is_empty():
            node = queue.pop()
            result.append(node)
            for adj_node in graph[node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        if len(graph) == len(result):
            return result
        return None

    @staticmethod
    def _get_graph(mtx):
        n = len(mtx)
        graph = {}
        for i in range(n):
            graph[mtx[i][0]] = []
            graph[mtx[i][1]] = []
        for i in range(n):
            graph[mtx[i][1]].append(mtx[i][0])
        return graph

    @staticmethod
    def _get_indegrees(graph):
        indegrees = {i: 0 for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1
        return indegrees


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
