# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# Solution - https://www.youtube.com/watch?v=zQ3zgFypzX4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=12


class Solution:
    @staticmethod
    def dfs(graph, node, parent, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if adj_node == parent:
                continue
            elif not visited[adj_node]:
                if Solution.dfs(graph, adj_node, node, visited):
                    return True
            else:
                return True
        return False

    @staticmethod
    def detect_cycle(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                if Solution.dfs(graph, node, None, visited):
                    return True
        return False


print(
    Solution.detect_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 6],
            4: [3],
            5: [2, 7],
            6: [3, 7],
            7: [5, 6]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 6],
            4: [3],
            5: [2, 7],
            6: [3],
            7: [5]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [],
            1: [2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [1],
            1: [0, 2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 3]
        }
    )
)
