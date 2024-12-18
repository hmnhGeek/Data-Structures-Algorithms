class Solution:
    @staticmethod
    def _get_edges(graph):
        edges = []
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                edges.append([node, adj_node, wt])
        return edges

    @staticmethod
    def get_shortest_distances(graph, source):
        if source not in graph:
            return
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        v = len(graph)
        edges = Solution._get_edges(graph)
        for i in range(v - 1):
            for edge in edges:
                u, v, w = edge
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
        for edge in edges:
            u, v, w = edge
            if distances[u] + w < distances[v]:
                return "Negative Cycle Detected!"
        return list(distances.values())


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