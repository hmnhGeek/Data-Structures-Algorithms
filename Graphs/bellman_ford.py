class Graph:
    def __init__(self, adj_list):
        self.graph = adj_list

    def _get_edges(self):
        # This function converts adjacency list into a edge list in O(V + E) time.
        # The list will be of the form [source, adjacent node, edge weight].
        edge_list = []
        for node in self.graph:
            # for each adjacent node, we have data in this form: (adj_node, edge_wt)
            for adj_node in self.graph[node]:
                edge_list.append([node, adj_node[0], adj_node[1]])
        return edge_list

    def get_shortest_path_distances(self, source):
        # Time complexity is O(V * E) and space complexity is O(V + E) for edge list (of size E) and
        # the distances array (of size V).

        # Compute the edges of the graph in O(V + E) time.
        edges = self._get_edges()

        # initialize a distances array which will store all the distances from source node
        # to each and every node of the graph.
        distances = {i: float('inf') for i in self.graph}
        distances[source] = 0

        # loop for V - 1 times
        for i in range(len(self.graph) - 1):
            # for each edge, check if the distance to adjacent node is lower than the original
            # distance of the adjacent node from the source node. If yes, then simply update
            # the distance of the adjacent node to this smaller distance via node `node`.
            for edge in edges:
                node, adj_node, edge_wt = edge
                if distances[node] + edge_wt < distances[adj_node]:
                    distances[adj_node] = distances[node] + edge_wt

        # Do a Vth iteration to detect cycle. If the graph has no negative cycle, all the distances
        # must have been relaxed till V - 1 iterations. If there is a cycle, the algorithm can go
        # into an infinite loop (basically getting better distances every time). In that case, simply
        # return. Otherwise, return the distances array finally.
        for edge in edges:
            node, adj_node, edge_wt = edge
            if distances[node] + edge_wt < distances[adj_node]:
                return "Has negative cycle"

        return distances


graph1 = Graph(
    {
        0: [[1, 5]],
        1: [[2, -2], [5, -3]],
        2: [[4, 3]],
        3: [[2, 6], [4, -2]],
        4: [],
        5: [[3, 1]]
    }
)

graph2 = Graph(
    {
        0: [[3, 6]],
        1: [[0, 4], [2, 6]],
        2: [],
        3: [[1, 2]]
    }
)

graph3 = Graph(
    {
        0: [],
        1: [[0, 4], [2, -6]],
        2: [[3, 5]],
        3: [[1, -2]]
    }
)

print(graph1.get_shortest_path_distances(0))
print(graph2.get_shortest_path_distances(0))
print(graph3.get_shortest_path_distances(2))