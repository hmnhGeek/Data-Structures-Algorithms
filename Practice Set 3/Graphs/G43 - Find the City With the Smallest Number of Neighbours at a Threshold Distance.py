# Problem link - https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1
# Solution - https://www.youtube.com/watch?v=PwMVNSJ5SLI&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=43


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
        """
            Time complexity is O(V^3) and space complexity is O(V^2).
        """

        # in O(V + E) time and O(V^2) space, get the adjacency matrix.
        adj_mtx = Solution._get_adj_mtx(edges, n)

        # apply Floyd Warshall in O(V^3) time.
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    adj_mtx[u][v] = min(adj_mtx[u][v], adj_mtx[u][k] + adj_mtx[k][v])

        # detect negative weight
        for i in range(n):
            if adj_mtx[i][i] < 0:
                return -1

        # find the city in O(V^2) time.
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
