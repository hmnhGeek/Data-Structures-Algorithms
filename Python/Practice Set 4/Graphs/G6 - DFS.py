class Solution:
    @staticmethod
    def _dfs(graph, node, visited):
        # mark the node as visited and push the node to result list.
        visited[node] = True
        print(node, end=" ")

        # loop on the adjacent nodes of this graph
        for adj_node in graph[node]:
            # if the adjacent node is not visited yet, recursively call DFS on it.
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited)

    @staticmethod
    def dfs(graph):
        # create a blank visited map of size O(V).
        visited = {i: False for i in graph}

        # loop on the graph nodes
        for node in graph:
            # if the node is not visited, initiate a DFS from it in O(V + E) time.
            if not visited[node]:
                Solution._dfs(graph, node, visited)
        print()


graph1 = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 4, 7],
    4: [3, 8],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [4, 7]
}
Solution.dfs(graph1)

graph2 = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0],
    4: [2]
}
Solution.dfs(graph2)

graph3 = {
    0: [1, 2],
    1: [0, 2],
    2: [1, 0, 3, 4],
    3: [2],
    4: [2]
}
Solution.dfs(graph3)

graph4 = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3]
}
Solution.dfs(graph4)
