class Graph:
    _tin = 0

    @staticmethod
    def _dfs(graph, node, discovery_time, visited, lowest_time, parents, articulation_points):
        visited[node] = True
        discovery_time[node] = lowest_time[node] = Graph._tin
        Graph._tin += 1
        children = 0
        for adj_node in graph[node]:
            if not visited[adj_node]:
                children += 1
                parents[adj_node] = node
                Graph._dfs(graph, adj_node, discovery_time, visited, lowest_time, parents, articulation_points)
                lowest_time[node] = min(lowest_time[node], lowest_time[adj_node])
                if parents[node] is None and children > 1:
                    articulation_points[node] = True
                if parents[node] is not None and lowest_time[adj_node] >= discovery_time[node]:
                    articulation_points[node] = True
            if parents[node] != adj_node:
                lowest_time[node] = min(lowest_time[node], discovery_time[adj_node])

    @staticmethod
    def get_articulation_points(graph):
        Graph._tin = 0
        discovery_time = {i: None for i in graph}
        visited = {i: False for i in graph}
        lowest_time = {i: None for i in graph}
        parents = {i: None for i in graph}
        articulation_points = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Graph._dfs(graph, node, discovery_time, visited, lowest_time, parents, articulation_points)
        for node in articulation_points:
            if articulation_points[node]:
                print(node, end=" ")
        print()


# Graph.get_articulation_points(
#     {
#         0: [1, 2, 3],
#         1: [0],
#         2: [0, 3, 4, 5],
#         3: [0, 2],
#         4: [2, 6],
#         5: [2, 6],
#         6: [4, 5]
#     }
# )


Graph.get_articulation_points(
    {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2, 4],
        4: [3, 5],
        5: [4]
    }
)

Graph.get_articulation_points(
    {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D", "E"],
        "D": ["B", "C", "E"],
        "E": ["C", "D", "F", "G"],
        "F": ["E", "G"],
        "G": ["E", "F"]
    }
)