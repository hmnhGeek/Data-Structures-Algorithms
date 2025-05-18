class Solution:
    @staticmethod
    def _get_graph(mtx):
        n = len(mtx)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if mtx[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        return graph

    @staticmethod
    def _dfs(graph, node, visited):
        # mark the node as visited and perform dfs on adjacent nodes.
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited)

    @staticmethod
    def find_num_provinces(mtx):
        # get the graph from the matrix in O(V^2) time and O(V + E) space.
        graph = Solution._get_graph(mtx)

        # define a visited array of size V to use in DFS.
        visited = {i: False for i in range(len(mtx))}

        # get the number of provinces in this variable.
        num_components = 0

        # loop on the nodes of the graph
        for node in graph:
            # if this node is not yet visited, this is a new component
            if not visited[node]:
                num_components += 1
                Solution._dfs(graph, node, visited)

        # return the number of provinces.
        return num_components


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