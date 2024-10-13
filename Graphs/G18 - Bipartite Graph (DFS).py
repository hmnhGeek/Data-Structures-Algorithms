# Problem link - https://www.geeksforgeeks.org/problems/bipartite-graph/1
# Solution - https://www.youtube.com/watch?v=KG5YFfR0j8A&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=18


class Graph:
    @staticmethod
    def _invert(color):
        if color == 1:
            return 0
        return 1

    @staticmethod
    def _dfs(graph, node, node_colors, color):
        node_colors[node] = color
        for adj_node in graph[node]:
            if node_colors[adj_node] is None:
                if not Graph._dfs(graph, adj_node, node_colors, Graph._invert(color)):
                    return False
            else:
                if node_colors[adj_node] == color:
                    return False
        return True

    @staticmethod
    def is_bipartite(graph):
        node_colors = {i: None for i in graph}
        start_node = list(node_colors.keys())[0]
        return Graph._dfs(graph, start_node, node_colors, 0)


class Solution:
    @staticmethod
    def is_bipartite(graph):
        return Graph.is_bipartite(graph)


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
            1: [3],
            2: [0, 3],
            3: [0, 1, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 5],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [0, 4]
        }
    )
)