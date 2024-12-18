# Problem link - https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/#floyd-warshall-algorithm
# Solution - https://www.youtube.com/watch?v=YbY8cVwWAvw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=42


class Solution:
    @staticmethod
    def _get_adj_mtx(graph):
        n = len(graph)
        mtx = [[1e6 for _ in range(n)] for _ in range(n)]
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                mtx[node][adj_node] = wt
        # self node wt should be 0.
        for i in range(n):
            mtx[i][i] = 0
        return mtx

    @staticmethod
    def floyd_warshall(graph):
        """
            Time complexity is O(V^3) and space is O(V^2).
        """

        # get the adjacency matrix from a graph using O(V^2) time and O(V^2) space.
        adj_mtx = Solution._get_adj_mtx(graph)
        n = len(graph)

        # using a via node, relax all the edges in the adjacency matrix in O(V^3) time.
        for via_node in graph:
            for u in range(n):
                for v in range(n):
                    adj_mtx[u][v] = min(adj_mtx[u][v], adj_mtx[u][via_node] + adj_mtx[via_node][v])

        # In O(V) time check if there's a negative cycle or not.
        for i in range(n):
            if adj_mtx[i][i] < 0:
                return "Negative cycle detected!"

        # print the adjacency matrix after getting all the shortest distances.
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