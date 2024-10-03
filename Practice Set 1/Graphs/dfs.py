class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def _dfs(self, node, visited, traversal):
        if not visited[node]:
            visited[node] = True
            traversal.append(node)
            for adj_node in self.graph[node]:
                self._dfs(adj_node, visited, traversal)

    def dfs(self, start_node):
        visited = {i: False for i in self.graph}
        traversal = []
        self._dfs(start_node, visited, traversal)
        return traversal


print(
    Graph(
        {
            1: [2, 6],
            2: [1, 3, 4],
            3: [2],
            4: [2, 5],
            5: [4, 7],
            6: [1, 7, 8],
            7: [5, 6],
            8: [6]
        }
    ).dfs(6)
)