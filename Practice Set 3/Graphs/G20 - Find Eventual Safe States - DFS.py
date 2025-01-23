# Problem link - https://www.geeksforgeeks.org/problems/eventual-safe-states/1
# Solution - https://www.youtube.com/watch?v=uRbJ1OF9aYM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=20


class Solution:
    @staticmethod
    def _dfs(graph, node, visited, path_visited, safe_nodes):
        # mark this node as visited and path visited
        visited[node] = True
        path_visited[node] = True

        # loop on the adjacent nodes of the graph
        for adj_node in graph[node]:
            # if this node is not visited
            if not visited[adj_node]:
                # and if this adj_node leads to a cycle, mark it as unsafe.
                if Solution._dfs(graph, adj_node, visited, path_visited, safe_nodes):
                    safe_nodes[adj_node] = False
                    return True
            # or if, this node is visited and path visited, then there's a cycle, again mark this adj_node as unsafe.
            elif path_visited[adj_node]:
                safe_nodes[adj_node] = False
                return True

        # unmark this node from path visited.
        path_visited[node] = False

        # no cycle was detected, return False.
        return False

    @staticmethod
    def find_safe_states(graph):
        """
            Time complexity is O(V + E) and space complexity is O(3V).
        """

        # create visited and path visited arrays to detect cycles
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}

        # create a dictionary to store the safe nodes. Assume all of them are safe initially.
        safe_nodes = {i: True for i in graph}

        # loop on the graph components.
        for node in graph:
            if not visited[node]:
                # if there is a cycle from this node, mark this node as unsafe.
                if Solution._dfs(graph, node, visited, path_visited, safe_nodes):
                    safe_nodes[node] = False
        return safe_nodes


print(
    Solution.find_safe_states(
        {
            1: [2],
            2: [3],
            3: [4, 5],
            4: [6],
            5: [6],
            6: [7],
            7: [],
            8: [1, 9],
            9: [10],
            10: [8],
            11: [9]
        }
    )
)

print(
    Solution.find_safe_states(
        {
            0: [1, 2],
            1: [2, 3],
            2: [5],
            3: [0],
            4: [5],
            5: [],
            6: []
        }
    )
)

print(
    Solution.find_safe_states(
        {
            0: [1],
            1: [2],
            2: [0, 3],
            3: []
        }
    )
)

print(
    Solution.find_safe_states(
        {
            0: [1, 2, 3, 4],
            1: [1, 2],
            2: [3, 4],
            3: [0, 4],
            4: []
        }
    )
)
