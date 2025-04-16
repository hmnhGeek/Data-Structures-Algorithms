class Solution:
    _timer = 1

    @staticmethod
    def _dfs(graph, node, parent, tin, low, visited, bridges):
        # mark the node as visited
        visited[node] = True

        # assign the latest time and increment the timer.
        tin[node] = low[node] = Solution._timer
        Solution._timer += 1

        # loop on the adjacent nodes.
        for adj_node in graph[node]:
            # if the adjacent node is the parent itself, do nothing.
            if adj_node == parent:
                continue

            # if the adjacent node is not yet visited, perform a dfs on the adjacent node.
            elif not visited[adj_node]:
                Solution._dfs(graph, adj_node, node, tin, low, visited, bridges)

                # once the dfs on the adjacent node is completed, make the node inherit the lowest time from it.
                low[node] = min(low[node], low[adj_node])

                # if low time of adjacent node is more than low time of node, then it means we cannot reach this
                # adjacent node except via node. Thus, this edge is a bridge.
                if low[node] < low[adj_node]:
                    bridges.append((node, adj_node))
            else:
                # else if the adjacent node is already visited, simply update the lowest time of the node.
                low[node] = min(low[node], low[adj_node])

    @staticmethod
    def get_bridges(graph):
        Solution._timer = 1

        # create tracking variables
        tin = {i: -1 for i in graph}
        low = {i: -1 for i in graph}
        visited = {i: False for i in graph}

        # create list which will store the bridges and update it using DFS.
        bridges = []
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, None, tin, low, visited, bridges)

        # return the bridges.
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
