# Problem link - https://www.geeksforgeeks.org/problems/number-of-provinces/1
# Solution - https://www.youtube.com/watch?v=ACzkVtewUYA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=7


class Solution:
    @staticmethod
    def _dfs(graph, node, visited):
        # mark the node as visited and perform dfs on adjacent nodes.
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited)

    @staticmethod
    def _get_graph(mtx):
        n = len(mtx)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j and mtx[i][j] == 1:
                    graph[i].append(j)
        return graph

    @staticmethod
    def find_num_provinces(mtx):
        """
            Time complexity is O(V + E + V^2) and space complexity is O(V + E).
        """

        # get the graph from the matrix in O(V^2) time and O(V + E) space.
        graph = Solution._get_graph(mtx)

        # define a visited array of size V to use in DFS.
        visited = {i: False for i in graph}

        # get the number of provinces in this variable.
        num_provinces = 0

        # loop on the nodes of the graph
        for node in graph:
            # if this node is not yet visited, this is a new component
            if not visited[node]:
                num_provinces += 1
                Solution._dfs(graph, node, visited)

        # return the number of provinces.
        return num_provinces



print(
    Solution.find_num_provinces(
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(
    Solution.find_num_provinces(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(Solution.find_num_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))