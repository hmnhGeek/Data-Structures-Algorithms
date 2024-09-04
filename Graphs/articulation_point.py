class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list
        self.timer = 1

    def _find_articulation_points(self, parent, node, visited, in_time, min_time, articulation_pts):
        visited[node] = True
        in_time[node] = self.timer
        min_time[node] = self.timer
        self.timer += 1
        child = 0

        for adj_node in self.graph[node]:
            if adj_node == parent:
                continue

            if not visited[adj_node]:
                self._find_articulation_points(node, adj_node, visited, in_time, min_time, articulation_pts)
                min_time[node] = min(min_time[adj_node], min_time[node])
                if min_time[adj_node] >= in_time[node] and parent is not None:
                    articulation_pts[node] = True
                child += 1
            else:
                min_time[node] = min(in_time[adj_node], in_time[node])

        if child > 1 and parent is None:
            articulation_pts[node] = True

    def get_articulation_points(self, start_node):
        visited = {i: False for i in self.graph}
        in_time = {i: float('inf') for i in self.graph}
        min_time = {i: float('inf') for i in self.graph}
        articulation_points = {i: False for i in self.graph}
        self._find_articulation_points(None, start_node, visited, in_time, min_time, articulation_points)
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