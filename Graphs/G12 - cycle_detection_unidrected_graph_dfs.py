# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# Solution - https://www.youtube.com/watch?v=zQ3zgFypzX4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=12


class Graph:
    @staticmethod
    def _dfs_has_cycle(graph, node, parent, visited):
        # in the DFS call, we first mark the current node as visited
        visited[node] = True

        # now loop on all the adjacent nodes.
        for adj_node in graph[node]:
            # if the adjacent node is already visited, and it is not a parent, then there must be a cycle
            if visited[adj_node] and adj_node != parent:
                # return True, because only parent node as an adjacent node can be visited
                return True
            elif not visited[adj_node]:
                # else if the adjacent node is not visited yet, check if a cycle is found further down the
                # recursion. If yes, return True
                if Graph._dfs_has_cycle(graph, adj_node, node, visited):
                    return True
        # finally, for all the DFS calls on the adjacent nodes, if no cycle was found, return False.
        return False

    @staticmethod
    def has_cycle(graph):
        """
            Overall time complexity is O(V + E) and space complexity is O(V).
        """

        # if the graph has multiple components, we can cater to that using this logic. Create a blank
        # visited array for each node in the graph.
        visited = {i: False for i in graph}

        # loop on each node in the graph using visited array (or simply the graph)
        for node in visited:
            # if the node is not yet visited, we are inside one of the components.
            if not visited[node]:
                # using this node as a starting node, check if this component has a cycle or not.
                if Graph._dfs_has_cycle(graph, node, None, visited):
                    # if it has a cycle, return True.
                    return True
        # if no component has a cycle, return False.
        return False


print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [5],
            3: [1, 4, 6],
            4: [3],
            5: [7],
            6: [3, 7],
            7: [5, 6]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [],
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [1],
            3: [1, 4],
            4: [3],
            5: [],
            6: [],
            7: [8],
            8: [7]
        }
    )
)

print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [1, 5, 6],
            3: [1, 4, 7],
            4: [3],
            5: [2],
            6: [2],
            7: [3, 8],
            8: [7]
        }
    )
)

print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 7],
            4: [3, 8],
            5: [2],
            6: [],
            7: [3, 8],
            8: [4, 7]
        }
    )
)