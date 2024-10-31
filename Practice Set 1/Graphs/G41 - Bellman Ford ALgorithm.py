# Problem link - https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
# Solution - https://www.youtube.com/watch?v=0vVofAhAYjc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=41


class Graph:
    @staticmethod
    def _get_edges(graph):
        edges = []
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                edges.append((node, adj_node, wt))
        return edges

    @staticmethod
    def get_shortest_path(graph, source):
        if source not in graph:
            return
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        num_vertices = len(graph)
        edges = Graph._get_edges(graph)

        for i in range(num_vertices - 1):
            for edge in edges:
                u, v, edge_wt = edge
                if distances[v] > distances[u] + edge_wt:
                    distances[v] = distances[u] + edge_wt

        for edge in edges:
            u, v, edge_wt = edge
            if distances[v] > distances[u] + edge_wt:
                return "Negative cycle detected!"

        return distances.values()


print(
    Graph.get_shortest_path(
        {
            0: [[1, 5]],
            1: [[2, -2], [5, -3]],
            2: [[4, 3]],
            3: [[2, 6], [4, -2]],
            4: [],
            5: [[3, 1]]
        },
        0
    )
)

print(
    Graph.get_shortest_path(
        {
            0: [[1, 9]],
            1: []
        },
        0
    )
)

print(
    Graph.get_shortest_path(
        {
            0: [[1, 5]],
            1: [[0, 3], [2, -1]],
            2: [[0, 1]]
        },
        2
    )
)

print(
    Graph.get_shortest_path(
        {
            0: [[1, -1]],
            1: []
        },
        1
    )
)

print(
    Graph.get_shortest_path(
        {
            1: [[2, -2]],
            2: [[3, -1]],
            3: [[1, 2]]
        },
        3
    )
)