class Graph:
    @staticmethod
    def _has_cycle(graph, node, visited, path_visited):
        visited[node] = True
        path_visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                if Graph._has_cycle(graph, adj_node, visited, path_visited):
                    return True
            elif path_visited[adj_node]:
                return True
        path_visited[node] = False
        return False

    @staticmethod
    def detect_cycle(graph):
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                has_cycle = Graph._has_cycle(graph, node, visited, path_visited)
                if has_cycle:
                    return True
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