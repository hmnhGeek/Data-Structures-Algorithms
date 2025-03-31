# Problem link - https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# Solution - https://www.youtube.com/watch?v=Qzf1a--rhp8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=6


class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def _dfs(self, node, visited, traversal):
        """
            Time complexity is O(V + E) and space complexity is O(V) for the recursion stack.
        """

        # if the node is not visited, visit it, add it to traversal array
        if not visited[node]:
            visited[node] = True
            traversal.append(node)
            # for each adjacent node, call the _dfs method again
            for adj_node in self.graph[node]:
                self._dfs(adj_node, visited, traversal)

    def dfs(self, start_node):
        # create a blank visited array for each node in the graph
        visited = {i: False for i in self.graph}
        # create a variable to store DFS traversal.
        traversal = []
        # call the recursive _dfs method to update traversal array with DFS.
        self._dfs(start_node, visited, traversal)
        # return traversal array.
        return traversal


print(
    Graph(
        {
            1: [2, 6],
            2: [1, 3, 4],
            3: [2],
            4: [2, 5],
            5: [4, 7],
            6: [1, 7, 8],
            7: [5, 6],
            8: [6]
        }
    ).dfs(6)
)

print(
    Graph(
        {
            1: [2, 3],
            2: [5],
            3: [1, 4, 6],
            4: [3],
            5: [7],
            6: [3, 7],
            7: [5, 6]
        }
    ).dfs(1)
)