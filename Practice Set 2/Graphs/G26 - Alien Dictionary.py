class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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
            node.next = self.head
            self.head = node
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
    _alphabets = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def _construct_graph(graph, orders):
        for i in range(len(orders) - 1):
            s1, s2 = orders[i], orders[i + 1]
            n1, n2 = len(s1), len(s2)
            p, q = 0, 0
            while p < n1:
                if s1[p] != s2[q]:
                    graph[s1[p]].append(s2[q])
                    break
                p += 1
                q += 1

    @staticmethod
    def _get_toposort(graph):
        visited = {i: False for i in graph}


    @staticmethod
    def get_alien_dictionary(orders, k):
        graph = {Solution._alphabets[i]: [] for i in range(k)}
        Solution._construct_graph(graph, orders)
        topo_sort = Solution._get_toposort(graph)