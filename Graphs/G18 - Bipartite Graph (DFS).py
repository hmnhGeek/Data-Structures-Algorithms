# Problem link - https://www.geeksforgeeks.org/problems/bipartite-graph/1
# Solution - https://www.youtube.com/watch?v=KG5YFfR0j8A&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=18


class Graph:
    @staticmethod
    def _invert(color):
        if color == 1:
            return 0
        return 1

    @staticmethod
    def _dfs(graph, node, node_colors, color):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # mark the color of this node with `color`.
        node_colors[node] = color

        # loop on the adjacent nodes of this graph.
        for adj_node in graph[node]:
            # if the adjacent node is not yet colored, perform a DFS on it.
            if node_colors[adj_node] is None:
                # while performing DFS on adjacent node, if it is found that the graph is not bipartite,
                # simply return False.
                if not Graph._dfs(graph, adj_node, node_colors, Graph._invert(color)):
                    return False
            else:
                # if the adjacent node is already colored and that too with the same color as of the `node`,
                # then return False because adjacent nodes cannot have same color in a bipartite graph. If the
                # colors are different, nothing needs to be done.
                if node_colors[adj_node] == color:
                    return False
        # finally, if everything goes fine, return True, it's a bipartite graph.
        return True

    @staticmethod
    def is_bipartite(graph):
        # create a dictionary to store the colors of the nodes.
        node_colors = {i: None for i in graph}

        # initialize a variable to store the result. Assume this graph is bipartite.
        is_bipartite = True

        # loop on all the nodes of the graph.
        for node in node_colors:
            # if the node is not yet colored, i.e., it is not yet visited, we have found a component; run DFS on
            # this node and take a logical AND with the result. Basically, here we are trying to check that all
            # components of the graph need to be bipartite in order for the whole graph to be termed as bipartite.
            if node_colors[node] is None:
                is_bipartite = is_bipartite and Graph._dfs(graph, node, node_colors, 0)
        # finally return the bipartite result for the whole graph.
        return is_bipartite


class Solution:
    @staticmethod
    def is_bipartite(graph):
        return Graph.is_bipartite(graph)


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
            1: [3],
            2: [0, 3],
            3: [0, 1, 2]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        }
    )
)

print(
    Solution.is_bipartite(
        {
            0: [1, 5],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [0, 4]
        }
    )
)