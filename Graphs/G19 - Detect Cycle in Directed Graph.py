# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
# Solution - https://www.youtube.com/watch?v=9twcmtQj4DU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=19


class Graph:
    @staticmethod
    def _has_cycle(graph, node, visited, path_visited):
        # mark the node as visited and path visited.
        visited[node] = True
        path_visited[node] = True

        # loop on the adjacent nodes of the graph
        for adj_node in graph[node]:
            # if the adjacent node is not visited, then it is simple, just do a DFS on it.
            if not visited[adj_node]:
                # if a cycle is found from the adjacent node, return True.
                if Graph._has_cycle(graph, adj_node, visited, path_visited):
                    return True
            # if however, the node is visited and is also path visited, this would mean that the same
            # node can be visited again and again even by staying on the same path, i.e., there's a cycle
            # and therefore return True.
            elif path_visited[adj_node]:
                return True

        # once all the adjacent nodes are done with, unmark the current node from path visited. Basically,
        # here we are implying that we have checked this path.
        path_visited[node] = False
        # finally return False if there was no cycle detected.
        return False

    @staticmethod
    def detect_cycle(graph):
        """
            Overall time complexity is O(V + E) and space complexity is O(V).
        """

        # create a visited and path visited array for the nodes in the graph. This will take O(V) space.
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}

        # loop on the nodes from the graph.
        for node in graph:
            # if the node is not visited, we have a component to check.
            if not visited[node]:
                # detect if there is a cycle starting from this node.
                has_cycle = Graph._has_cycle(graph, node, visited, path_visited)
                # if there is, then basically the graph has cycle, return True
                if has_cycle:
                    return True
        # if there is no component in which a cycle was found, return False as there is no cycle in the graph.
        return False


print(
    Graph.detect_cycle(
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
    Graph.detect_cycle(
        {
            0: [1],
            1: [2],
            2: []
        }
    )
)

print(
    Graph.detect_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
    )
)

print(
    Graph.detect_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [3],
            3: []
        }
    )
)