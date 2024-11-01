class Graph:
    @staticmethod
    def _get_graph(edge_list, n):
        graph = [[1e6 for _ in range(n)] for _ in range(n)]
        for edge in edge_list:
            src, dest, wt = edge
            graph[src][dest] = wt
            graph[dest][src] = wt

        for i in range(n):
            graph[i][i] = 0

        return graph

    @staticmethod
    def floyd_warshall(edge_list, n):
        graph = Graph._get_graph(edge_list, n)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        for i in range(n):
            if graph[i][i] < 0:
                return -1

        return graph


print(
    Graph.floyd_warshall(
        [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]],
        4
    )
)