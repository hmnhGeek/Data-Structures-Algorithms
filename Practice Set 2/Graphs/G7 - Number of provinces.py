# Problem link - https://www.geeksforgeeks.org/problems/number-of-provinces/1
# Solution - https://www.youtube.com/watch?v=ACzkVtewUYA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=7


class Solution:
    @staticmethod
    def _dfs(graph, node, visited):
        # mark the node as visited.
        visited[node] = True
        # perform DFS on adjacent nodes.
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited)

    @staticmethod
    def _get_graph(mtx, graph):
        # To generate the graph, we will take O(V^2) time.
        n = len(mtx)
        for i in range(n):
            for j in range(n):
                if i != j and mtx[i][j] == 1:
                    graph[i].append(j)

    @staticmethod
    def num_provinces(mtx):
        """
            Overall time complexity is O(V^2 + V + E) and space complexity is O(V).
        """

        # create a graph of space O(V + E) using V^2 matrix.
        graph = {i: [] for i in range(len(mtx))}
        # This will take O(V^2) time and O(V + E) space.
        Solution._get_graph(mtx, graph)

        # create an adjacency list of O(V) space.
        visited = {i: False for i in graph}

        # store number of components as 0.
        num_components = 0

        # iterate on each node of the graph
        for node in graph:
            # and if the node is not visited
            if not visited[node]:
                # increase the number of components.
                num_components += 1
                # perform a DFS from this node.
                Solution._dfs(graph, node, visited)

        # return the number of components.
        return num_components


print(
    Solution.num_provinces(
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(
    Solution.num_provinces(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(Solution.num_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
