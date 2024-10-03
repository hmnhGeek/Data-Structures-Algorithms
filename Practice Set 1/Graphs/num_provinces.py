class Graph:
    @classmethod
    def _dfs(cls, graph, node, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Graph._dfs(graph, adj_node, visited)

    @staticmethod
    def get_num_components(adjacency_list):
        visited = {i: False for i in adjacency_list}
        num_components = 0
        for node in visited:
            if not visited[node]:
                num_components += 1
                Graph._dfs(adjacency_list, node, visited)
        return num_components


class Solution:
    @staticmethod
    def find_num_provinces(graph):
        return Graph.get_num_components(graph)


print(
    Solution.find_num_provinces(
        {
            1: [3],
            2: [],
            3: [1]
        }
    )
)

print(
    Solution.find_num_provinces(
        {
            1: [],
            2: [],
            3: []
        }
    )
)

print(
    Solution.find_num_provinces(
        {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: []
        }
    )
)