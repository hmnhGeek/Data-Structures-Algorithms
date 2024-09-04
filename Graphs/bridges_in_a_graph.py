class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list
        self.timer = 1

    def _dfs_fetch_bridges(self, parent, node, visited, in_time, min_time, bridges):
        # mark the node as visited and set the in time and min time as the timer value.
        visited[node] = True
        in_time[node] = self.timer
        min_time[node] = self.timer

        # increment the timer by 1 unit.
        self.timer += 1

        # iterate on the adjacent nodes of the current node
        for adj_node in self.graph[node]:
            # if the adjacent node is parent, do nothing because this is something you're coming from.
            if adj_node == parent:
                continue

            # if the adjacent node is not yet visited, do a DFS on it
            if not visited[adj_node]:
                self._dfs_fetch_bridges(node, adj_node, visited, in_time, min_time, bridges)

                # update the min time of this node by comparing it with the min time of adjacent node.
                min_time[node] = min(min_time[node], min_time[adj_node])

                # if the min time of adjacent node is more than the min time of this node, the edge between
                # them must be a bridge.
                if min_time[adj_node] > min_time[node]:
                    bridges.append((node, adj_node))
            else:
                # else, if the adjacent node is already visited, no need of a DFS; simply update the min time
                # of this node by comparing it with the min time of the adjacent node.
                min_time[node] = min(min_time[node], min_time[adj_node])

    def get_bridges(self, start_node):
        # The time complexity is O(V + E) and space complexity is O(3V + E)

        # Store the minimum time (from adjacent nodes) and time of first appearance of every node in a dictionary.
        min_time = {i: float("inf") for i in self.graph}
        in_time = {i: float("inf") for i in self.graph}

        # store a visited array, typically for a DFS traversal.
        visited = {i: False for i in self.graph}

        # create an array to hold bridges.
        bridges = []

        # do a DFS from the starting node with no parent. This will take O(V + E) time for DFS.
        self._dfs_fetch_bridges(None, start_node, visited, in_time, min_time, bridges)

        # reset the timer in case for reuse.
        self.timer = 1

        # return the bridges that are found.
        return bridges


class BridgesFinder:
    # This is a utility class which will use the `Graph` class to find the bridges.
    def __init__(self, edge_list):
        self.graph = Graph(self._build_graph_from_edges(edge_list))

    def _build_graph_from_edges(self, edge_list):
        graph = {}
        for edge in edge_list:
            # create an edge between source to destination and vice-versa at the same time.
            source, destination = edge
            if source not in graph:
                graph[source] = [destination]
            else:
                graph[source].append(destination)

            if destination not in graph:
                graph[destination] = [source]
            else:
                graph[destination].append(source)

        return graph

    def get_bridges(self, start_node):
        # This will take O(V + E) time and space each.
        return self.graph.get_bridges(start_node)


print(BridgesFinder([[0, 1], [1, 2], [2, 0], [1, 3]]).get_bridges(0))
print(BridgesFinder([[0, 1]]).get_bridges(1))
print(BridgesFinder([[0, 1], [1, 2], [0, 2], [2, 3]]).get_bridges(2))
print(
    BridgesFinder(
        [
            [1, 2],
            [1, 3],
            [2, 3],
            [2, 4]
        ]
    ).get_bridges(4)
)
