class Graph:
    @staticmethod
    def _dfs(graph, i, j, p, q, visited, max_effort, all_efforts, n, m):
        # if you've reached the last cell.
        if i == n - 1 and j == m - 1:
            # take the minimum effort out of all the efforts
            all_efforts[0] = min(all_efforts[0], max(max_effort, abs(graph[p][q] - graph[i][j])))
            return

        visited[i][j] = True

        # update the max effort for this path.
        max_effort = max(max_effort, abs(graph[p][q] - graph[i][j]))

        if 0 <= i - 1 < n and not visited[i - 1][j]:
            Graph._dfs(graph, i - 1, j, i, j, visited, max_effort, all_efforts, n, m)

        if 0 <= j + 1 < m and not visited[i][j + 1]:
            Graph._dfs(graph, i, j + 1, i, j, visited, max_effort, all_efforts, n, m)

        if 0 <= i + 1 < n and not visited[i + 1][j]:
            Graph._dfs(graph, i + 1, j, i, j, visited, max_effort, all_efforts, n, m)

        if 0 <= j - 1 < m and not visited[i][j - 1]:
            Graph._dfs(graph, i, j - 1, i, j, visited, max_effort, all_efforts, n, m)

        # once backtracking reset the visited flag.
        visited[i][j] = False

    @staticmethod
    def get_min_effort(graph):
        n, m = len(graph), len(graph[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        all_efforts = [1e6]
        # start dfs from (0, 0) and take previous also (0, 0), with max effort set to 0.
        Graph._dfs(graph, 0, 0, 0, 0, visited, 0, all_efforts, n, m)
        return all_efforts[0]


print(Graph.get_min_effort([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(Graph.get_min_effort([[7, 7], [7, 7]]))
print(Graph.get_min_effort([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(Graph.get_min_effort([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))