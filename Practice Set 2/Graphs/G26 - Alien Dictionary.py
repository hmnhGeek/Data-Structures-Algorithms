


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