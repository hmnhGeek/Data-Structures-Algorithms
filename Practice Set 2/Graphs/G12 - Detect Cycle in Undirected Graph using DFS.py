# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# Solution - https://www.youtube.com/watch?v=zQ3zgFypzX4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=12


class Solution:
    @staticmethod
    def _has_cycle(graph, node, parent, visited):
        # visit the node
        visited[node] = True
        for adj_node in graph[node]:
            # if the adjacent node is not visited, visit it using DFS.
            if not visited[adj_node]:
                # if a cycle is detected during the visit, return True.
                if Solution._has_cycle(graph, adj_node, node, visited):
                    return True
            # if the adjacent node is not a parent, and it is visited, there must be a cycle.
            elif adj_node != parent:
                return True
        # else there is no cycle, return False.
        return False

    @staticmethod
    def detect_cycle(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                # if any component has a cycle, return True.
                if Solution._has_cycle(graph, node, None, visited):
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