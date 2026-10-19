class Solution:
    @staticmethod
    def get_bridges(graph):
        n = len(graph)
        low = {i: 0 for i in graph}
        tin = {i: 0 for i in graph}
        visited = {i: False for i in graph}
        bridges = []
        timer = [1]
        for node in graph:
            if not visited[node]:
                Solution._dfs(node, -1, tin, low, visited, timer, bridges, graph)
        return bridges

    @staticmethod
    def _dfs(node, parent, tin, low, visited, timer, bridges, graph):
        visited[node] = True
        tin[node] = low[node] = timer[0]
        timer[0] += 1
        for adj_node in graph[node]:
            if adj_node == parent:
                continue
            if not visited[adj_node]:
                Solution._dfs(adj_node, node, tin, low, visited, timer, bridges, graph)
                low[node] = min(low[node], low[adj_node])
                if low[adj_node] > tin[node]:
                    bridges.append((adj_node, node))
            else:
                low[node] = min(low[node], low[adj_node])


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
