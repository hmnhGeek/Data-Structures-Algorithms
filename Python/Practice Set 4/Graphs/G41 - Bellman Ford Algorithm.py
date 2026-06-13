class Solution:
    @staticmethod
    def get_shortest_distances(graph, source):
        if source not in graph:
            return
        edges = Solution._get_edges(graph)
        distances = {node: 1e6 for node in graph}
        distances[source] = 0
        n = len(graph)
        for i in range(n - 1):
            for edge in edges:
                u, v, w = edge
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
        for edge in edges:
            u, v, w = edge
            if distances[u] + w < distances[v]:
                return
        return distances

    @staticmethod
    def _get_edges(graph):
        edges = []
        for node in graph:
            for adj_node, wt in graph[node]:
                edges.append((node, adj_node, wt))
        return edges


print(
    Solution.get_shortest_distances(
        {
            0: [[1, 9]],
            1: []
        },
        0
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 5]],
            1: [[0, 3], [2, -1]],
            2: [[0, 1]]
        },
        2
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 5]],
            1: [[2, 1], [3, 2]],
            2: [[4, 1]],
            3: [],
            4: [[3, -1]]
        },
        0
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 4]],
            1: [[2, -6]],
            2: [[3, 5]],
            3: [[1, -2]]
        },
        0
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 5]],
            1: [[2, -2], [5, -3]],
            2: [[4, 3]],
            3: [[2, 6], [4, -2]],
            4: [],
            5: [[3, 1]]
        },
        0
    )
)
