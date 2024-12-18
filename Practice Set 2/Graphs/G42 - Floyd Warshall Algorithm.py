class Solution:
    @staticmethod
    def _get_adj_mtx(graph):
        n = len(graph)
        mtx = [[1e6 for _ in range(n)] for _ in range(n)]
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                mtx[node][adj_node] = wt
        for i in range(n):
            mtx[i][i] = 0
        return mtx

    @staticmethod
    def floyd_warshall(graph):
        adj_mtx = Solution._get_adj_mtx(graph)
        n = len(graph)
        for via_node in graph:
            for u in range(n):
                for v in range(n):
                    adj_mtx[u][v] = min(adj_mtx[u][v], adj_mtx[u][via_node] + adj_mtx[via_node][v])
        for i in range(n):
            if adj_mtx[i][i] < 0:
                return "Negative cycle detected!"
        for i in range(n):
            for j in range(n):
                print(adj_mtx[i][j] if adj_mtx[i][j] != 1e6 else -1, end=" ")
            print()
        print()


Solution.floyd_warshall(
    {
        0: [[1, 2]],
        1: [[0, 1], [2, 3]],
        2: [],
        3: [[0, 3], [1, 5], [2, 4]]
    }
)

Solution.floyd_warshall(
    {
        0: [[1, 1], [2, 43]],
        1: [[0, 1], [2, 6]],
        2: []
    }
)

Solution.floyd_warshall(
    {
        0: [[1, 25]],
        1: []
    }
)

Solution.floyd_warshall(
    {
        0: [[1, 4], [3, 5]],
        1: [[2, 1], [4, 6]],
        2: [[0, 2], [3, 3]],
        3: [[2, 1], [4, 2]],
        4: [[0, 1], [3, 4]]
    }
)