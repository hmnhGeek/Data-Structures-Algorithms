# Problem link - https://www.geeksforgeeks.org/problems/is-it-a-tree/1


class Solution:
    @staticmethod
    def _dfs(graph, node, parent, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                if Solution._dfs(graph, adj_node, node, visited):
                    return True
            elif adj_node != parent:
                return True
        return False

    @staticmethod
    def _graph_has_cycle(graph, disconnected):
        visited = {i: False for i in graph}
        num_components = 0
        for node in graph:
            if not visited[node]:
                num_components += 1
                # if more than one component has been found, set the status of disconnected to True.
                if num_components > 1:
                    disconnected[0] = True
                if Solution._dfs(graph, node, None, visited):
                    return True
        return False

    @staticmethod
    def check_if_tree(graph):
        """
            Detecting cycle will take O(V + E) time and O(V) space.
            Detecting multiple components will be done in the above step only.

            Time complexity is thus O(V + E) and space complexity is O(V).
        """

        # store the disconnected components status in a variable
        is_disconnected = [False]
        # check if the graph has cycle
        has_cycle = Solution._graph_has_cycle(graph, is_disconnected)
        # the graph is a tree if it has no cycle and all the nodes are connected (no multiple components)
        if not has_cycle and not is_disconnected[0]:
            return True
        return False


print(
    Solution.check_if_tree(
        {
            0: [1, 2, 3],
            1: [0],
            2: [0],
            3: [0, 4],
            4: [3]
        }
    )
)

print(
    Solution.check_if_tree(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1],
            3: [0, 4],
            4: [3]
        }
    )
)

print(
    Solution.check_if_tree(
        {
            0: [1],
            1: [0, 2, 3],
            3: [1],
            2: [1]
        }
    )
)

print(
    Solution.check_if_tree(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        }
    )
)
