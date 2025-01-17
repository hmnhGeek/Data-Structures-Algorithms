# Problem link - https://www.geeksforgeeks.org/problems/bipartite-graph/1
# Solution - https://www.youtube.com/watch?v=KG5YFfR0j8A&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=18


class Solution:
    @staticmethod
    def _dfs(graph, node, color, colors):
        # color this node
        colors[node] = color

        # loop on the adjacent nodes
        for adj_node in graph[node]:
            if colors[adj_node] is None:
                # if not bipartite, return False
                if not Solution._dfs(graph, adj_node, 0 if color == 1 else 1, colors):
                    return False
            elif colors[adj_node] == color:
                # if the color of adjacent node and this node is same, return False
                return False

        # finally return True
        return True

    @staticmethod
    def is_bipartite(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # initialize a colors array to store the colors
        colors = {i: None for i in graph}

        # loop on the nodes of the graph
        for node in graph:
            # and if the node is not yet colored, initiate a DFS with color 0 on it.
            if colors[node] is None:
                # if inside the DFS, it is detected that this graph is not bipartite, return False.
                if not Solution._dfs(graph, node, 0, colors):
                    return False

        # else return True.
        return True


print(
    Solution.is_bipartite(
        {
            1: [2],
            2: [3, 6],
            3: [2, 4],
            4: [3, 5, 7],
            5: [4, 6],
            6: [2, 5],
            7: [4, 8],
            8: [7]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            1: [2],
            2: [1, 3, 5],
            3: [2, 4],
            4: [3, 5, 6],
            5: [2, 4],
            6: [4]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1],
            1: [0, 2],
            2: [1]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [2, 3],
            1: [2],
            2: [0, 1, 3],
            3: [0, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1, 3],
            3: [0, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        }
    )
)
