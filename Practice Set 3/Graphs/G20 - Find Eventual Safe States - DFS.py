class Solution:
    @staticmethod
    def _dfs(graph, node, visited, path_visited, safe_nodes):
        visited[node] = True
        path_visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                if Solution._dfs(graph, adj_node, visited, path_visited, safe_nodes):
                    safe_nodes[adj_node] = False
                    return True
            elif path_visited[adj_node]:
                safe_nodes[adj_node] = False
                return True
        path_visited[node] = False
        return False

    @staticmethod
    def find_safe_states(graph):
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}
        safe_nodes = {i: True for i in graph}
        for node in graph:
            if not visited[node]:
                if Solution._dfs(graph, node, visited, path_visited, safe_nodes):
                    safe_nodes[node] = False
        return safe_nodes


print(
    Solution.find_safe_states(
        {
            1: [2],
            2: [3],
            3: [4, 5],
            4: [6],
            5: [6],
            6: [7],
            7: [],
            8: [1, 9],
            9: [10],
            10: [8],
            11: [9]
        }
    )
)

print(
    Solution.find_safe_states(
        {
            0: [1, 2],
            1: [2, 3],
            2: [5],
            3: [0],
            4: [5],
            5: [],
            6: []
        }
    )
)

print(
    Solution.find_safe_states(
        {
            0: [1],
            1: [2],
            2: [0, 3],
            3: []
        }
    )
)

print(
    Solution.find_safe_states(
        {
            0: [1, 2, 3, 4],
            1: [1, 2],
            2: [3, 4],
            3: [0, 4],
            4: []
        }
    )
)
