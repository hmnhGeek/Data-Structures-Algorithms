# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# Solution - https://www.youtube.com/watch?v=zQ3zgFypzX4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=12


class Solution:
    @staticmethod
    def _dfs_cycle_detect(graph, node, parent, visited):
        # mark this node as visited
        visited[node] = True

        # loop on the adjacent nodes
        for adj_node in graph[node]:
            # if this adjacent node is not yet visited, start a DFS using this node as a source node.
            if not visited[adj_node]:
                # if a cycle is found, return True.
                if Solution._dfs_cycle_detect(graph, adj_node, node, visited):
                    return True
            # if adjacent node is visited and it's not the parent, then there's a cycle, return True.
            elif adj_node != parent:
                return True

        # else finally return False as no cycle was detected.
        return False

    @staticmethod
    def detect_cycle(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # create a visited array for DFS
        visited = {i: False for i in graph}

        # loop on the nodes in the graph
        for node in graph:
            # find a source node for the DFS
            if not visited[node]:
                # if a cycle is found using this node as a source node, return True.
                if Solution._dfs_cycle_detect(graph, node, None, visited):
                    return True
        # else return False.
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
