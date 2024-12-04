# Problem link - https://www.geeksforgeeks.org/problems/eventual-safe-states/1
# Solution - https://www.youtube.com/watch?v=uRbJ1OF9aYM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=20


class Solution:
    @staticmethod
    def _has_cycle(graph, node, visited, path_visited, safe_nodes):
        # mark nodes as visited and path visited.
        visited[node] = True
        path_visited[node] = True

        # loop on the adjacent nodes.
        for adj_node in graph[node]:
            # typical cycle detection code from G19.
            if not visited[adj_node]:
                if Solution._has_cycle(graph, adj_node, visited, path_visited, safe_nodes):
                    return True
            elif path_visited[adj_node]:
                return True

        # unmark this node from path visited
        path_visited[node] = False
        # mark this node as safe as no adjacent node gave a cycle.
        safe_nodes[node] = True
        # return False for this node, as no cycle was found.
        return False

    @staticmethod
    def find_safe_states(graph):
        """
            Overall time complexity is O(V + E) and space is O(3V).
        """

        # define variables for visited, path visited and safe nodes. This will take O(3V) space.
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}
        safe_nodes = {i: False for i in graph}

        # loop on all the components.
        for node in graph:
            if not visited[node]:
                # if there's a cycle, don't break, continue checking for all the nodes.
                Solution._has_cycle(graph, node, visited, path_visited, safe_nodes)
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