class Solution:
    @staticmethod
    def _get_adj_mtx(edges, n):
        adj_mtx = [[1e6 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            adj_mtx[i][i] = 0
        for edge in edges:
            src, dst, wt = edge
            adj_mtx[src][dst] = wt
            adj_mtx[dst][src] = wt
        return adj_mtx

    @staticmethod
    def find_city(edges, threshold, n):
        adj_mtx = Solution._get_adj_mtx(edges, n)
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    adj_mtx[u][v] = min(adj_mtx[u][v], adj_mtx[u][k] + adj_mtx[k][v])
        for i in range(n):
            if adj_mtx[i][i] < 0:
                return -1
        num_cities, city = n, -1
        for i in range(n):
            count = 0
            for j in range(n):
                if adj_mtx[i][j] <= threshold:
                    count += 1
            if num_cities >= count:
                num_cities = count
                city = i
        return city


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
