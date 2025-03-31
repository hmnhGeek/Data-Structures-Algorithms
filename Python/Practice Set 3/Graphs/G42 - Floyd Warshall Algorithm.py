# Problem link - https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/#floyd-warshall-algorithm
# Solution - https://www.youtube.com/watch?v=YbY8cVwWAvw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=42


class Solution:
    @staticmethod
    def get_adjacency_mtx(graph):
        mtx = [[1e6 for _ in range(len(graph))] for _ in range(len(graph))]
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                mtx[node][adj_node] = wt
        for i in range(len(graph)):
            mtx[i][i] = 0
        return mtx

    @staticmethod
    def floyd_warshall(graph):
        """
            Overall time complexity is O(V^3) and space complexity is O(V^2).
        """

        n = len(graph)

        # Time complexity is O(V + E) and space complexity is O(V^2).
        distances = Solution.get_adjacency_mtx(graph)
        for i in range(n):
            distances[i][i] = 0

        # Time complexity is O(V^3)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        for i in range(n):
            if distances[i][i] < 0:
                return -1
        for row in distances:
            print(row)
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
