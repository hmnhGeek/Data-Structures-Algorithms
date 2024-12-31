class Solution:
    @staticmethod
    def _dfs(graph, node, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited)

    @staticmethod
    def _get_graph(mtx):
        n = len(mtx)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j and mtx[i][j] == 1:
                    graph[i].append(j)
        return graph

    @staticmethod
    def find_num_provinces(mtx):
        graph = Solution._get_graph(mtx)
        visited = {i: False for i in graph}
        num_provinces = 0
        for node in graph:
            if not visited[node]:
                num_provinces += 1
                Solution._dfs(graph, node, visited)
        return num_provinces



print(
    Solution.find_num_provinces(
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(
    Solution.find_num_provinces(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(Solution.find_num_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))