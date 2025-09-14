class Solution:
    @staticmethod
    def _dfs(graph, node, parent, color, node_colors):
        node_colors[node] = color
        for adj_node in graph[node]:
            if adj_node == parent:
                continue
            if node_colors[adj_node] is None:
                if not Solution._dfs(graph, adj_node, node, 0 if color == 1 else 1, node_colors):
                    return False
            if node_colors[adj_node] == color:
                return False
        return True

    @staticmethod
    def is_bipartite(graph):
        node_colors = {i: None for i in graph}
        for node in graph:
            if node_colors[node] is None:
                if not Solution._dfs(graph, node, None, 0, node_colors):
                    return False
        return True


print(
    Solution.is_bipartite(
        {
            1: [2],
            2: [3, 6],
            3: [2, 4],
            4: [3, 5, 7],
            5: [4, 6],
            6: [2, 5],
            7: [4, 8],
            8: [7]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            1: [2],
            2: [1, 3, 5],
            3: [2, 4],
            4: [3, 5, 6],
            5: [2, 4],
            6: [4]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1],
            1: [0, 2],
            2: [1]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [2, 3],
            1: [2],
            2: [0, 1, 3],
            3: [0, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1, 3],
            3: [0, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        }
    )
)
