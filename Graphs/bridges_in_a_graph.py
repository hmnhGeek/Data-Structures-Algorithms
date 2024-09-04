class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list
        self.timer = 1

    def _dfs_fetch_bridges(self, parent, node, visited, in_time, min_time, bridges):
        visited[node] = True
        in_time[node] = self.timer
        min_time[node] = self.timer
        self.timer += 1

        for adj_node in self.graph[node]:
            if adj_node == parent:
                continue

            if not visited[adj_node]:
                self._dfs_fetch_bridges(node, adj_node, visited, in_time, min_time, bridges)
                min_time[node] = min(min_time[node], min_time[adj_node])
                if min_time[adj_node] > min_time[node]:
                    bridges.append((node, adj_node))
            else:
                min_time[node] = min(min_time[node], min_time[adj_node])

    def get_bridges(self, start_node):
        min_time = {i: float("inf") for i in self.graph}
        in_time = {i: float("inf") for i in self.graph}
        visited = {i: False for i in self.graph}
        bridges = []
        self._dfs_fetch_bridges(None, start_node, visited, in_time, min_time, bridges)
        return bridges


class GraphFromEdges:
    def __init__(self, edge_list):
        self.graph = Graph(self._build_graph_from_edges(edge_list))

    def _build_graph_from_edges(self, edge_list):
        graph = {}
        for edge in edge_list:
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
        return self.graph.get_bridges(start_node)


print(GraphFromEdges([[0, 1], [1, 2], [2, 0], [1, 3]]).get_bridges(0))
print(GraphFromEdges([[0, 1]]).get_bridges(1))
