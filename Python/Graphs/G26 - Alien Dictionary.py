# Problem link - https://www.geeksforgeeks.org/problems/alien-dictionary/1
# Solution - https://www.youtube.com/watch?v=U3N_je7tWAs&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=26


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


class Graph:
    @staticmethod
    def _dfs(graph, node, visited, stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Graph._dfs(graph, adj_node, visited, stack)
        stack.push(node)

    @staticmethod
    def get_topological_sort(graph):
        visited = {i: False for i in graph}
        topo_sort = []
        stack = Stack()
        for node in graph:
            if not visited[node]:
                Graph._dfs(graph, node, visited, stack)
        while not stack.is_empty():
            topo_sort.append(stack.pop())
        return topo_sort


class Solution:
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def _add_edge(graph, first, second):
        i, j = 0, 0
        while i < len(first) and j < len(second):
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                graph[first[i]].append(second[j])
                return

    @staticmethod
    def _get_graph(words, k):
        # This will take O(k) space.
        graph = {i: [] for i in Solution.alphabets[:k]}

        # connect the edges between the graphs in O(n*k) time
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            Solution._add_edge(graph, first, second)
        return graph

    @staticmethod
    def get_alien_dictionary(words, k):
        # form a DAG from a given order of words with `k` characters from the English alphabets.
        graph = Solution._get_graph(words, k)
        # get the topological sort in O(k + E) time and O(k) space.
        topo_sort = Graph.get_topological_sort(graph)
        # print the order of alphabets
        print(topo_sort)


Solution.get_alien_dictionary(
    [
        "baa",
        "abcd",
        "abca",
        "cab",
        "cad"
    ],
    4
)

Solution.get_alien_dictionary(
    ["caa", "aaa", "aab"], 3
)

Solution.get_alien_dictionary(
    ["a", "aa", "aaa"], 1
)


