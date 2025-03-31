# Problem link - https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1
# Solution - https://www.youtube.com/watch?v=PwMVNSJ5SLI&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=43


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
        """
            Time complexity is O(V^3) and space complexity is O(V^2).
        """

        # get the adjacency matrix from the edge list in O(E) time and O(V^2) space.
        adj_mtx = Solution._get_adj_mtx(edges, n)
        # Apply Floyd-Warshall in O(V^3) time to get the shortest distances from all the nodes.
        Solution._apply_floyd_warshall(adj_mtx, n)

        # assume the minimum cities reachable to be n.
        min_cities_reachable = n
        # from city to be assumed as -1.
        from_city = -1

        # loop on all the cities as from city in O(V^2).
        for i in range(n):
            # count the number of cities reachable within threshold
            count = 0
            for j in range(n):
                # count such cities
                if adj_mtx[i][j] <= threshold:
                    count += 1
            # if the count is same or lower than min cities reachable, then update the from-city and min cities
            # reachable count.
            if count <= min_cities_reachable:
                from_city = i
                min_cities_reachable = count

        # return the final from_city.
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
