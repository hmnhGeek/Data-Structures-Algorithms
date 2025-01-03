# Problem link - https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1
# Solution - https://www.youtube.com/watch?v=PwMVNSJ5SLI&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=43


class Graph:
    @staticmethod
    def _get_graph(edge_list, n):
        graph = [[1e6 for _ in range(n)] for _ in range(n)]
        for edge in edge_list:
            src, dest, wt = edge
            graph[src][dest] = wt
            graph[dest][src] = wt

        for i in range(n):
            graph[i][i] = 0

        return graph

    @staticmethod
    def floyd_warshall(edge_list, n):
        graph = Graph._get_graph(edge_list, n)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        for i in range(n):
            if graph[i][i] < 0:
                return -1

        return graph


class Solution:
    @staticmethod
    def _get_count(row, threshold):
        count = 0
        for i in row:
            if i <= threshold:
                count += 1
        return count

    @staticmethod
    def get(edge_list, n, threshold):
        """
            Time complexity is O(n^3) and space complexity is O(n^2).
        """

        # Ot(n^3) and Os(n^2)
        min_distances = Graph.floyd_warshall(edge_list, n)
        min_count = 1e6
        city = -1

        # This will also take O(n^2) time.
        for row in range(n):
            count = Solution._get_count(min_distances[row], threshold)
            if min_count >= (count - 1):
                min_count = count - 1
                city = row
        return f"Minimum reachable cities is {min_count} with city = {city}"


print(
    Solution.get(
        [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]],
        4,
        4
    ))
