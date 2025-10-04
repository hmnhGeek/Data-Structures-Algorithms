# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
# Solution - https://www.youtube.com/watch?v=9twcmtQj4DU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=19


class Solution:
    @staticmethod
    def _dfs(graph, node, visited, path_visited):
        visited[node] = path_visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                if Solution._dfs(graph, adj_node, visited, path_visited):
                    return True
            elif path_visited[adj_node]:
                return True
        path_visited[node] = False
        return False

    @staticmethod
    def has_cycle(graph):
        """
            This is a typical DFS, and so, the time complexity is O(V + E) and space complexity is O(V).
        """
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                if Solution._dfs(graph, node, visited, path_visited):
                    return True
        return False


print(
    Solution.has_cycle(
        {
            1: [2],
            2: [3],
            3: [4, 7],
            4: [5],
            5: [6],
            6: [],
            7: [5],
            8: [9],
            9: [10],
            10: [8]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2],
            2: []
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [3],
            3: []
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2, 5],
            2: [3],
            3: [4],
            4: [0, 1],
            5: []
        }
    )
)
