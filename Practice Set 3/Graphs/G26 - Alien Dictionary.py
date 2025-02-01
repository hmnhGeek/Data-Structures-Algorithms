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

    def __str__(self):
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{curr.data}]"
        return result


class TopologicalSort:
    @staticmethod
    def _dfs(graph, node, visited, stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                TopologicalSort._dfs(graph, adj_node, visited, stack)
        stack.push(node)

    @staticmethod
    def get_topo_sort(graph):
        visited = {i: False for i in graph}
        stack = Stack()
        for node in graph:
            if not visited[node]:
                TopologicalSort._dfs(graph, node, visited, stack)
        return stack


class Solution:
    _alphabets = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def _get_graph(dictionary, k):
        graph = {i: [] for i in Solution._alphabets[:k]}
        for i in range(len(dictionary) - 1):
            s1, s2 = dictionary[i], dictionary[i + 1]
            length = min(len(s1), len(s2))
            for j in range(length):
                if s1[j] != s2[j]:
                    graph[s1[j]].append(s2[j])
                    break
        return graph

    @staticmethod
    def get_alien_dictionary(dictionary, k):
        graph = Solution._get_graph(dictionary, k)
        print(TopologicalSort.get_topo_sort(graph))


Solution.get_alien_dictionary(["baa","abcd","abca","cab","cad"], 4)
Solution.get_alien_dictionary(["caa","aaa","aab"], 3)
Solution.get_alien_dictionary(["dhhid" "dahi" "cedg" "fg" "gdah" "i" "gbdei" "hbgf" "e" "ddde"], 9)
Solution.get_alien_dictionary(["abc","bat","ade"], 5)
Solution.get_alien_dictionary(["a", "aa", "aaa"], 1)
