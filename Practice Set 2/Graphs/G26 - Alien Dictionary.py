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
    def _dfs(graph, node, visited, stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited, stack)
        stack.push(node)

    @staticmethod
    def _get_toposort(graph):
        visited = {i: False for i in graph}
        stack = Stack()
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, visited, stack)

        if stack.length != len(graph):
            print(False)
        else:
            while not stack.is_empty():
                print(stack.pop(), end=" ")
            print()

    @staticmethod
    def get_alien_dictionary(orders, k):
        """
            Overall time complexity is O(k + E) and space complexity is O(k).
        """

        graph = {Solution._alphabets[i]: [] for i in range(k)}
        Solution._construct_graph(graph, orders)
        Solution._get_toposort(graph)


Solution.get_alien_dictionary(["baa","abcd","abca","cab","cad"], 4)
Solution.get_alien_dictionary(["caa","aaa","aab"], 3)
Solution.get_alien_dictionary(["dhhid" "dahi" "cedg" "fg" "gdah" "i" "gbdei" "hbgf" "e" "ddde"], 9)
Solution.get_alien_dictionary(["abc","bat","ade"], 5)
Solution.get_alien_dictionary(["a", "aa", "aaa"], 1)
