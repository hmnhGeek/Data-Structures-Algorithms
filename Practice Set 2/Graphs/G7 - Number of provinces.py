class Solution:
    @staticmethod
    def _dfs(graph, node, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited)

    @staticmethod
    def _get_graph(mtx, graph):
        n = len(mtx)
        for i in range(n):
            for j in range(n):
                if i != j and mtx[i][j] == 1:
                    graph[i].append(j)

    @staticmethod
    def num_provinces(mtx):
        graph = {i: [] for i in range(len(mtx))}
        Solution._get_graph(mtx, graph)
        visited = {i: False for i in graph}
        num_components = 0
        for node in graph:
            if not visited[node]:
                num_components += 1
                Solution._dfs(graph, node, visited)
        return num_components


print(
    Solution.num_provinces(
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(
    Solution.num_provinces(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(Solution.num_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
