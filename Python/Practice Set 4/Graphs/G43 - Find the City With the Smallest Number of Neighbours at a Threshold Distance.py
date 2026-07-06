# Problem link - https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1
# Solution - https://www.youtube.com/watch?v=PwMVNSJ5SLI&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=43


class Solution:
    @staticmethod
    def find_city(edges, threshold, n):
        """
            Time complexity is O(V^3) and space complexity is O(V^2).
        """

        mtx = Solution._get_graph_matrix(edges, n)

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if mtx[i][via] + mtx[via][j] < mtx[i][j]:
                        mtx[i][j] = mtx[i][via] + mtx[via][j]

        for i in range(n):
            if mtx[i][i] < 0:
                return -1

        city = -1
        min_cities_reachable = n
        for i in range(n):
            count = 0
            for j in range(n):
                if i == j:
                    continue
                if mtx[i][j] <= threshold:
                    count += 1
            if count <= min_cities_reachable:
                min_cities_reachable = count
                city = i
        return city

    @staticmethod
    def _get_graph_matrix(edges, n):
        mtx = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(0)
                else:
                    row.append(1e6)
            mtx.append(row)
        for edge in edges:
            src, dest, wt = edge
            mtx[src][dest] = wt
            mtx[dest][src] = wt
        return mtx


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
