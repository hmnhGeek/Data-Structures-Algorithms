# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
# Solution - https://www.youtube.com/watch?v=9twcmtQj4DU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=19


class Solution:
    @staticmethod
    def _has_cycle(graph, node, visited, path_visited):
        # mark the node as visited and path visited.
        visited[node] = True
        path_visited[node] = True

        # iterate on the adjacent nodes of this node.
        for adj_node in graph[node]:
            # if the adjacent node is not visited, start a DFS from it.
            if not visited[adj_node]:
                # if during the DFS call, a cycle was found, then return True.
                if Solution._has_cycle(graph, adj_node, visited, path_visited):
                    return True
            # if the adjacent node is visited and path visited, then this is a cycle, return True.
            elif path_visited[adj_node]:
                return True

        # finally unmark this node from path visited during returning from recursion.
        path_visited[node] = False
        # return False as no cycle was found.
        return False

    @staticmethod
    def has_cycle(graph):
        """
            This is a typical DFS, and so, the time complexity is O(V + E) and space complexity is O(V).
        """

        # create visited and path visited arrays for this graph. These will take O(2V) space.
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}

        # iterate on all the components of the graph.
        for node in graph:
            if not visited[node]:
                # if in any component, a cycle is found, return True
                if Solution._has_cycle(graph, node, visited, path_visited):
                    return True
        # return False as no cycle was found in any component
        return False


print(
    Solution.has_cycle(
        {
            1: [2],
            2: [3],
            3: [4, 7],
            4: [5],
            5: [6],
            6: [],
            7: [5],
            8: [9],
            9: [10],
            10: [8]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2],
            2: []
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [3],
            3: []
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2, 5],
            2: [3],
            3: [4],
            4: [0, 1],
            5: []
        }
    )
)