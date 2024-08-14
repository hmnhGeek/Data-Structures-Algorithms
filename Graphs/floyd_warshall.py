class FloydWarshall:
    def __init__(self, adj_list):
        self.graph = adj_list

    def _build_adj_mtx(self):
        n = len(self.graph)
        mtx = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    mtx[i][j] = 0
                else:
                    for adj in self.graph[i]:
                        adj_node, edge_wt = adj
                        if adj_node == j:
                            mtx[i][j] = edge_wt
        return mtx

    def get_shortest_paths(self):
        adj_mtx = self._build_adj_mtx()

        for k in range(len(self.graph)):
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    adj_mtx[i][j] = min(adj_mtx[i][j], adj_mtx[i][k] + adj_mtx[k][j])

        for i in range(len(self.graph)):
            if adj_mtx[i][i] < 0:
                return -1

        return adj_mtx


sp1 = FloydWarshall(
    {
        0: [[1, 5]],
        1: [[2, -2], [5, -3]],
        2: [[4, 3]],
        3: [[2, 6], [4, -2]],
        4: [],
        5: [[3, 1]]
    }
).get_shortest_paths()

for row in sp1:
    print(row)

print()

sp2 = FloydWarshall(
    {
        0: [[3, 6]],
        1: [[0, 4], [2, 6]],
        2: [],
        3: [[1, 2]]
    }
).get_shortest_paths()

for row in sp2:
    print(row)

print()

sp3 = FloydWarshall(
    {
        0: [],
        1: [[0, 4], [2, -6]],
        2: [[3, 5]],
        3: [[1, -2]]
    }
).get_shortest_paths()

print(sp3)