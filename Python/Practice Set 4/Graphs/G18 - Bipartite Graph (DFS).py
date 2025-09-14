# Problem link - https://www.geeksforgeeks.org/problems/bipartite-graph/1
# Solution - https://www.youtube.com/watch?v=KG5YFfR0j8A&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=18


class Solution:
    @staticmethod
    def _dfs(graph, node, parent, color, node_colors):
        # color the current node
        node_colors[node] = color

        # loop on the neighbours of the node...
        for adj_node in graph[node]:
            # if the adjacent node is parent itself, there is nothing to be done.
            if adj_node == parent:
                continue

            # if the adjacent node is not yet colored, start dfs on it.
            if node_colors[adj_node] is None:
                if not Solution._dfs(graph, adj_node, node, 0 if color == 1 else 1, node_colors):
                    return False

            # if the adjacent node's color is same as current node's color, it's not bipartite.
            if node_colors[adj_node] == color:
                return False

        # else it is bipartite.
        return True

    @staticmethod
    def is_bipartite(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # store the colors of the node
        node_colors = {i: None for i in graph}

        # loop in the nodes of the graph
        for node in graph:
            # if this starting node is not yet colored, start a DFS from here...
            if node_colors[node] is None:
                # if this component is not a bipartite component, the whole graph is not bipartite
                # therefore, return False
                if not Solution._dfs(graph, node, None, 0, node_colors):
                    return False

        # the graph is bipartite, return True
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
