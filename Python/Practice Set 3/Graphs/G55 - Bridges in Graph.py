class Solution:
    _timer = 1

    @staticmethod
    def _dfs(graph, node, parent, tin, low, visited, bridges):
        visited[node] = True
        tin[node] = low[node] = Solution._timer
        Solution._timer += 1
        for adj_node in graph[node]:
            if adj_node == parent:
                continue
            elif not visited[adj_node]:
                Solution._dfs(graph, adj_node, node, tin, low, visited, bridges)
                low[node] = min(low[node], low[adj_node])
                if low[node] < low[adj_node]:
                    bridges.append((node, adj_node))
            else:
                low[node] = min(low[node], low[adj_node])

    @staticmethod
    def get_bridges(graph):
        Solution._timer = 1
        tin = {i: -1 for i in graph}
        low = {i: -1 for i in graph}
        visited = {i: False for i in graph}
        bridges = []
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, None, tin, low, visited, bridges)
        return bridges


print(
    Solution.get_bridges(
        {
            1: [2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 3, 5],
            5: [4, 6],
            6: [5, 7, 9],
            7: [6, 8],
            8: [7, 9, 10],
            9: [6, 8],
            10: [8, 11],
            11: [10, 12],
            12: [10, 11]
        }
    )
)

print(
    Solution.get_bridges(
        {
            0: [1, 2],
            1: [0, 2, 3],
            2: [1, 0],
            3: [1]
        }
    )
)

print(
    Solution.get_bridges(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [1, 0],
            3: [0, 4],
            4: [3]
        }
    )
)

print(
    Solution.get_bridges(
        {
            0: [1, 2],
            1: [0, 2, 6, 4, 3],
            2: [0, 1],
            3: [1, 5],
            4: [1, 5],
            5: [3, 4],
            6: [1]
        }
    )
)

print(
    Solution.get_bridges(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
    )
)
