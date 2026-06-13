class Solution:
    @staticmethod
    def floyd_warshall(graph):
        distances, n = Solution._get_distances(graph)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
        for i in range(n):
            if distances[i][i] < 0:
                return -1
        print(distances)

    @staticmethod
    def _get_distances(graph):
        n = len(graph)
        mtx = [[1e6 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            mtx[i][i] = 0
        for node in graph:
            for adj_node, wt in graph[node]:
                mtx[node][adj_node] = wt
        return mtx, n


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
