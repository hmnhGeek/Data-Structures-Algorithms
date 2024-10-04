# Problem link - https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1


class Utils:
    @classmethod
    def _get_neighbours(cls, matrix, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and matrix[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= i - 1 < n and 0 <= j + 1 < m and matrix[i - 1][j + 1] == 1:
            neighbours.append((i - 1, j + 1))
        if 0 <= j + 1 < m and matrix[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and 0 <= j + 1 < m and matrix[i + 1][j + 1] == 1:
            neighbours.append((i + 1, j + 1))
        if 0 <= i + 1 < n and matrix[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= i + 1 < n and 0 <= j - 1 < m and matrix[i + 1][j - 1] == 1:
            neighbours.append((i + 1, j - 1))
        if 0 <= j - 1 < m and matrix[i][j - 1] == 1:
            neighbours.append((i, j - 1))
        if 0 <= i - 1 < n and 0 <= j - 1 < m and matrix[i - 1][j - 1] == 1:
            neighbours.append((i - 1, j - 1))
        return neighbours

    @staticmethod
    def convert_grid_to_graph(matrix):
        n, m = len(matrix), len(matrix[0])
        graph = {}
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    node = i * m + j
                    if node not in graph:
                        graph[node] = []
                    neighbours = Utils._get_neighbours(matrix, i, j, n, m)
                    for neighbour in neighbours:
                        a, b = neighbour
                        adj_node = a * m + b
                        graph[node].append(adj_node)
        return graph


class Graph:
    @classmethod
    def _dfs(cls, graph, node, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Graph._dfs(graph, adj_node, visited)

    @staticmethod
    def dfs(graph):
        visited = {i: False for i in graph}
        num_components = 0
        for node in visited:
            if not visited[node]:
                num_components += 1
                Graph._dfs(graph, node, visited)
        return num_components


class Solution:
    @staticmethod
    def find_num_islands(matrix):
        return Graph.dfs(Utils.convert_grid_to_graph(matrix))


print(
    Solution.find_num_islands(
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 1]
        ]
    )
)

print(Solution.find_num_islands([[0, 1], [1, 0], [1, 1], [1, 0]]))
print(Solution.find_num_islands([[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0]]))
