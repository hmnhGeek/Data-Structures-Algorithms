class Graph:
    tin = 1

    @staticmethod
    def _dfs(graph, visited, t_low, tin, parent, node, bridges):
        visited[node] = True
        tin[node] = Graph.tin
        t_low[node] = Graph.tin
        Graph.tin += 1
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Graph._dfs(graph, visited, t_low, tin, node, adj_node, bridges)
        for adj_node in graph[node]:
            if adj_node != parent:
                t_low[node] = min(t_low[node], t_low[adj_node])

        if parent is not None:
            if t_low[parent] < t_low[node]:
                bridges.append((parent, node))

    @staticmethod
    def find_bridges(graph):
        Graph.tin = 1
        bridges = []
        t_low = {i: 0 for i in graph}
        tin = {i: 0 for i in graph}
        visited = {i: False for i in graph}

        for node in graph:
            if not visited[node]:
                Graph._dfs(graph, visited, t_low, tin, None, node, bridges)
        return bridges


print(
    Graph.find_bridges(
        {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1],
            3: [1]
        }
    )
)

print(
    Graph.find_bridges(
        {
            1: [2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 5],
            5: [4, 6],
            6: [5, 7, 9],
            7: [6, 8],
            8: [7, 9, 10],
            9: [6, 8],
            10: [8, 11, 12],
            11: [10, 12],
            12: [10, 11]
        }
    )
)

print(
    Graph.find_bridges(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1],
            3: [0, 4],
            4: [3]
        }
    )
)

print(
    Graph.find_bridges(
        {
            0: [1, 2],
            1: [0, 2, 3, 4, 6],
            2: [0, 1],
            3: [1, 5],
            4: [1, 5],
            5: [3, 4],
            6: [1]
        }
    )
)

print(
    Graph.find_bridges(
        {
            0: [1],
            1: [2],
            2: [3],
            3: [4],
            4: []
        }
    )
)