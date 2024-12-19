class Solution:
    @staticmethod
    def _get_adj_mtx(edges, n):
        mtx = [[1e6 for _ in range(n)] for _ in range(n)]
        for edge in edges:
            src, dst, wt = edge
            mtx[src][dst] = wt
            mtx[dst][src] = wt
        for i in range(n):
            mtx[i][i] = 0
        return mtx

    @staticmethod
    def _apply_floyd_warshall(mtx, n):
        for via in range(n):
            for u in range(n):
                for v in range(n):
                    if mtx[u][v] > mtx[u][via] + mtx[via][v]:
                        mtx[u][v] = mtx[u][via] + mtx[via][v]
        for i in range(n):
            if mtx[i][i] < 0:
                raise Exception("Negative cycle detected!")

    @staticmethod
    def find_city(edges, threshold, n):
        adj_mtx = Solution._get_adj_mtx(edges, n)
        Solution._apply_floyd_warshall(adj_mtx, n)
        min_cities_reachable = n
        from_city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if adj_mtx[i][j] <= threshold:
                    count += 1
            if count <= min_cities_reachable:
                from_city = i
                min_cities_reachable = count
        return from_city


print(
    Solution.find_city(
        [[0, 1, 3],
         [1, 2, 1],
         [1, 3, 4],
         [2, 3, 1]],
        4,
        4
    )
)

print(
    Solution.find_city(
        [[0, 1, 2],
         [0, 4, 8],
         [1, 2, 3],
         [1, 4, 2],
         [2, 3, 1],
         [3, 4, 1]],
        2,
        5
    )
)
