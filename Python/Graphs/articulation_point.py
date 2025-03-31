# Problem link - https://naukri.com/code360/library/articulation-points-in-a-graph
# Solution - https://www.youtube.com/watch?v=j1QDfU21iZk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=56


class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list
        self.timer = 1

    def _find_articulation_points(self, parent, node, visited, in_time, min_time, articulation_pts):
        # mark the node as visited
        visited[node] = True

        # populate the in time and min time with timer value.
        in_time[node] = self.timer
        min_time[node] = self.timer

        # increment the timer by 1 unit
        self.timer += 1

        # count the number of children for this node.
        child = 0

        # traverse on the adjacent nodes
        for adj_node in self.graph[node]:
            # if the adjacent node is parent, don't do anything.
            if adj_node == parent:
                continue

            # if the adjacent node is not visited, do a DFS on it.
            if not visited[adj_node]:
                self._find_articulation_points(node, adj_node, visited, in_time, min_time, articulation_pts)

                # update the min_time of this node with the min of current node and adjacent node's min_time.
                min_time[node] = min(min_time[adj_node], min_time[node])

                # if min_time of adjacent node is greater than the in time of the current node, and the parent is not
                # None, i.e., node is not the starting node, then this node is an articulation node.
                if min_time[adj_node] >= in_time[node] and parent is not None:
                    articulation_pts[node] = True

                # increment the child count.
                child += 1
            else:
                # min_time of the node should be the min of the min_time[node] and the in_time[adj_node] (in_time of
                # adj_node because adj_node is visited; don't confuse with the bridge question. Here we have to consider
                # in_time for adj_node because its visited; hence in else condition.)
                min_time[node] = min(in_time[adj_node], min_time[node])

        # if there is more than 1 child for this node and its parent is None, then it's the starting node. And when the
        # starting node has more than one child, then after removing this node, there will be more than one component
        # created. Mark this node as true as articulation point.
        if child > 1 and parent is None:
            articulation_pts[node] = True

    def get_articulation_points(self, start_node):
        # DFS will take O(V + E) time and (4V + E) space.

        # visited array is needed for DFS traversal.
        visited = {i: False for i in self.graph}

        # store in time and min time
        in_time = {i: float('inf') for i in self.graph}
        min_time = {i: float('inf') for i in self.graph}

        # store articulation points array which will be marked True for relevant nodes.
        articulation_points = {i: False for i in self.graph}

        # populate the `articulation_points` array.
        self._find_articulation_points(None, start_node, visited, in_time, min_time, articulation_points)

        # return that array.
        return articulation_points


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
        return self.graph.get_articulation_points(start_node)


print(
    BridgesFinder(
        [
            [0, 1],
            [1, 4],
            [3, 4],
            [3, 2],
            [4, 2]
        ]
    ).get_bridges(3)
)

print(
    BridgesFinder(
        [
            [0, 4],
            [0, 1],
            [1, 4],
            [2, 4],
            [4, 3],
            [2, 3]
        ]
    ).get_bridges(4)
)

print(
    BridgesFinder(
        [
            ["A", "B"],
            ["A", "F"],
            ["B", "F"],
            ["F", "C"],
            ["F", "E"],
            ["E", "D"],
            ["C", "D"]
        ]
    ).get_bridges("F")
)

print(
    BridgesFinder(
        [
            ["A", "B"],
            ["B", "C"],
            ["C", "D"],
            ["D", "E"]
        ]
    ).get_bridges("E")
)