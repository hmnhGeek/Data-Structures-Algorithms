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
    def get_graph_from_words(strings):
        graph = {}
        for string in strings:
            for character in string:
                graph[character] = []
        n = len(strings)
        for i in range(n - 1):
            first_string, second_string = strings[i], strings[i + 1]
            min_length = min(len(first_string), len(second_string))
            j = 0
            while j < min_length:
                if first_string[j] != second_string[j]:
                    graph[first_string[j]].append(second_string[j])
                    break
                j += 1
        return graph

    @staticmethod
    def get_topological_sort(graph):
        queue = Queue()
        result = []
        indegrees = Solution.get_indegrees(graph)
        for node in indegrees:
            if indegrees[node] == 0:
                queue.push(node)
        while not queue.is_empty():
            node = queue.pop()
            result.append(node)
            for adj_node in graph[node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        return result

    @staticmethod
    def get_indegrees(graph):
        indegrees = {i: 0 for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1
        return indegrees