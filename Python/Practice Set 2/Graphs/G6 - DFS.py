# Problem link - https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# Solution - https://www.youtube.com/watch?v=Qzf1a--rhp8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=6


class Solution:
    @staticmethod
    def _dfs(graph, node, visited, traversal):
        visited[node] = True
        traversal.append(node)
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited, traversal)

    @staticmethod
    def dfs(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        visited = {i: False for i in graph}
        traversal = []
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, visited, traversal)
        return traversal


print(
    Solution.dfs(
        {
            1: [2, 3],
            2: [1, 5, 6],
            3: [1, 4, 7],
            4: [3, 8],
            5: [2],
            6: [2],
            7: [3, 8],
            8: [4, 7]
        }
    )
)

print(
    Solution.dfs(
        {
            0: [1, 2, 3],
            1: [0],
            2: [0, 4],
            3: [0],
            4: [2]
        }
    )
)

print(
    Solution.dfs(
        {
            0: [1, 2],
            1: [0, 2],
            2: [1, 0, 3, 4],
            3: [2],
            4: [2]
        }
    )
)

print(
    Solution.dfs(
        {
            0: [1],
            1: [0, 2],
            2: [1],
            3: [4],
            4: [3]
        }
    )
)