# Problem link - https://www.geeksforgeeks.org/problems/eventual-safe-states/1
# Solution - https://www.youtube.com/watch?v=uRbJ1OF9aYM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=20


class Graph:
    @staticmethod
    def _dfs(graph, node, visited, path_visited, safe_nodes):
        # mark the node as visited and path visited.
        visited[node] = True
        path_visited[node] = True

        # assume all the adjacent nodes are safe nodes.
        all_adjacent_nodes_safe = True

        # loop on the adjacent nodes of this node.
        for adj_node in graph[node]:
            # if the node is not yet visited, initiate a DFS call and whatever be the result,
            # do a logical AND with current value of `all_adjacent_nodes_safe`. This ensures
            # that if this adjacent node is not a safe node, then the `node` itself will be
            # and unsafe node.
            if not visited[adj_node]:
                all_adjacent_nodes_safe = all_adjacent_nodes_safe and Graph._dfs(graph, adj_node, visited, path_visited,
                                                                                 safe_nodes)
            # if the node is visited and path visited also, then there is a cycle and so, not all
            # the adjacent nodes are safe.
            elif path_visited[adj_node]:
                all_adjacent_nodes_safe = False

            # if the nodes is visited but not path visited, then there is no cycle, but a different path.
            # We do not need to initiate a separate DFS call for this adjacent node. In fact, we need to
            # do nothing, but simply update `all_adjacent_nodes_safe` by taking logical AND with the safe
            # node status of this adjacent node because this was already visited in some other path.
            else:
                all_adjacent_nodes_safe = all_adjacent_nodes_safe and safe_nodes[adj_node]

        # finally, if still all the adjacent nodes of this node are safe, then mark this node as safe
        # else mark this node as unsafe.
        safe_nodes[node] = all_adjacent_nodes_safe

        # unmark from path visited as there is no cycle.
        path_visited[node] = False

        # return the status of being safe node or not for this node.
        return all_adjacent_nodes_safe

    @staticmethod
    def safe_nodes(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # declare three dictionaries; for visited, path visited and safe node demarcation.
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}
        safe_nodes = {i: False for i in graph}

        # iterate on the nodes of the graph...
        for node in graph:
            # if the node is not visited, then initiate a DFS traversal from this node.
            if not visited[node]:
                Graph._dfs(graph, node, visited, path_visited, safe_nodes)

        # return the eventual safe nodes.
        return safe_nodes


print(
    Graph.safe_nodes(
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
    Graph.safe_nodes(
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
    Graph.safe_nodes(
        {
            0: [1],
            1: [2],
            2: [0, 3],
            3: []
        }
    )
)

print(
    Graph.safe_nodes(
        {
            0: [1, 2, 3, 4],
            1: [1, 2],
            2: [3, 4],
            3: [0, 4],
            4: []
        }
    )
)
